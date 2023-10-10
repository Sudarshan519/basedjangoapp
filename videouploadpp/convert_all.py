import subprocess
import os
# Input video file (720p)
input_video = "ElephantsDream.mp4"

# Output directory
output_dir = "output/"
# Ensure the output directory exists or create it
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
# FFmpeg command to convert and generate HLS
ffmpeg_command = [
    "ffmpeg",
    "-i", input_video,
    # 320p
    "-vf", "scale=320:-2",
    "-c:v", "h264",
    "-b:v", "500k",
    "-profile:v", "baseline",
    "-level", "3.0",
    "-s", "320x180",
    "-c:a", "aac",
    "-strict", "-2",
    "-b:a", "128k",
    "-f", "hls",
    "-hls_time", "6",
    "-hls_list_size", "0",
    "-hls_segment_filename", f"{output_dir}320p_%03d.ts",
    # 480p
    "-vf", "scale=480:-2",
    "-c:v", "h264",
    "-b:v", "800k",
    "-profile:v", "main",
    "-level", "3.1",
    "-s", "480x270",
    "-c:a", "aac",
    "-strict", "-2",
    "-b:a", "128k",
    "-f", "hls",
    "-hls_time", "6",
    "-hls_list_size", "0",
    "-hls_segment_filename", f"{output_dir}480p_%03d.ts",
    # 720p
    "-vf", "scale=720:-2",
    "-c:v", "h264",
    "-b:v", "1500k",
    "-profile:v", "high",
    "-level", "4.1",
    "-s", "720x404",
    "-c:a", "aac",
    "-strict", "-2",
    "-b:a", "192k",
    "-f", "hls",
    "-hls_time", "6",
    "-hls_list_size", "0",
    "-hls_segment_filename", f"{output_dir}720p_%03d.ts",
    # Master playlist
    "-map", "0",
    "-f", "hls",
    "-hls_time", "6",
    "-hls_list_size", "0",
    "-hls_segment_filename", f"{output_dir}720p_%03d.ts",
    f"{output_dir}master_playlist.m3u8",
]

# Run FFmpeg command
subprocess.run(ffmpeg_command)

print("Conversion complete.")
