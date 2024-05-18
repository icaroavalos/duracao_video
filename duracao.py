from moviepy.editor import VideoFileClip
from dotenv import load_dotenv
import os

load_dotenv()

video = VideoFileClip(os.getenv("caminhopasta"))
duration = video.duration
minuteDuration = video.duration/60

print(f"Duração {minuteDuration:.2f} minutos")