from moviepy.editor import VideoFileClip
from dotenv import load_dotenv
import os
from funcao import fazer_sucrilhos, deixar_maiusculo

load_dotenv()

video = VideoFileClip(os.getenv("caminhopasta"))
duration = video.duration
minuteDuration = video.duration/60

print(f"Duração {minuteDuration:.2f} minutos")

resultado_final = fazer_sucrilhos('milho', 'acucar')
print(resultado_final)

print(deixar_maiusculo('teste'))