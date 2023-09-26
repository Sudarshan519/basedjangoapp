import subprocess

# Input video file
input_file = 'input_video.mp4'

# Output video file
output_file = 'output_video.mp4'

# FFmpeg command for conversion (adjust as needed)
ffmpeg_command = [
    'ffmpeg',
    '-i', input_file,              # Input file
    '-vf', 'scale=1280:720',      # Resize to 720p resolution (adjust as needed)
    '-r', '30',                   # Set the frame rate to 30 FPS (adjust as needed)
    '-c:v', 'libx264',            # Video codec: H.264
    '-crf', '20',                 # Constant Rate Factor (adjust as needed)
    '-c:a', 'aac',                # Audio codec: AAC
    '-strict', 'experimental',    # Required for AAC codec
    '-b:a', '192k',               # Audio bitrate (adjust as needed)
    output_file                   # Output file
]

try:
    subprocess.run(ffmpeg_command, check=True)
    print(f'Successfully converted {input_file} to {output_file}')
except subprocess.CalledProcessError as e:
    print(f'Error: {e}')
# This script performs the following optimizations:

# Resizes the video to 720p resolution (1280x720 pixels). You can adjust the resolution as needed for your use case.
# Sets the frame rate to 30 frames per second (FPS). You can adjust the frame rate as needed.
# Uses the H.264 video codec and AAC audio codec for compatibility and efficiency.
# Replace input_video.mp4 and output_video.mp4 with the actual file paths you want to use. Adjust the FFmpeg command options to meet your specific requirements.

# Keep in mind that the -crf (Constant Rate Factor) and -b:a (audio bitrate) settings affect the trade-off between video quality and file size. Lower values result in higher quality but larger file sizes, while higher values result in lower quality but smaller file sizes. Adjust these settings according to your quality and size preferences.

# You can further optimize the conversion process based on your specific needs and hardware capabilities.





