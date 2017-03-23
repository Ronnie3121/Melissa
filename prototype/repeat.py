#!/usr/bin/env python2
import os
import sys
import speech_recognition as sr

def tts(message):
    """
    This function takes a message as an argument and converts it to speech depending on the OS.
    """
    if sys.platform == 'darwin':
        tts_engine = 'say'
        return os.system(tts_engine + ' ' + message)
    elif sys.platform == 'linux2' or sys.platform == 'linux':
        tts_engine = 'espeak'
        return os.system(tts_engine + ' "' + message + '"')

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
    message = r.recognize_google(audio)
    tts(message)
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition servicee; {0}".format(e))
