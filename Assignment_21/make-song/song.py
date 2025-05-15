import pysynth

test = [('e',4) , ('g',4) , ('a',4) , ('g',4) , ('e',2) , ('f',4) , ('e',2)]

pysynth.make_wav(test , fn = "song.wav")