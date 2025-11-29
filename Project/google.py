import pyttsx3
import webbrowser

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

# Speak and open Google
speak("Opening Google")
webbrowser.open("https://www.google.com")
