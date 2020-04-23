import speech_recognition as sr
#from os import path
from pydub import AudioSegment

class convert:

    def convert(self):

        # files                                                                         
        src = "audio.mp3"
        dst = "audio.wav"

        # convert wav to mp3                                                            
        sound = AudioSegment.from_mp3('audio.mp3')
        sound.export(dst, format="wav")