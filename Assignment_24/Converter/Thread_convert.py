import time
from threading import Thread
from moviepy import VideoFileClip


start_time = time.time()

def convert(video):

    vid = VideoFileClip(video)
    audio_name = video.replace('.mp4','.mp3')
    vid.audio.write_audiofile(audio_name)

    vid.close()


videos = [
    'videos\Matter.mp4',
    'videos\Fulfil.mp4',
    'videos\D_Mahyar.mp4',
    'videos\Take_Me_Away.mp4',
    'videos\I _cant_fit_in.mp4'
    ]

threads = []

for video in videos :

    new_threads = Thread(target=convert, args=[video])
    threads.append(new_threads)

for t in threads :
    t.start()

for t in threads :
    t.join()


end_time = time.time()

print(end_time - start_time)
# Result = 8.853510618209839 took time