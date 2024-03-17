import speech_recognition as sr

r = sr.Recognizer()

audio = "D:\Speech Recognation\temp.wav"

with sr.AudioFile(audio) as source:
    audio = r.record(source)
    print("done")


try:
    text = r.recognize_google(audio)
    print(text)
except:
    print("not recognized")