import os
import subprocess
from django.http import FileResponse, HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

from videouploadpp.convert_multi_audio_mkv import convert_to_hls
from .models import Video
from .forms import VideoUploadForm
def convert_to_hls(video_path, output_path):
    subprocess.run(['ffmpeg', '-i', video_path, '-c:v', 'h264', '-hls_time', '10', '-hls_list_size', '0', '-hls_segment_filename', f'{output_path}/segment%d.ts', f'{output_path}/index.m3u8'])
    # subprocess.run(['ffmpeg', '-i', video_path, '-c:v',"copy" ,"-c:a" ,"copy" "-scodec" ,"webvtt" ,"-f" ,"hls", "-hls_time" ,"4", "-hls_playlist_type", "vod" ,"-hls_segment_filename" ,f"{output_path}output_%03d.ts", "-hls_list_size" ,"0",  f'{output_path}/index.m3u8'])
    # ffmpeg -i SteinsGate_-_S01E01.mkv -c:v copy -c:a copy -scodec webvtt -f hls -hls_time 4 -hls_playlist_type vod -hls_segment_filename "output_%03d.ts" -hls_list_size 0 output.m3u8
#   '-vf', 'scale=1280:720',      # Resize to 720p resolution (adjust as needed)
    # '-r', '30',     
def upload_video(request):
    if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            video =form.save()
            
            #             # Generate HLS playlist
            video_path = video.video_file.path
            hls_output_path = os.path.join('media', 'hls', str(video.id))
            os.makedirs(hls_output_path, exist_ok=True)
            convert_to_hls(video.video_file.path,hls_output_path)
            
            # convert_to_hls(video_path, hls_output_path)
            video.hls_playlist = os.path.join(hls_output_path, 'index.m3u8')

            
            video.save()
            return JsonResponse({"playable-link":video.hls_playlist})#redirect('watch_videos')
    else:
        form = VideoUploadForm()
    return render(request, 'videouploadapp/upload_video.html', {'form': form})

def watch_videos(request):
    videos = Video.objects.all()
    return render(request, 'watch_videos.html', {'videos': videos})


def play_hls_video(request, video_id):
    try:
        video = Video.objects.get(id=video_id)
        hls_base_url = '/media/hls/'  # Update to match your directory structure
        playable_link = f'{hls_base_url}{video_id}/index.m3u8'
        return JsonResponse({"data":playable_link})
        # return render(request, 'videouploadpp/play_hls_video.html', {'playable_link': playable_link})
    except Video.DoesNotExist:
        return HttpResponse('Video not found', status=404)
    



# def upload_video(request):
#     if request.method == 'POST':
#         form = VideoUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             video = form.save()

#             # Generate HLS playlist
#             video_path = video.upload.path
#             hls_output_path = os.path.join('media', 'hls', str(video.id))
#             os.makedirs(hls_output_path, exist_ok=True)
#             convert_to_hls(video_path, hls_output_path)
#             video.hls_playlist = os.path.join(hls_output_path, 'index.m3u8')
#             video.save()

#             return redirect('video_detail', video_id=video.id)
#     else:
#         form = VideoUploadForm()
#     return render(request, 'upload.html', {'form': form})


def stream_video(request):
    # Define the path to the video file
    video_path = os.path.join("media", "sample.mp4")

    # Open the video file in binary mode
    video_file = open(video_path, "rb")

    # Set the content type for the response
    response = FileResponse(video_file, content_type="video/mp4")

    # Optionally, specify the content length (size of the video file)
    response["Content-Length"] = os.path.getsize(video_path)

    return response