import pyttsx3
import time
import os
from gtts import gTTS

# ------------------- Jarvis Voice Function -------------------
def jarvis_speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 170)
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()
    engine.stop()

# ------------------- German Voice Function (gTTS) -------------------
def german_speak(text):
    print(f"German: {text}")
    filename = f"temp_voice_{int(time.time() * 1000)}.mp3"
    tts = gTTS(text=text, lang='de')  # German language
    tts.save(filename)
    os.system(f'start /min "" "{filename}"')
    time.sleep(4)  # Wait for the audio to play
    os.remove(filename)

# ------------------- AUTOMATIC GERMAN SYSTEM CHECK -------------------
time.sleep(1)
jarvis_speak("Hello Jarvis, can you hear me?")
german_speak("Ja, ich höre Sie.")

jarvis_speak("What is your status?")
german_speak("Ich arbeite im normalen Betriebsmodus.")

jarvis_speak("Are you ready to start work?")
german_speak("Ja, ich bin vollständig bereit.")

jarvis_speak("Good, begin the system check.")
german_speak("Verstanden. Starte die Systemüberprüfung.")

jarvis_speak("Checking power systems...")
german_speak("Überprüfe die Energiesysteme... Alles funktioniert einwandfrei.")

jarvis_speak("What about the network connection?")
german_speak("Die Netzwerkverbindung ist stabil. Internet ist verfügbar.")

jarvis_speak("Run diagnostics on the sensors.")
german_speak("Führe Diagnosen der Sensoren durch. Kamera, Mikrofon und Temperatursensoren funktionieren einwandfrei.")

jarvis_speak("How is your memory and storage status?")
german_speak("Speicherauslastung liegt bei 35 %. Festplattenspeicher ist ausreichend. Systemzustand optimal.")

jarvis_speak("Excellent. Now check the voice recognition module.")
german_speak("Teste das Spracherkennungsmodul. Antwortgeschwindigkeit ist normal.")

jarvis_speak("Very good. Are all systems ready for deployment?")
german_speak("Ja, alle Systeme sind vollständig einsatzbereit.")

jarvis_speak("Excellent, everything looks perfect.")
german_speak("Ausgezeichnet. Alles läuft reibungslos.")

jarvis_speak("Jarvis, await further instructions.")
german_speak("Verstanden. Ich warte auf Ihre nächsten Befehle.")
