# battery.py
import psutil
import pyttsx3

def jarvis_speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 170)
    voices = engine.getProperty("voices")
    if len(voices) > 1:
        engine.setProperty("voice", voices[1].id)
    print(text)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

# -------- MAIN --------
jarvis_speak(f"Sir, the battery percentage is {psutil.sensors_battery().percent} percent.")
