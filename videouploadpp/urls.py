from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_video, name='upload_video'),
    path('', views.watch_videos, name='watch_videos'),
    path('play-video/<int:video_id>',views.play_hls_video,name='sdfsdf')
]
