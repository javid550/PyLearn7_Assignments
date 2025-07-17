<<<<<<< HEAD
import time
from moviepy import VideoFileClip


start_time = time.time()


videos = [
    'videos\Matter.mp4',
    'videos\Fulfil.mp4',
    'videos\D_Mahyar.mp4',
    'videos\Take_Me_Away.mp4',
    'videos\I _cant_fit_in.mp4'
    ]

for video in videos :

    vid = VideoFileClip(video)
    audio_name = video.replace('.mp4','.mp3')
    vid.audio.write_audiofile(audio_name)

    vid.close()


end_time = time.time()

print(end_time - start_time)
=======
import time
from moviepy import VideoFileClip


start_time = time.time()


videos = [
    'videos\Matter.mp4',
    'videos\Fulfil.mp4',
    'videos\D_Mahyar.mp4',
    'videos\Take_Me_Away.mp4',
    'videos\I _cant_fit_in.mp4'
    ]

for video in videos :

    vid = VideoFileClip(video)
    audio_name = video.replace('.mp4','.mp3')
    vid.audio.write_audiofile(audio_name)

    vid.close()


end_time = time.time()

print(end_time - start_time)
>>>>>>> 6728bcf5d32f2f5a1539c3c4d5760f434ef7b9da
# Result : 9.543945550918579 took time