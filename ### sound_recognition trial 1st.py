### sound_recognition trial 1st
import speech_recognition as sr

# Create a recognizer instance
r = sr.Recognizer()

# Load the audio file
audio_file = sr.AudioFile('C:/Users/Şebnem/Desktop/ses2nd.wav')

# Open the audio file and read the audio data into a variable
with audio_file as source:
    audio_data = r.record(source)

# Transcribe the audio file
transcription = r.re(audio_data)

# Print the transcription
print(transcription)


import deepspeech

# Load the DeepSpeech model
model = deepspeech.Model('path/to/deepspeech/model.pbmm')

# Load the audio file
with open('path/to/audio/file.wav', 'rb') as audio_file:
    audio_data = audio_file.read()

# Transcribe the audio file
transcription = model.stt(audio_data)
print(transcription)




