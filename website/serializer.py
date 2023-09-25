from rest_framework import serializers
from .models import *
class WhyUsSerializer(serializers.ModelSerializer):
    class Meta:
        model=WhyChooseUs
        exclude=('sitesetting',)
        # fields="__all__"
        

class StepsToStartUpSerializer(serializers.ModelSerializer):
    class Meta:
        model=StepsToStartUp
        exclude=('sitesetting',)
        # fields="__all__"


class WhatYouCanDoSerializer(serializers.ModelSerializer):
    class Meta:
        model=WhatYouCanDo
        exclude=('sitesetting',)
        # fields="__all__"

class TermsAndConditionsSerializer(serializers.ModelSerializer):
    class Meta:
        model=TermsAndConditions
        exclude=('sitesetting',)
        # fields="__all__"

from website.models import SiteSettingsData, StepsToStartUp, TermsAndConditions, WhatYouCanDo, WhyChooseUs
class SiteSettingsSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField()
    whyus=WhyUsSerializer(many=True)
    steps=StepsToStartUpSerializer(many=True)
    whatyoucando=WhatYouCanDoSerializer(many=True)
    terms=TermsAndConditionsSerializer(many=True)
    class Meta:
        model= SiteSettingsData 
        fields="__all__"
        include=('id')
    def update(self, instance, validated_data):
        whyus = validated_data.pop('whyus')
        steps=validated_data.pop('steps')
        whatyoucando=validated_data.pop('whatyoucando')
        terms=validated_data.pop('terms')
        site=instance
        for whyus_data in whyus:
            WhyChooseUs.objects.create(sitesetting=site,**whyus_data)
        for steps_data in steps:
            StepsToStartUp.objects.create(sitesetting=site,**steps_data)
        for what_you_can_do_data in whatyoucando:
            WhatYouCanDo.objects.create(sitesetting=site,**what_you_can_do_data)
        for terms_data in terms:
            TermsAndConditions.objects.create(sitesetting=site,**terms_data)
        return site
    def create(self, validated_data):
        whyus = validated_data.pop('whyus')
        steps=validated_data.pop('steps')
        whatyoucando=validated_data.pop('whatyoucando')
        terms=validated_data.pop('terms')
        site=SiteSettingsData.objects.create(**validated_data)
        for whyus_data in whyus:
            WhyChooseUs.objects.create(sitesetting=site,**whyus_data)
        for steps_data in steps:
            StepsToStartUp.objects.create(sitesetting=site,**steps_data)
        for what_you_can_do_data in whatyoucando:
            WhatYouCanDo.objects.create(sitesetting=site,**what_you_can_do_data)
        for terms_data in terms:
            TermsAndConditions.objects.create(sitesetting=site,**terms_data)
        return site
        # tracks_data = validated_data.pop('tracks')
        # album = Album.objects.create(**validated_data)
        # for track_data in tracks_data:
        #     Track.objects.create(album=album, **track_data)
        # return album
