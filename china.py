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

# ------------------- Chinese TTS -------------------
def china_speak(text):
    """Chinese"""
    print(f"CN: {text}")
    filename = f"cn_{int(time.time() * 1000)}.mp3"
    tts = gTTS(text=text, lang="zh-CN")
    tts.save(filename)
    os.system(f'start /min "" "{filename}"')
    time.sleep(max(len(text)/15, 3))  # adjust based on text length
    os.remove(filename)

# ------------------- Chinese System Check -------------------
time.sleep(1)
jarvis_speak("Hello Jarvis, can you hear me?")
china_speak("是的，我能听到。")  # Yes, I can hear you

jarvis_speak("What is your status?")
china_speak("我正在正常运行。")  # I am operating normally

jarvis_speak("Are you ready to start work?")
china_speak("是的，我已经准备好了。")  # Yes, I am ready

jarvis_speak("Good, begin the system check.")
china_speak("明白，开始系统检查。")  # Understood, starting system check

jarvis_speak("Checking power systems...")
china_speak("正在检查电源系统……一切正常。")  # All normal

jarvis_speak("What about the network connection?")
china_speak("网络连接稳定，互联网已连接。")  # Network stable

jarvis_speak("Run diagnostics on the sensors.")
china_speak("正在运行传感器诊断。摄像头、麦克风和温度传感器全部正常。")  

jarvis_speak("How is your memory and storage status?")
china_speak("内存使用率为35%，存储空间充足，系统状态最佳。")  

jarvis_speak("Excellent. Now check the voice recognition module.")
china_speak("正在测试语音识别模块。响应速度正常。")  

jarvis_speak("Very good. Are all systems ready for deployment?")
china_speak("是的，所有系统都已准备就绪。")  

jarvis_speak("Excellent, everything looks perfect.")
china_speak("完美，一切运行顺利。")  

jarvis_speak("Jarvis, await further instructions.")
china_speak("好的，正在等待您的下一步指令。")
