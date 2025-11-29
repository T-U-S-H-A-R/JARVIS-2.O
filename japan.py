import pyttsx3
from gtts import gTTS
import os
import time

# ------------------- Jarvis voice function -------------------
def jarvis_speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 170)
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)  # female/second voice
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()
    engine.stop()

# ------------------- Japanese voice function (gTTS) -------------------
def japan_speak(text):
    print(f"Japanese: {text}")
    filename = f"japan_{int(time.time()*1000)}.mp3"
    tts = gTTS(text=text, lang='ja')  # Japanese language
    tts.save(filename)
    os.system(f'start /min "" "{filename}"')  # plays the audio minimized
    time.sleep(4)  # wait for it to finish
    os.remove(filename)

# ------------------- AUTOMATIC JAPANESE SYSTEM CHECK -------------------
time.sleep(1)
jarvis_speak("Hello Jarvis, can you hear me?")
japan_speak("はい、聞こえます。")  # Yes, I can hear you

jarvis_speak("What is your status?")
japan_speak("私は正常に動作しています。")  # I am operating normally

jarvis_speak("Are you ready to start work?")
japan_speak("はい、準備ができています。")  # Yes, I am ready

jarvis_speak("Good, begin the system check.")
japan_speak("了解しました。システムチェックを開始します。")  # Understood, starting system check

jarvis_speak("Checking power systems...")
japan_speak("電源システムを確認中です。すべて正常です。")  # Checking power systems... all normal

jarvis_speak("What about the network connection?")
japan_speak("ネットワーク接続を確認しました。インターネットは安定しています。")  # Network connection confirmed. Internet is stable

jarvis_speak("Run diagnostics on the sensors.")
japan_speak("センサーの診断を実行中です。カメラ、マイク、温度センサーすべて正常です。")  # Sensor diagnostics

jarvis_speak("How is your memory and storage status?")
japan_speak("メモリ使用率は35％、ストレージ容量は十分です。最適な状態です。")  # Memory and storage status

jarvis_speak("Excellent. Now check the voice recognition module.")
japan_speak("音声認識モジュールをテスト中です。応答速度は問題ありません。")  # Testing voice recognition module

jarvis_speak("Very good. Are all systems ready for deployment?")
japan_speak("はい、すべてのシステムが展開準備完了です。")  # All systems ready

jarvis_speak("Excellent, everything looks perfect.")
japan_speak("完璧です。すべて順調に動作しています。")  # Perfect. Everything fine

jarvis_speak("Jarvis, await further instructions.")
japan_speak("承知しました。次の指示を待機します。")  # Awaiting further instructions
