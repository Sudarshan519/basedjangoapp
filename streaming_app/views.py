from http import HTTPStatus
import time
from django.http import FileResponse, JsonResponse, StreamingHttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404, render

# Create your views here.
from rest_framework import viewsets

from subscription.models import Subscription
import userr
from .models import *
from .serializers import *
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import FormParser, MultiPartParser

from rest_framework import mixins
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
from django.views.decorators.cache import never_cache
from rest_framework.response import Response
from rest_framework import generics
from django.utils.decorators import method_decorator
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

class WatchMovieAPI(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request,id, format=None):
        serializer_context = {
    'request': (request),
}    
        try:
      
            usersupscription= Subscription.objects.filter(user=request.user).latest('id')#.latest('id')#.filter(Subscription.user==request.user).latest
            print(usersupscription)
            if usersupscription:
                movie=Movie.objects.get(id=id)
                serializer=UserSerializer(request.user)
                if usersupscription.is_active:
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

def generate_video_chunks(video_path, chunk_size=1024 * 1024):
    with open(video_path, 'rb') as video_file:
        while True:
            chunk = video_file.read(chunk_size)
            if not chunk:
                break
            yield chunk
            time.sleep(1)  # Simulated delay between chunks


def stream_file(request, file_id):
    uploaded_file = get_object_or_404(Movie, pk=file_id)
    file_path = uploaded_file.movie_path.path
    chunk_size = 1024  # Set your desired chunk size
    # response = StreamingHttpResponse(generate_video_chunks(file_path), content_type="application/octet-stream")
    # response['Content-Disposition'] = 'attachment; filename="your_video.mp4"'

    # # response['Content-Disposition'] = 'attachment; filename="chunked_data.txt"'
    # return response
    # print(file_path)
    response = FileResponse(open(file_path, 'rb'))
    return response