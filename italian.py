import pyttsx3
from gtts import gTTS
import os
import time

# ------------------- English Jarvis voice -------------------
def jarvis_speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 170)
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()
    engine.stop()

# ------------------- Italian TTS -------------------
def italian_speak(text):
    """Italian"""
    print(f"IT: {text}")
    filename = f"it_{int(time.time() * 1000)}.mp3"
    tts = gTTS(text=text, lang="it")
    tts.save(filename)
    os.system(f'start /min "" "{filename}"')  # Play minimized
    time.sleep(max(len(text)/15, 3))  # Adjust duration based on text length
    os.remove(filename)

# ------------------- Italian System Check -------------------
time.sleep(1)
jarvis_speak("Hello Jarvis, can you hear me?")
italian_speak("Sì, ti sento.")  # Yes, I can hear you

jarvis_speak("What is your status?")
italian_speak("Sto funzionando normalmente.")  # I am operating normally

jarvis_speak("Are you ready to start work?")
italian_speak("Sì, sono pronto.")  # Yes, I am ready

jarvis_speak("Good, begin the system check.")
italian_speak("Ricevuto. Avvio il controllo del sistema.")  # Understood, starting system check

jarvis_speak("Checking power systems...")
italian_speak("Sto controllando i sistemi di alimentazione... Tutto è normale.")  # All normal

jarvis_speak("What about the network connection?")
italian_speak("La connessione di rete è stabile. Internet è disponibile.")  # Network stable

jarvis_speak("Run diagnostics on the sensors.")
italian_speak("Eseguo la diagnostica dei sensori. Fotocamera, microfono e sensori di temperatura funzionano correttamente.")  

jarvis_speak("How is your memory and storage status?")
italian_speak("Utilizzo della memoria al 35%. Spazio di archiviazione sufficiente. Stato ottimale.")  

jarvis_speak("Excellent. Now check the voice recognition module.")
italian_speak("Test del modulo di riconoscimento vocale in corso. La velocità di risposta è regolare.")  

jarvis_speak("Very good. Are all systems ready for deployment?")
italian_speak("Sì, tutti i sistemi sono completamente pronti all'uso.")  

jarvis_speak("Excellent, everything looks perfect.")
italian_speak("Perfetto. Tutto funziona senza problemi.")  

jarvis_speak("Jarvis, await further instructions.")
italian_speak("Capito. In attesa dei tuoi prossimi comandi.")
