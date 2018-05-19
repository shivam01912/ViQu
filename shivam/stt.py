import speech_recognition as sr
import time

r=sr.Recognizer()
mic = sr.Microphone()

print "Starting to record in 3 secs"
time.sleep(3)

print "Start speaking"
with mic as source:
	audio = r.listen(source)

print "Recording ended...Recognizing Speech"

print "You said : ",r.recognize_google(audio)