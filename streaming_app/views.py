from django.http import JsonResponse
from django.shortcuts import get_list_or_404, render

# Create your views here.
from rest_framework import viewsets
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
         

# from rest_framework import mixins
# class EpisodesViewSet( mixins.ListModelMixin,viewsets.GenericViewSet):
#     # pass
#     def list(self, request):
#             queryset = Episodes.objects.filter(tv_show=request.id)
#             doc = get_list_or_404(queryset)
#             serializer = EpisodesSerializer(doc,many=True,)
#             return JsonResponse(serializer.data,safe=False)
    