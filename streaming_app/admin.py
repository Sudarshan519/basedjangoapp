from django.contrib import admin
from .models import  Movie,TVSeries,Episode
# Register your models here.

# class MovieAdmin(admin.ModelAdmin):
    # list_display = ['url', 'img_preview',
    #                 # 'video_preview'
    #                 ]
admin.site.register(Movie )#, MovieAdmin)
admin.site.register(TVSeries)
admin.site.register(Episode)