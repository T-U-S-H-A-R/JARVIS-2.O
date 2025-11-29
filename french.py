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

# ------------------- French TTS -------------------
def french_speak(text):
    """French"""
    print(f"FR: {text}")
    filename = f"fr_{int(time.time() * 1000)}.mp3"
    tts = gTTS(text=text, lang="fr")
    tts.save(filename)
    os.system(f'start /min "" "{filename}"')  # Play minimized
    time.sleep(max(len(text)/15, 3))  # Adjust duration based on text length
    os.remove(filename)

# ------------------- French System Check -------------------
time.sleep(1)
jarvis_speak("Hello Jarvis, can you hear me?")
french_speak("Oui, je vous entends.")  # Yes, I can hear you

jarvis_speak("What is your status?")
french_speak("Je fonctionne normalement.")  # I am operating normally

jarvis_speak("Are you ready to start work?")
french_speak("Oui, je suis prêt.")  # Yes, I am ready

jarvis_speak("Good, begin the system check.")
french_speak("Bien reçu. Lancement de la vérification du système.")  # Understood, starting system check

jarvis_speak("Checking power systems...")
french_speak("Vérification des systèmes d'alimentation... Tout est normal.")  # All normal

jarvis_speak("What about the network connection?")
french_speak("La connexion réseau est stable. Internet est disponible.")  # Network stable

jarvis_speak("Run diagnostics on the sensors.")
french_speak("Exécution du diagnostic des capteurs. Caméra, micro et capteurs de température fonctionnent correctement.")  

jarvis_speak("How is your memory and storage status?")
french_speak("Utilisation de la mémoire à 35 %. Espace de stockage suffisant. État optimal.")  

jarvis_speak("Excellent. Now check the voice recognition module.")
french_speak("Test du module de reconnaissance vocale en cours. La vitesse de réponse est normale.")  

jarvis_speak("Very good. Are all systems ready for deployment?")
french_speak("Oui, tous les systèmes sont entièrement prêts.")  

jarvis_speak("Excellent, everything looks perfect.")
french_speak("Parfait. Tout fonctionne sans problème.")  

jarvis_speak("Jarvis, await further instructions.")
french_speak("Compris. En attente de vos prochaines instructions.")
