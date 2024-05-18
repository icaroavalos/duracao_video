from moviepy.editor import VideoFileClip
from dotenv import load_dotenv
import os

load_dotenv()

video = VideoFileClip(os.getenv("caminhopasta"))
duration = video.duration

print(f"Duração {duration} segundos")