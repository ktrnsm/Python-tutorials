###trial
import speech_recognition as sr
from pydub import AudioSegment

audio_file = AudioSegment.from_wav("C:/Users/Şebnem/Desktop/ses2nd.wav")
audio_file.export("audio_file.flac", format="flac")

r = sr.Recognizer()
with sr.AudioFile("audio_file.flac") as source:
    audio = r.record(source,duration=10, offset=0)

try:
    text = r.recognize_google(audio, show_all=False)
    print(text)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))