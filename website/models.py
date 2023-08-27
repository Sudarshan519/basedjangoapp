from decimal import Decimal
from django.db import models
from django.forms import CharField, DecimalField, FloatField

# Create your models here.
class SiteSettingsData(models.Model):
    id=models.IntegerField(primary_key=True)
    title=models.CharField(default="default",max_length=256,)
    desc=models.CharField(default="default",max_length=256)
    exchange_rate=models.DecimalField(max_digits=20, decimal_places=2,default=0.00 )
    service_fee=models.DecimalField(max_digits=6, decimal_places=2,default=0.00)
    app_store_link=models.CharField(default="default",max_length=256)
    play_store_link=models.CharField(default="default",max_length=256)
    follow_up_label=models.CharField(default="default",max_length=256)
    follow_up_desc=models.CharField(default="default",max_length=256)
    what_you_can_do=models.CharField(default="default",max_length=256)
    what_you_can_do_desc=models.CharField(default="default",max_length=256)
    customer_video=models.CharField(default="default",max_length=256)
    customer_video_label=models.CharField(default="default",max_length=256)
    mobile_logo=models.CharField(default="default",max_length=256)
    play_store_icon=models.CharField(default="default",max_length=256)
    app_store_icon=models.CharField(default="default",max_length=256)
    background_image=models.CharField(default="default",max_length=256)
    background_image_second=models.CharField(default="default",max_length=256)
    # whyus=models.ForeignKey("website.WhyChooseUs",  on_delete=models.CASCADE,related_name="why_us")
    # steps=models.ForeignKey("website.StepsToStartUp",on_delete=models.CASCADE)
    # what_you_can_do=models.ForeignKey("website.WhatYouCanDo",on_delete=models.CASCADE)
    # terms=models.ForeignKey("website.TermsAndConditions",on_delete=models.CASCADE)
class WhyChooseUs(models.Model):
    fontawesome_icon=models.CharField(default="default",max_length=256)
    title=models.CharField(default="default",max_length=256)
    desc=models.CharField(default="default",max_length=256)
    sitesetting=models.ForeignKey("website.SiteSettingsData",  on_delete=models.CASCADE,related_name="whyus",default=1)
class StepsToStartUp(models.Model):
    title=models.CharField(default="default",max_length=256)
    desc=models.CharField(default="default",max_length=256)
    sitesetting=models.ForeignKey("website.SiteSettingsData",  on_delete=models.CASCADE,related_name="steps",default=1)
class WhatYouCanDo(models.Model):
    fontawesome_icon=models.CharField(default="default",max_length=256)
    label=models.CharField(default="default",max_length=256)
    sitesetting=models.ForeignKey("website.SiteSettingsData",  on_delete=models.CASCADE,related_name="whatyoucando",default=1)
class TermsAndConditions(models.Model):
    label=models.CharField(default="default",max_length=256)
    link=models.CharField(default="default",max_length=256)
    sitesetting=models.ForeignKey("website.SiteSettingsData",  on_delete=models.CASCADE,related_name="terms",default=1)