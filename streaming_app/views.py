from django.http import JsonResponse
from django.shortcuts import get_list_or_404, render

# Create your views here.
from rest_framework import viewsets
from .models import *
from .serializers import *
class MovieViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer



class EpisodesViewSet(viewsets.ModelViewSet):
    queryset=Episode.objects.all()
    serializer_class=EpisodeSerializer


class TVShowsViewSet(viewsets.ModelViewSet):
    episode=EpisodeSerializer(many=True,read_only=True)
    queryset = TVSeries.objects.all()
    serializer_class = TVSeriesSerializer
# from rest_framework import mixins
# class EpisodesViewSet( mixins.ListModelMixin,viewsets.GenericViewSet):
#     # pass
#     def list(self, request):
#             queryset = Episodes.objects.filter(tv_show=request.id)
#             doc = get_list_or_404(queryset)
#             serializer = EpisodesSerializer(doc,many=True,)
#             return JsonResponse(serializer.data,safe=False)
    