import subprocess

input_video = "input_video.mp4"
output_formats = [
    {"format": "mp4", "resolution": "1280x720", "bitrate": "1500k"},
    {"format": "webm", "resolution": "640x360", "bitrate": "1000k"},
]

for output_format in output_formats:
    output_file = f"output_{output_format['resolution']}.{output_format['format']}"
    ffmpeg_command = [
        "ffmpeg",
        "-i", input_video,
        "-vf", f"scale={output_format['resolution']}",
        "-b:v", output_format['bitrate'],
        "-c:a", "aac",
        output_file
    ]

    try:
        subprocess.run(ffmpeg_command, check=True)
        print(f"Successfully created {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
