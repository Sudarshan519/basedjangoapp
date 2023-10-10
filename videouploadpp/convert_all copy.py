import subprocess
import os

# Input video file (replace with your video file)
input_video = "[Kayoanime] Monster - S01E01.mkv"

# Output directory
output_dir = "output/"

# Ensure the output directory exists or create it
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# List of resolutions and their corresponding bitrates
resolutions = [
    {"width": 320, "height": 180, "bitrate": "500k"},
    {"width": 480, "height": 270, "bitrate": "800k"},
    {"width": 720, "height": 404, "bitrate": "1500k"}
]

# List to store individual playlist paths
playlist_paths = []

for resolution in resolutions:
    # Output file path for the current resolution
    output_file = f"{output_dir}{resolution['width']}p.m3u8"

    # FFmpeg command to convert to HLS
    ffmpeg_command = [
        "ffmpeg",
        "-i", input_video,
        "-vf", f"scale={resolution['width']}:{resolution['height']}",
        "-c:v", "h264",
        "-preset:v", "ultrafast",
        "-b:v", resolution['bitrate'],
        # "-profile:v", "main",
        "-level", "3.1",
        "-s", f"{resolution['width']}x{resolution['height']}",
        "-c:a", "aac",
        "-strict", "-2",
        "-b:a", "128k",
        "-f", "hls",
        "-hls_time", "6",
        "-hls_list_size", "0",
        "-hls_segment_filename", f"{output_dir}{resolution['width']}p_%03d.ts",
        output_file,
    ]

    subprocess.run(ffmpeg_command)

    # Store the path of the generated individual playlist
    playlist_paths.append(output_file)

# Create the content for the master playlist
master_playlist_content = "#EXTM3U\n"

for index, playlist_path in enumerate(playlist_paths):
    resolution = os.path.basename(playlist_path).split(".")[0]  # Extract resolution from the filename
    master_playlist_content += f"#EXT-X-STREAM-INF:BANDWIDTH={resolutions[index]['bitrate']},RESOLUTION={resolution}\n"
    master_playlist_content += f"{os.path.basename(playlist_path)}\n"

# Write the master playlist content to a file
master_playlist_path = os.path.join(output_dir, "master_playlist.m3u8")

with open(master_playlist_path, "w") as master_playlist_file:
    master_playlist_file.write(master_playlist_content)

print("Conversion complete.")
