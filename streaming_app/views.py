from http import HTTPStatus
import os
import subprocess
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_list_or_404, redirect, render
# from fastapi import openapi

# Create your views here.
from rest_framework import viewsets
from streaming_app.video_upload_form import VideoUploadForm

from subscription.models import Subscription
import userr
from .models import *
from .serializers import *
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import FormParser, MultiPartParser
from django.utils.decorators import method_decorator
from rest_framework import mixins
from django.views.decorators.cache import never_cache
# @swagger_auto_schema(tags=['MOVIE'],method='post', operation_description='',request_body=MovieSerializer,)

class MovieViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    parser_classes = (FormParser, MultiPartParser)


class EpisodesViewSet(viewsets.ModelViewSet):
    queryset=Episode.objects.all()
    serializer_class=EpisodeSerializer
    parser_classes = (FormParser, MultiPartParser)


class TVShowsViewSet(viewsets.ModelViewSet):
    episode=EpisodeSerializer(many=True,read_only=True)
    queryset = TVSeries.objects.all()
    serializer_class = TVSeriesSerializer
    parser_classes = (FormParser, MultiPartParser)
from rest_framework.views import APIView
from rest_framework import permissions
from django.http import HttpRequest
@swagger_auto_schema(tags=['user'])
class UserDashboard(APIView):
    # permission_classes = (permissions.IsAuthenticated,)
    permission_classes = [permissions.IsAuthenticated]
    # @permission_classes([permissions.IsAuthenticated])
    # @login_required
    # @employee_required
    def get(self, request, format=None):
        serializer_context = {
    'request': (request),
}

        serializer=UserSerializer(request.user)
        return JsonResponse(serializer.data,safe=False)
from rest_framework.response import Response
from rest_framework import generics
class HomeAPI(generics.ListAPIView):
    movies_queryset = Movie.objects.all()
    tvshow_queryset = TVSeries.objects.all()
    parser_classes = (FormParser, MultiPartParser)
    @method_decorator(never_cache)
    def list(self, request, *args, **kwargs):
        movie_serializer = MovieSerializer(self.movies_queryset, many=True)
        tvshow_serializer = TVSeriesSerializer(self.tvshow_queryset, many=True)
        
        response_data = {
            'movies': movie_serializer.data,
            'tvshows': tvshow_serializer.data,
        }
        
        return Response(response_data)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
@api_view(['GET'])

# @swagger_auto_schema(tags=["my_custom_tag"], method='delete', manual_parameters=[openapi.Parameter(
#     name='delete_form_param',
#      in_=openapi.IN_FORM,
#     type=openapi.TYPE_INTEGER,
#     description="this should not crash (form parameter on DELETE method)"
# )])
def api_root(request, format=None):
    movies_queryset = Movie.objects.all()
    tvshow_queryset = TVSeries.objects.all()
    movie_serializer = MovieSerializer(movies_queryset, many=True ).data
    tvshow_serializer = TVSeriesSerializer(tvshow_queryset, many=True ).data
    # top,trending, fetaured ,latest
    return JsonResponse({
        'movies': movie_serializer,
        'tvshows':tvshow_serializer,
    })
class WatchMovieAPI(APIView):
    # permission_classes = [permissions.IsAuthenticated]
    def get(self, request,id, format=None):
        return JsonResponse(MoviePathSerializer(Movie.objects.get(id=id)).data,safe=False)
        serializer_context = {
    'request': (request),
}    
        try:
            if request.user   :
                usersupscription= Subscription.objects.filter(user=request.user).latest('id')#.latest('id')#.filter(Subscription.user==request.user).latest
                print(usersupscription)
            if usersupscription or True:
                movie=Movie.objects.get(id=id)
                movie.view_count+=1
                movie.save()
                if request.user:
                    serializer=UserSerializer(request.user)
                if usersupscription.is_active or True:
                    print(True)
                    return JsonResponse(MoviePathSerializer(movie).data,safe=False)
                return JsonResponse({"error":"subscription not found"})
                # return JsonResponse(serializer.data,safe=False)
            else:
                return JsonResponse({
                    "status":HTTPStatus.NOT_FOUND,
                    "error":"Subscription Not found."})
            
        except Exception as e:
            
            return JsonResponse({
                "status":HTTPStatus.NOT_FOUND,
                "error":str(e)})
# from rest_framework import mixins
# class EpisodesViewSet( mixins.ListModelMixin,viewsets.GenericViewSet):
#     # pass
#     def list(self, request):
#             queryset = Episodes.objects.filter(tv_show=request.id)
#             doc = get_list_or_404(queryset)
#             serializer = EpisodesSerializer(doc,many=True,)
#             return JsonResponse(serializer.data,safe=False)

def play_hls_video(request, video_id):
    try:
        video = Movie.objects.get(id=video_id)
        hls_base_url = '/media/hls/'  # Update to match your directory structure
        playable_link = f'{hls_base_url}{video_id}/index.m3u8'
        return render(request, 'play_hls_video.html', {'playable_link': playable_link})
    except Movie.DoesNotExist:
        return HttpResponse('Video not found', status=404)
    

def convert_to_hls(video_path, output_path):
    subprocess.run(['ffmpeg', '-i', video_path, '-c:v', 'h264', '-hls_time', '10', '-hls_list_size', '0', '-hls_segment_filename', f'{output_path}/segment%d.ts', f'{output_path}/index.m3u8'])

def upload_video(request):
    if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save()

            # Generate HLS playlist
            video_path = video.upload.path
            hls_output_path = os.path.join('media', 'hls', str(video.id))
            os.makedirs(hls_output_path, exist_ok=True)
            convert_to_hls(video_path, hls_output_path)
            video.hls_playlist = os.path.join(hls_output_path, 'index.m3u8')
            video.save()

            return redirect('video_detail', video_id=video.id)
    else:
        form = VideoUploadForm()
    return render(request, 'upload.html', {'form': form})

class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        video_id = self.kwargs.get('video_id')
        return MovieComment.objects.filter(video_id=video_id, parent=None)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MovieComment.objects.all()
    serializer_class = CommentSerializer