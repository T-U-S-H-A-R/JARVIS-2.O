import pyttsx3
from datetime import datetime

# -------- SPEAK FUNCTION --------
def speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 170)
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)
    print(text)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

# Announce the current time directly
current_time = datetime.now().strftime("%H:%M:%S")
speak("The current time is " + current_time)
