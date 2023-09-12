from django.db import models
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Movie(models.Model):
    title=models.CharField(max_length=256,null=True,blank=True)
    logo=models.ImageField(_("Banner Image"), upload_to='media/', height_field=None, width_field=None, max_length=None,null=True,blank=True)
    url=models.CharField(max_length=256)
    youtube_trailer_id=models.CharField(max_length=256)
    desc=models.CharField(max_length=256,null=True,blank=True)
    movie_path=models.FileField(upload_to='movie/', null=True,blank=True)
    price=models.CharField(max_length=256,null=True,blank=True)
    rating=models.FloatField( null=True,blank=True)
    discount=models.FloatField(null=True,blank=True)
    trending=models.CharField(choices=(("Trending","Trending"),("Latest","Latest")),default='Trending',max_length=80)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True )
    def img_preview(self): #new
        return mark_safe('<img src = "{url}" height = "80" width="140"/>'.format(
             url = self.logo.url
         ))
    # def video_preview(self):
    #     print(self.movie_path)
    #     return mark_safe(f'<video width="320" height="240" controls src="{self.movie_path}" autoplay></video>')
    def __str__(self) -> str:
        return self.title

class TVSeries(models.Model):
    title=models.CharField(max_length=256,null=True,blank=True)
    logo=models.ImageField(_("Banner Image"), upload_to='media/', height_field=None, width_field=None, max_length=None,null=True,blank=True)
    url=models.CharField(max_length=256)
    youtube_trailer_id=models.CharField(max_length=256)
    desc=models.CharField(max_length=256,null=True,blank=True)
    # movie_path=models.FileField(upload_to='movie/', null=True,blank=True)
    price=models.FloatField(max_length=256,null=True,blank=True)
    rating=models.FloatField( null=True,blank=True)
    discount=models.FloatField(null=True,blank=True,default=0)
    trending=models.CharField(choices=(("Trending","Trending"),("Latest","Latest")),default='Trending',max_length=80)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True )
    def img_preview(self): #new
        return mark_safe('<img src = "{url}" height = "80" width="140"/>'.format(
             url = self.logo.url
         ))
    def __str__(self) -> str:
        return self.title
class Episode(models.Model):
    label=models.CharField(max_length=256,null=True,blank=True)
    logo=models.ImageField(_("Banner Image"), upload_to='media/', height_field=None, width_field=None, max_length=None,null=True,blank=True)
    youtube_trailer_id=models.CharField(max_length=256)
    desc=models.CharField(max_length=256,null=True,blank=True)
    movie_path=models.FileField(upload_to='series/', null=True,blank=True)
    tv_show=models.ForeignKey(TVSeries,on_delete=models.CASCADE,related_name='episode')
    
    def __str__(self) -> str:
        return self.label