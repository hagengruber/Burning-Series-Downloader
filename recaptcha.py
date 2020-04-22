import speech_recognition as sr
#from os import path
from pydub import AudioSegment

# files                                                                         
src = "audio.mp3"
dst = "test.wav"

# convert wav to mp3                                                            
sound = AudioSegment.from_mp3('audio.mp3')
sound.export(dst, format="wav")

r = sr.Recognizer()

with sr.WavFile('test.wav') as source:
    audio = r.record(source)

try: 
    text = r.recognize_google(audio, language='de-DE') 
    print("you said: " + text)

except sr.UnknownValueError: 
    print("Google Speech Recognition could not understand audio") 

except sr.RequestError as e: 
    print("Could not request results from Google Speech Recognition service; {0}".format(e)) 