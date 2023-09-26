from django.db import models

# Create your models here. 
class Video(models.Model):
    title = models.CharField(max_length=255)
    video_file = models.FileField(upload_to='videos/')
    hls_playlist = models.FileField(upload_to='hls/', null=True, blank=True)
    def __str__(self):
        return self.title