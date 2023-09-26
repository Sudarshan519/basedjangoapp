import os
import subprocess
from django.http import HttpResponse
from django.conf import settings
import ffmpeg
import threading

def extract_video(input_mkv, output_directory):
    # Extract video stream
    output_video = os.path.join(output_directory, 'video.mp4')
    subprocess.run(['ffmpeg', '-i', input_mkv, '-c:v', 'copy', output_video])


def convert_audio_track(input_mkv, output_directory, audio_track_index):
    # Extract audio track
    output_audio = os.path.join(output_directory, f'audio_track_{audio_track_index}.aac')
    subprocess.run(['ffmpeg', '-i', input_mkv, '-map', f'0:a:{audio_track_index}', '-strict', '-2', output_audio])

    # Convert audio track to HLS
    output_hls = os.path.join(output_directory, f'audio_track_{audio_track_index}.m3u8')
    subprocess.run(['ffmpeg', '-i', output_audio, '-f', 'hls', '-hls_time', '10', '-hls_playlist_type', 'vod',
                    '-hls_segment_filename', f'audio_track_{audio_track_index}_%03d.ts', output_hls])

def convert_to_hls(input_path,output_directory):
    # Path to the input MKV file
    input_mkv = input_path

    # Output directory for HLS content
    # output_directory = os.path.join(settings.MEDIA_ROOT, 'hls')

    # Create the output directory if it doesn't exist
    # os.makedirs(output_directory, exist_ok=True)

    # Extract audio tracks from the MKV file
    input_probe = ffmpeg.probe(input_mkv, v='error', select_streams='a:0')
    num_audio_tracks = len(input_probe['streams'])
    # Create a thread for each audio track conversion
    threads = []
    for i in range(num_audio_tracks):
        thread = threading.Thread(target=convert_audio_track, args=(input_mkv, output_directory, i))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()



    # for i in range(num_audio_tracks):
    #     output_audio = os.path.join(output_directory, f'audio_track_{i}.aac')
    #     subprocess.run(['ffmpeg', '-i', input_mkv, '-map', f'0:a:{i}', '-strict', '-2', output_audio])

    # # Convert audio tracks to HLS streams
    # for i in range(num_audio_tracks):
    #     output_audio = os.path.join(output_directory, f'audio_track_{i}.aac')
    #     output_hls = os.path.join(output_directory, f'audio_track_{i}.m3u8')

    #     subprocess.run(['ffmpeg', '-i', output_audio, '-f', 'hls', '-hls_time', '10', '-hls_playlist_type', 'vod',
    #                     '-hls_segment_filename', f'audio_track_{i}_%03d.ts', output_hls])

    # Generate a master playlist
    with open(os.path.join(output_directory, 'index.m3u8'), 'w') as master_playlist:
        master_playlist.write('#EXTM3U\n')
        for i in range(num_audio_tracks):
            master_playlist.write(f'#EXT-X-STREAM-INF:BANDWIDTH=1280000,AUDIO="audio"\n')
            master_playlist.write(f'audio_track_{i}.m3u8\n')

    return master_playlist