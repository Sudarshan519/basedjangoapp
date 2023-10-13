import subprocess
import json
import os

# Input video file (replace with your video file)
input_video = "[Kayoanime] Monster - S01E56.mkv"

# Output directory
output_dir = f"1.{input_video.split('.')[0].replace(' ','')}/"

# Ensure the output directory exists or create it
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Run FFprobe to get stream information
ffprobe_command = [
    "ffprobe",
    # "-v", "error",
    "-show_entries", "stream=index:stream_tags=language:stream=codec_name",
    "-of", "json",
    input_video,
]

try:
    ffprobe_output = subprocess.check_output(ffprobe_command, universal_newlines=True)
    print(ffprobe_output)
    data = json.loads(ffprobe_output)
    # print(ffprobe_output)
    audio_streams = []
    subtitle_streams = []

    for stream in data["streams"][:4]:
        # print(stream)
        stream_info = {
            "index": stream["index"],
            "codec_name": stream["codec_name"],
            "language": stream["tags"]["language"] if "tags" in stream and "language" in stream["tags"] else None,
        }

        if stream_info["codec_name"] == "opus":
            audio_streams.append(stream_info)
        elif stream_info["codec_name"] == "hevc":
            video_stream = stream_info
        elif stream_info["codec_name"] == "ass" :
            subtitle_streams=stream_info
        else:
            pass
    # # audio stream conversion
    # print(audio_streams)
    # # Generate HLS playlists for all audio streams
    for audio_stream in audio_streams:
        output_audio_file = f"{output_dir}output_audio_{audio_stream['index']}.m3u8"

        ffmpeg_audio_command = [
            "ffmpeg",
            "-i", input_video,
            "-vn",
            # "-acodec","copy",
            # "-c:a", "libopus",
            # "-strict", "-2",
            "-b:a", "128k",
            "-f", "hls",
            "-hls_time", "6",
            "-hls_list_size", "0",
            "-hls_segment_filename", f"{output_dir}output_audio_{audio_stream['index']}_%03d.ts",
            "-map", f"0:a:{audio_stream['index']}?",
            output_audio_file,
        ]

        subprocess.run(ffmpeg_audio_command)

    # video stream conversion
    print(video_stream)
    # Generate HLS playlists for the video stream
    output_video_file = f"{output_dir}output_video.m3u8"

    ffmpeg_video_command = [
        "ffmpeg",
        "-i", input_video,
        "-c:v", "copy",
        "-f", "hls",
        "-hls_time", "6",
        "-hls_list_size", "0",
        "-hls_segment_filename", f"{output_dir}output_video_%03d.ts",
        "-map", f"0:v:0",
        output_video_file,
    ]

    subprocess.run(ffmpeg_video_command)

    # # subtitle stream conversion
    # print(subtitle_streams)    
    #     # Create the content for the master playlist
    master_playlist_content = "#EXTM3U\n#EXT-X-VERSION:3\n"

    # # Video playlist
    master_playlist_content += f"# Video Stream\n#EXT-X-STREAM-INF:BANDWIDTH=1000000,RESOLUTION=1280x720\noutput_video.m3u8\n"

    # Audio playlists
    for audio_stream in audio_streams:
        master_playlist_content += f"# Audio Tracks\n#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID=\"audio\",NAME=\"{audio_stream['language']}\",LANGUAGE=\"{audio_stream['language']}\",DEFAULT=YES,AUTOSELECT=YES,URI=\"output_audio_{audio_stream['index']}.m3u8\"\n"

    # # Subtitle playlists
    # for subtitle_stream in subtitle_streams:
    #     master_playlist_content += f"# Subtitle Tracks\n#EXT-X-MEDIA:TYPE=SUBTITLES,GROUP-ID=\"subs\",LANGUAGE=\"{subtitle_stream['language']}\",NAME=\"{subtitle_stream['language']}\",DEFAULT=YES,AUTOSELECT=YES,URI=\"output_subtitle_{subtitle_stream['index']}.m3u8\"\n"

    # Write the master playlist content to a file
    master_playlist_path = os.path.join(output_dir, "master_playlist.m3u8")

    with open(master_playlist_path, "w") as master_playlist_file:
        master_playlist_file.write(master_playlist_content)
except:
    pass

# EXAMPLE
#EXTM3U
#EXT-X-VERSION:3
# Video Stream
#EXT-X-STREAM-INF:BANDWIDTH=1000000,RESOLUTION=1280x720
# output_video.m3u8
# Audio Tracks
#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="audio",NAME="eng",LANGUAGE="eng",DEFAULT=YES,AUTOSELECT=YES,URI="output_audio_1.m3u8"
# Audio Tracks
#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="audio",NAME="jpn",LANGUAGE="jpn",DEFAULT=YES,AUTOSELECT=YES,URI="output_audio_2.m3u8"
# Subtitle Stream (if available)
#EXT-X-MEDIA:TYPE=SUBTITLES,GROUP-ID="subs",LANGUAGE="en",NAME="English",DEFAULT=YES,AUTOSELECT=YES,FORCED=NO,URI="output_audio_2_vtt.m3u8"