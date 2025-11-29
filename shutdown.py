import os
import pyttsx3
import time

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 170)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

# Speak before shutdown
speak("Shutting down sir")

# Small delay to allow speech to finish properly before shutdown
time.sleep(2)

# Execute shutdown command
os.system("shutdown /s /t 5")
