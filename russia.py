import pyttsx3
from gtts import gTTS
import os
import time

# ------------------- English voices -------------------
def jarvis_speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 170)
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()
    engine.stop()

# ------------------- Russian TTS -------------------
def russia_speak(text):
    """Russian"""
    print(f"RU: {text}")
    filename = f"ru_{int(time.time() * 1000)}.mp3"
    tts = gTTS(text=text, lang="ru")
    tts.save(filename)
    os.system(f'start /min "" "{filename}"')
    time.sleep(max(len(text)/15, 3))  # adjust depending on text length
    os.remove(filename)

# ------------------- Russian System Check -------------------
time.sleep(1)
jarvis_speak("Hello Jarvis, can you hear me?")
russia_speak("Да, я вас слышу.")  # Yes, I can hear you

jarvis_speak("What is your status?")
russia_speak("Я работаю в нормальном режиме.")  # I am operating normally

jarvis_speak("Are you ready to start work?")
russia_speak("Да, я полностью готов.")  # Yes, I am fully ready

jarvis_speak("Good, begin the system check.")
russia_speak("Принято. Запускаю проверку системы.")  # Understood, starting system check

jarvis_speak("Checking power systems...")
russia_speak("Проверяю энергетические системы... Все работает нормально.")  # All normal

jarvis_speak("What about the network connection?")
russia_speak("Соединение с сетью стабильно. Интернет доступен.")  # Network stable

jarvis_speak("Run diagnostics on the sensors.")
russia_speak("Запускаю диагностику сенсоров. Камера, микрофон и температурные датчики функционируют корректно.")  

jarvis_speak("How is your memory and storage status?")
russia_speak("Использование памяти — 35%. Дискового пространства достаточно. Состояние оптимальное.")  

jarvis_speak("Excellent. Now check the voice recognition module.")
russia_speak("Тестирую модуль распознавания речи. Скорость ответа в пределах нормы.")  

jarvis_speak("Very good. Are all systems ready for deployment?")
russia_speak("Да, все системы полностью готовы к работе.")  

jarvis_speak("Excellent, everything looks perfect.")
russia_speak("Отлично. Всё работает без сбоев.")  

jarvis_speak("Jarvis, await further instructions.")
russia_speak("Понял. Ожидаю ваших следующих команд.")
