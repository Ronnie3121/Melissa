#!/usr/bin/env python2

import speech_recognition as sr
# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# recognise speech using Google Speech Recognition
try:
    # for testing purposes, you're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition servicee; {0}".format(e))
    