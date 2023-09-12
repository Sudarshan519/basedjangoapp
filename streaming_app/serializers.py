from rest_framework import serializers
from .models import *
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields="__all__"


class EpisodeSerializer(serializers.ModelSerializer):

    class Meta:
        model=Episode
        fields=("id","label","tv_show","desc")

        
class TVSeriesSerializer(serializers.ModelSerializer):
    episode=EpisodeSerializer(many=True,read_only=True)


    class Meta:
        model=TVSeries
        exclude=()
        
        include=["episode"]
 