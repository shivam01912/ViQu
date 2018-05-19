import speech_recognition as sr
import time

r=sr.Recognizer()
r.energy_threshold = 4000

mic = sr.Microphone()

print "Starting to record in 3 secs"
time.sleep(3)

print "Start speaking"
with mic as source:
	# r.adjust_for_ambient_noise(source)
	audio = r.record(source,duration=10)

print "Recording ended...Recognizing Speech"

print "You said : ",r.recognize_google(audio)