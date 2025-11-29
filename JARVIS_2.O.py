||LIBRARY USED||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

#-----------------------------------------------------------------------BATTRY AND RAM-----------------------------------------------------------------------------------------------------#
import psutil
#------------------------------------------------------------------------OPENING CAMERA----------------------------------------------------------------------------------------------------#
import cv2
#--------------------------------------------------------------CONVERT TEXT TO SPEECH(AI)--------------------------------------------------------------------------------------------------#
import pyttsx3
#---------------------------------------------------------------CONVERT SPEECH(HUMAN) TO TEXT(AI)------------------------------------------------------------------------------------------#
import speech_recognition as sr
#------------------------------------------------------------------OPENING WEBISTES--------------------------------------------------------------------------------------------------------#
import webbrowser
#--------------------------------------------------------------------OPERATING SYSTEM------------------------------------------------------------------------------------------------------#
import os
import sys
#-------------------------------------------------------------------USING TIME------------------------------------------------------------------------------------
import time
#-----------------------------------------------------------------------REQUEST FOR ASKING QUESTIONS-------------------------------------------------------------------------
import requests
#-------------------------------------------------------------------GENERATE ANY LANGUAGE-------------------------------------------------------------------------
from gtts import gTTS
#--------------------------------------------------------------SHOW CALENDAR-----------------------------------------------------------------------------------
import calendar
import numpy as np
import pandas as pd
#----------------------------------------------------------------SHOW TIME AND DATE-------------------------------------------------------------------------
from datetime import datetime

import google.generativeai as genai

#---------------------------------------------------------------------SELECT ANY WORD-----------------------------------------------------------------------------------
import random
import matplotlib.pyplot as plt

print("\033[31m ________   _______      ___    ___ ___  ___  ________                 ___  ________  ________  ___      ___ ___  ________          ")
print("\033[31m|\   ___  \|\  ___ \    |\  \  /  /|\  \|\  \|\   ****\               |\  \|\   __  \|\   __  \|\  \    /  /|\  \|\   ****\         ")
print("\033[31m\ \  \\ \  \ \   **/|   \ \  \/  / | \  \\\  \ \  \***|*              \ \  \ \  \|\  \ \  \|\  \ \  \  /  / | \  \ \  \***|*        ")
print("\033[31m \ \  \\ \  \ \  \_|/**  \ \    / / \ \  \\\  \ \_____  \           __ \ \  \ \   __  \ \   _  *\ \  \/  / / \ \  \ \*____  \       ")
print("\033[31m  \ \  \\ \  \ \  \*|\ \  /     \/   \ \  \\\  \|****|\  \         |\  \\*\  \ \  \ \  \ \  \\  \\ \    / /   \ \  \|____|\  \      ")
print("\033[31m   \ \**\\ \**\ \*******\/  /\   \    \ \*******\****\*\  \        \ \********\ \**\ \**\ \**\\ *\\ \**/ /     \ \**\****\_\  \     ")
print("\033[31m    \|**| \|**|\|_______/**/ /\ **\    \|*******|\**_______\        \|********|\|**|\|**|\|**|\|**|\|**|/       \|**|\*________\    \033[0m")
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||NOVA|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||#
API_KEY = ""  # apni Gemini API key
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")
def nova_speak(texts):
    print("AI बोलेगी:", texts)
    filename = f"temp_voice_{int(time.time() * 5000)}.mp3"
    tts = gTTS(text=texts, lang='hi')
    tts.save(filename)
    os.system(f'start /min "" "{filename}"')
    time.sleep(5)
    os.remove(filename)

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||ITALIAN|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||#

def italian_speak(texts):                                       
    print("AI बोलेगी:", texts)
    filename = f"temp_voice_{int(time.time() * 200)}.mp3"
    tts = gTTS(text=texts, lang='it')  # <-- Japanese language
    tts.save(filename)
    os.system(f'start /min "" "{filename}"')
    time.sleep(5)
    os.remove(filename)

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||JAPAN|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||#

def japan_speak(texts):
    print("AI बोलेगी:", texts)
    filename = f"temp_voice_{int(time.time() * 200)}.mp3"
    tts = gTTS(text=texts, lang='ja')  # <-- Japanese language
    tts.save(filename)
    os.system(f'start /min "" "{filename}"')
    time.sleep(5)
    os.remove(filename)

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||RUSSIA|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||#

def russia_speak(texts):
    print("AI बोलेगी:", texts)
    filename = f"temp_voice_{int(time.time() * 200)}.mp3"
    tts = gTTS(text=texts, lang='ru')  # <-- Japanese language
    tts.save(filename)
    os.system(f'start /min "" "{filename}"')
    time.sleep(5)
    os.remove(filename)

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||CHINA|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||#

def china_speak(texts):
    print("AI बोलेगी:", texts)
    filename = f"temp_voice_{int(time.time() * 200)}.mp3"
    tts = gTTS(text=texts, lang='zh-CN')  # <-- Japanese language
    tts.save(filename)
    os.system(f'start /min "" "{filename}"')
    time.sleep(5)
    os.remove(filename)

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||GERMAN|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||#

def german_speak(texts):
    print("AI बोलेगी:", texts)
    filename = f"temp_voice_{int(time.time() * 200)}.mp3"
    tts = gTTS(text=texts, lang='de')  # <-- Japanese language
    tts.save(filename)
    os.system(f'start /min "" "{filename}"')
    time.sleep(5)
    os.remove(filename)

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||FRENCH|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||#

def french_speak(texts):
    print("AI बोलेगी:", texts)
    filename = f"temp_voice_{int(time.time() * 200)}.mp3"
    tts = gTTS(text=texts, lang='fr')  # <-- Japanese language
    tts.save(filename)
    os.system(f'start /min "" "{filename}"')
    time.sleep(5)
    os.remove(filename)

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||FRIDAY|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||#

def friday_speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 170)
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)
    print(text)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||JARVIS|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||#

def jarvis_speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 170)
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)
    print(text)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||FACE DETECETED|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||#
MEMORY={}
#-------------------------------------------------------------------------FACE DETECTION-----------------------------------------------------------------------------------
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)
access_granted = False
while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 0), 2)
        print(random.choice(["\033[31m Access granted \033[0m","\033[32m Access granted \033[0m","\033[33m Access granted \033[0m","\033[34m Access granted \033[0m","\033[35m Access granted \033[0m","\033[36m Access granted \033[0m","\033[37m Access granted \033[0m"]))
        jarvis_speak("Access Granted")
        access_granted = True
        break
    cv2.imshow("Face Detected", frame)
    if access_granted or cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
# -------- IF FACE FOUND → START VOICE ASSISTANT --------
if access_granted:
    recognizer = sr.Recognizer()
    while True:
        try:
            with sr.Microphone() as source:
                print(random.choice(["\033[31mListening\033[0m","\033[32mListening\033[0m","\033[33mListening\033[0m","\033[34mListening\033[0m","\033[35mListening\033[0m","\033[36mListening\033[0m","\033[37mListening\033[0m"]))
                jarvis_speak("Listening.......\n")
                recognizer.adjust_for_ambient_noise(source, duration=0)
                audio = recognizer.listen(source)
            user_text = recognizer.recognize_google(audio)
            print(random.choice(["\033[31m You said:\033[0m","\033[32m You said:\033[0m","\033[33m You said:\033[0m","\033[34m You said:\033[0m","\033[35m You said:\033[0m","\033[36m You said:\033[0m","\033[37m You said:\033[0m"]), user_text)
            MEMORY["COMMAND"]=user_text
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||TRICKS||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||#
            if "tricks" in user_text.lower():
                print(random.choice([ "\033[31mSIR: Please tell me which trick you want — birthday formula or convert, SIR.\033[0m","\033[32mSIR: Kindly specify the trick you want, SIR — birthday formula or convert?\033[32m","\033[33mSIR: Which trick should I use, SIR? Birthday formula or convert?\033[0m","\033[34mSIR: Please choose your trick, SIR — birthday formula or convert.\033[0m","\033[35mSIR: I need to know which trick you want, SIR — birthday formula or convert.\033[0m","\033[36mSIR: Tell me the trick you prefer, SIR — birthday formula or convert?\033[0m","\033[37mSIR: Which trick do you want me to perform, SIR — birthday formula or convert?\033[0m"]))
                jarvis_speak(random.choice(["SIR: Please tell me which trick you want — birthday formula or convert, SIR.","SIR: Kindly specify the trick you want, SIR — birthday formula or convert?","SIR: Which trick should I use, SIR? Birthday formula or convert?","SIR: Please choose your trick, SIR — birthday formula or convert.","SIR: I need to know which trick you want, SIR — birthday formula or convert.","SIR: Tell me the trick you prefer, SIR — birthday formula or convert?","SIR: Which trick do you want me to perform, SIR — birthday formula or convert?"]))
                try:
                    with sr.Microphone() as source: 
                        recognizer.adjust_for_ambient_noise(source, duration=1)
                        audio_trick = recognizer.listen(source)
                        a = recognizer.recognize_google(audio_trick, language='en-IN')
                        MEMORY["TRICKS"]=a
                        if "birthday" in a.lower():
                            try:
                                print(random.choice("\033[31mEnter Birthday date\033[0m","\033[32mEnter Birthday date\033[0m","\033[33mEnter Birthday date\033[0m","\033[34mEnter Birthday date\033[0m","\033[35mEnter Birthday date\033[0m","\033[36mEnter Birthday date\033[0m","\033[37mEnter Birthday date\033[0m"))
                                jarvis_speak(random.choice("Enter Birthday date"))
                                a=int(input(random.choice(["\033[31mEnter birthday date\033[0m","\033[32mEnter birthday date\033[0m","\033[33mEnter birthday date\033[0m","\033[34mEnter birthday date\033[0m","\033[35mEnter birthday date\033[0m","\033[36mEnter birthday date\033[0m","\033[37mEnter birthday date\033[0m"])))
                                b=a*2
                                c=b+5
                                d=c*50
                                print(random.choice(["\033[31mEnter birthday date in terms for number like january 1, february 2 and so on\033[0m","\033[32mEnter birthday date in terms for number like january 1, february 2 and so on\033[0m","\033[33mEnter birthday date in terms for number like january 1, february 2 and so on\033[0m","\033[34mEnter birthday date in terms for number like january 1, february 2 and so on\033[0m","\033[35mEnter birthday date in terms for number like january 1, february 2 and so on\033[0m","\033[36mEnter birthday date in terms for number like january 1, february 2 and so on\033[0m","\033[37mEnter birthday date in terms for number like january 1, february 2 and so on\033[0m","\033[37mEnter birthday date in terms for number like january 1, february 2 and so on\033[0m"]))
                                jarvis_speak("Enter birthday date in terms for number like january 1, february 2 and so on")
                                e=int(input(random.choice(["\033[31mEnter birthday date in terms for number like january 1, february 2 and so on\033[0m","\033[32mEnter birthday date in terms for number like january 1, february 2 and so on\033[0m","\033[33mEnter birthday date in terms for number like january 1, february 2 and so on\033[0m","\033[34mEnter birthday date in terms for number like january 1, february 2 and so on\033[0m","\033[35mEnter birthday date in terms for number like january 1, february 2 and so on\033[0m","\033[36mEnter birthday date in terms for number like january 1, february 2 and so on\033[0m","\033[37mEnter birthday date in terms for number like january 1, february 2 and so on\033[0m"])))
                                f=d+e 
                                jarvis_speak(f"Your NUmber code is {f}")
                            except Exception as e:
                                print(random.choice(["\033[31mTry Again Sir\033[0m","\033[32mTry Again Sir\033[0m","\033[33mTry Again Sir\033[0m","\033[34mTry Again Sir\033[0m","\033[35mTry Again Sir\033[0m","\033[36mTry Again Sir\033[0m","\033[37mTry Again Sir\033[0m"]))
                                jarvis_speak("Try Again Sir")
                        elif "formula" in a.lower():
                            try:
                                print(random.choice(["\033[31mEnter rgb form\033[0m","\033[32mEnter rgb form\033[0m","\033[33mEnter rgb form\033[0m","\033[34mEnter rgb form\033[0m","\033[35mEnter rgb form\033[0m","\033[36mEnter rgb form\033[0m","\033[37mEnter rgb form\033[0m"]))
                                jarvis_speak("Enter rgb form")
                                print(random.choice(["\033[31mEnter red number\033[0m","\033[32mEnter red number\033[0m","\033[33mEnter red number\033[0m","\033[34mEnter red number\033[0m","\033[35mEnter red number\033[0m","\033[36mEnter red number\033[0m","\033[37mEnter red number\033[0m"]))
                                jarvis_speak("Enter red number")
                                red=int(input(random.choice(["\033[31mEnter red\033[0m","\033[32mEnter red\033[0m","\033[33mEnter red\033[0m","\033[34mEnter red\033[0m","\033[35mEnter red\033[0m","\033[36mEnter red\033[0m","\033[37mEnter red\033[0m"])))
                                jarvis_speak("Enter green number")
                                green=int(input(random.choice(["\033[31mEnter green\033[0m","\033[32mEnter green\033[0m","\033[33mEnter green\033[0m","\033[34mEnter green\033[0m","\033[35mEnter green\033[0m","\033[36mEnter green\033[0m","\033[37mEnter green\033[0m"])))
                                print(random.choice(["\033[31mEnter blue number\033[0m","\033[32mEnter blue number\033[0m","\033[33mEnter blue number\033[0m","\033[34mEnter blue number\033[0m","\033[35mEnter blue number\033[0m","\033[36mEnter blue number\033[0m","\033[37mEnter blue number\033[0m"]))
                                jarvis_speak("Enter blue number")
                                blue=int(input(random.choice(["\033[31mEnter blue\033[0m","\033[32mEnter blue\033[0m","\033[33mEnter blue\033[0m","\033[34mEnter blue\033[0m","\033[35mEnter blue\033[0m","\033[36mEnter blue\033[0m","\033[37mEnter blue\033[0m"])))
                                jarvis_speak(f"you have entered red is {red}, green is {green}, blue is {blue}")
                                r=red//51
                                g=green/51
                                b=blue//51
                                formula=16+(36*r)+(6*g)+b
                                jarvis_speak(f"your number code is {formula} from red is {red}, green is {green}, blue is {blue}")
                                jarvis_speak(f"in terms of 0 to 5 r is {r}, g is {g}, b is {b} from red is {red}, green is {green}, blue is {blue}")
                            except Exception as e: 
                                print(f"{e}")
                        elif "convert" in a.lower():
                            try:
                                print(random.choice(["\033[31mEnter number code\033[0m","\033[32mEnter number code\033[0m","\033[33mEnter number code\033[0m","\033[34mEnter number code\033[0m","\033[35mEnter number code\033[0m","\033[36mEnter number code\033[0m","\033[37mEnter number code\033[0m"]))
                                jarvis_speak("Enter number code")
                                i=int(input(random.choice(["\033[31mEnter number code\033[0m","\033[32mEnter number code\033[0m","\033[33mEnter number code\033[0m","\033[34mEnter number code\033[0m","\033[35mEnter number code\033[0m","\033[36mEnter number code\033[0m","\033[37mEnter number code\033[0m"])))
                                jarvis_speak(f"you have entered number code is {i}")
                                nx=i-16
                                r=nx//36
                                g=(nx%36)//6
                                b=nx%6
                                jarvis_speak(f"from {i} we get r is {r}, g is {g}, b is {b} ")
                                jarvis_speak(f"so r g b is {r*51} ,{g*51}, {b*51}")
                            except Exception as e:
                                print(f"{e}")
                        else:
                            print(random.choice([ "\033[31mSIR: Please attempt it again, SIR.\033[0m","\033[32mSIR: That didn't go through, try again, SIR.\033[0m","\033[33mSIR: Kindly repeat the action, SIR.\033[0m","\033[34mSIR: SIR, you may try again now.\033[0m","\033[35mSIR: The process failed, please retry, SIR.\033[0m","\033[36mSIR: Requesting another attempt, SIR.\033[0m","\033[37mSIR: Command not completed, try again, SIR.\033[0m","SIR: Please repeat your input, SIR.","SIR: Go ahead with another try, SIR.","SIR: SIR, please perform that action again.","SIR: Let’s give it one more try, SIR.","SIR: Retry recommended, SIR.","SIR: SIR, that didn’t work — try once more.","SIR: Please input again, SIR.","SIR: Attempt once more for accuracy, SIR."]))
                            jarvis_speak(random.choice([ "SIR: Please attempt it again, SIR.","SIR: That didn't go through, try again, SIR.","SIR: Kindly repeat the action, SIR.","SIR: SIR, you may try again now.","SIR: The process failed, please retry, SIR.","SIR: Requesting another attempt, SIR.","SIR: Command not completed, try again, SIR.","SIR: Please repeat your input, SIR.","SIR: Go ahead with another try, SIR.","SIR: SIR, please perform that action again.","SIR: Let’s give it one more try, SIR."]))                
                except Exception as e:
                    print(random.choice([ "\033[31mSIR: Please attempt it again, SIR.\033[0m","\033[32mSIR: That didn't go through, try again, SIR.\033[0m","\033[33mSIR: Kindly repeat the action, SIR.\033[0m","\033[34mSIR: SIR, you may try again now.\033[0m","\033[35mSIR: The process failed, please retry, SIR.\033[0m","\033[36mSIR: Requesting another attempt, SIR.\033[0m","\033[37mSIR: Command not completed, try again, SIR.\033[0m","SIR: Please repeat your input, SIR.","SIR: Go ahead with another try, SIR.","SIR: SIR, please perform that action again.","SIR: Let’s give it one more try, SIR.","SIR: Retry recommended, SIR.","SIR: SIR, that didn’t work — try once more.","SIR: Please input again, SIR.","SIR: Attempt once more for accuracy, SIR."]))
                    jarvis_speak(random.choice(["SIR: Please attempt it again, SIR.","SIR: That didn't go through, try again, SIR.","SIR: Kindly repeat the action, SIR.","SIR: SIR, you may try again now.","SIR: The process failed, please retry, SIR.","SIR: Requesting another attempt, SIR.","SIR: Command not completed, try again, SIR.","SIR: Please repeat your input, SIR.","SIR: Go ahead with another try, SIR.","SIR: SIR, please perform that action again.","SIR: Let’s give it one more try, SIR.","SIR: Retry recommended, SIR.","SIR: SIR, that didn’t work — try once more.","SIR: Please input again, SIR.","SIR: Attempt once more for accuracy, SIR."]))

            elif "chat" in user_text.lower():
                print(random.choice(["\033[31mHello! I'm Gemini. Speak your prompt. Type 'exit' to quit.\033[0m","\033[32mHello! I'm Gemini. Type your prompt. Type 'exit' to quit.\033[0m","\033[33mHello! I'm Gemini. Type your prompt. Type 'exit' to quit.\033[0m","\033[34mHello! I'm Gemini. Type your prompt. Type 'exit' to quit.\033[0m"]))
                jarvis_speak("Hello! I'm Gemini. Speak your prompt. Type 'exit' to quit.")
                try: 
                    with sr.Microphone() as source: 
                        recognizer.adjust_for_ambient_noise(source, duration=1)
                        audio_city = recognizer.listen(source)
                        city = recognizer.recognize_google(audio_city, language='en-IN')
                        response = model.generate_content(city)
                        if "exit" in city.lower():
                            jarvis_speak("exit Gmeni")
                            break
        # Colored text randomly (red, green, yellow)
                        colors = ["\033[31m", "\033[32m", "\033[33m","\033[34m","\033[35m","\033[36m","\033[37m"]
                        color = random.choice(colors)
                        jarvis_speak(f"{color}Gemini > {response.text}\033[0m")
                except Exception as e:
                    print("Error:", e)

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||WEATHER|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||#            
            elif any(word in user_text.lower() for word in ["mausam","weather"]):
                print(random.choice([ "\033[31mSIR: Please tell me the city name.\033[0m","\033[32mSIR: Kindly provide the city name, SIR.\033[0m","\033[33mSIR: May I have the city name, SIR?\033[0m","\033[34mSIR: Please specify which city, SIR.\033[0m","\033[35mSIR: Requesting the city name, SIR.\033[0m","\033[35mSIR: I need the city name to continue, SIR.\033[0m","\033[36mSIR: Please mention the city you want, SIR.\033[0m","\033[37mSIR: Waiting for the city name, SIR.\033[0m","SIR: Could you provide the city name, SIR?","SIR: Please enter the city name, SIR."]))
                jarvis_speak(random.choice(["SIR: Please tell me the city name.","SIR: Kindly provide the city name, SIR.","SIR: May I have the city name, SIR?","SIR: Please specify which city, SIR.","SIR: Requesting the city name, SIR.","SIR: I need the city name to continue, SIR.","SIR: Please mention the city you want, SIR.","SIR: Waiting for the city name, SIR.","SIR: Could you provide the city name, SIR?","SIR: Please enter the city name, SIR."]))
                try: 
                    with sr.Microphone() as source: 
                        recognizer.adjust_for_ambient_noise(source, duration=1)
                        audio_city = recognizer.listen(source)
                        city = recognizer.recognize_google(audio_city, language='en-IN')
                        MEMORY["WEATHER"]=city
                        print(random.choice(["\033[31m City Recognized \033[0m","\033[32m City Recognized \033[0m","\033[33m City Recognized \033[0m","\033[34m City Recognized \033[0m","\033[35m City Recognized \033[0m","\033[36m City Recognized \033[0m","\033[37m City Recognized \033[0m"]))
                        print("City recognized:", city)
                        url = f"https://wttr.in/{city}?format=j1"
                        response = requests.get(url)
                        if response.status_code == 200:
                            data = response.json()
                            current = data['current_condition'][0]
                            temp = current['temp_C']
                            MEMORY["TEMPERATURE"]=temp
                            desc = current['weatherDesc'][0]['value']
                            MEMORY["DESC"]=desc 
                            humidity = current['humidity']
                            MEMORY["HUMIDITY"]=humidity
                            wind = current['windspeedKmph']
                            MEMORY["WIND"]=wind
                            direction = current['winddir16Point']
                            MEMORY["DIRECTION"]=direction
                            result = (f"SIR: Weather in {city}: Temperature is {temp}°C, Condition is {desc}, " f"Humidity is {humidity}%, Wind is {wind} km/h from {direction}.")
                            jarvis_speak(result) 
                        else:
                            print(random.choice(["[\033[31mSIR: I’m unable to retrieve the weather data at the moment, SIR.\033[0m","\033[32mSIR: Weather information could not be accessed, SIR.\033[0m","\033[33mSIR: I’m having trouble getting the weather update, SIR.\033[0m","\033[34mSIR: The weather details aren’t reachable right now, SIR.\033[0m","\033[35mSIR: I cannot pull the weather report currently, SIR.\033[0m","\033[36mSIR: Unable to load the weather status at this time, SIR.\033[0m","\033[37mSIR: Weather service is not responding, SIR.\033[0m","SIR: I’m failing to fetch the weather data, SIR.","SIR: The weather information is unavailable right now, SIR.","SIR: I’m unable to access weather updates at present, SIR."]))
                            jarvis_speak(random.choice(["SIR: I’m unable to retrieve the weather data at the moment, SIR.","SIR: Weather information could not be accessed, SIR.","SIR: I’m having trouble getting the weather update, SIR.","SIR: The weather details aren’t reachable right now, SIR.","SIR: I cannot pull the weather report currently, SIR.","SIR: Unable to load the weather status at this time, SIR.","SIR: Weather service is not responding, SIR."]))
                except Exception as e:
                    print(f"Error fetching weather: {e}")
                    print(random.choice(["\033[31mSIR: There was a problem retrieving weather information, SIR.\033[0m","\033[32mSIR: I encountered an issue while fetching the weather data, SIR.\033[0m","\033[33mSIR: Weather information retrieval failed, SIR.\033[0m","\033[34mSIR: I'm unable to access the weather details right now, SIR.\033[0m","\033[35mSIR: There was an error fetching the weather update, SIR.\033[0m","\033[36mSIR: I couldn't retrieve the weather report, SIR.\033[0m","\033[37mSIR: Weather data is currently unreachable, SIR.\033[0m","SIR: I'm experiencing difficulty getting the weather info, SIR.","SIR: The weather service isn't responding at the moment, SIR.","SIR: Unable to obtain the weather information at this time, SIR."]))
                    jarvis_speak(random.choice(["SIR: There was a problem retrieving weather information, SIR.","SIR: I encountered an issue while fetching the weather data, SIR.","SIR: Weather information retrieval failed, SIR.","SIR: I'm unable to access the weather details right now, SIR.","SIR: There was an error fetching the weather update, SIR.","SIR: I couldn't retrieve the weather report, SIR.","SIR: Weather data is currently unreachable, SIR.","SIR: I'm experiencing difficulty getting the weather info, SIR.","SIR: The weather service isn't responding at the moment, SIR.","SIR: Unable to obtain the weather information at this time, SIR."]))
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||TALKING|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||#
            elif "talking" in user_text.lower():
                print(random.choice(["\033[31mSIR: Please tell me which conversation you want — German, Japanese, Chinese, Italian, French, or Russian, SIR.\033[0m","\033[32mSIR: Kindly specify the conversation language — German, Japanese, Chinese, Italian, French, or Russian, SIR.\033[0m","\033[33mSIR: Which conversation language should I use, SIR? German, Japanese, Chinese, Italian, French, or Russian?\033[0m","\033[34mSIR: Please choose a language for the conversation — German, Japanese, Chinese, Italian, French, or Russian, SIR.\033[0m","\033[35mSIR: I need the language preference, SIR — German, Japanese, Chinese, Italian, French, or Russian.\033[0m","\033[36mSIR: Tell me your desired language for the conversation, SIR — German, Japanese, Chinese, Italian, French, or Russian.\033[0m","\033[37mSIR: Which language would you like to continue in, SIR? German, Japanese, Chinese, Italian, French, or Russian?\033[0m"]))
                jarvis_speak(random.choice(["SIR: Please tell me which conversation you want — German, Japanese, Chinese, Italian, French, or Russian, SIR.","SIR: Kindly specify the conversation language — German, Japanese, Chinese, Italian, French, or Russian, SIR.","SIR: Which conversation language should I use, SIR? German, Japanese, Chinese, Italian, French, or Russian?","SIR: Please choose a language for the conversation — German, Japanese, Chinese, Italian, French, or Russian, SIR.","SIR: I need the language preference, SIR — German, Japanese, Chinese, Italian, French, or Russian.","SIR: Tell me your desired language for the conversation, SIR — German, Japanese, Chinese, Italian, French, or Russian.","SIR: Which language would you like to continue in, SIR? German, Japanese, Chinese, Italian, French, or Russian?","SIR: Please select the language for our conversation — German, Japanese, Chinese, Italian, French, or Russian, SIR.","SIR: Let me know the conversation language, SIR — German, Japanese, Chinese, Italian, French, or Russian.","SIR: SIR, choose a language for the conversation — German, Japanese, Chinese, Italian, French, or Russian."]))
                try: 
                    with sr.Microphone() as source: 
                        recognizer.adjust_for_ambient_noise(source, duration=1)
                        audio_talking = recognizer.listen(source)
                        b = recognizer.recognize_google(audio_talking, language='en-IN')
                        MEMORY["TALKING"]=b
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||GERMAN||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
                        if "german" in b.lower():
                            print(random.choice(["\033[31mHello Jarvis, can you hear me?\033[0m","\033[32mHello Jarvis, can you hear me?\033[0m","\033[33mHello Jarvis, can you hear me?\033[0m","\033[34mHello Jarvis, can you hear me?\033[0m","\033[35mHello Jarvis, can you hear me?\033[0m","\033[36mHello Jarvis, can you hear me?\033[0m","\033[37mHello Jarvis, can you hear me?\033[0m"]))
                            jarvis_speak("Hello Jarvis, can you hear me?")
                            print(random.choice(["\033[31mJa, ich höre Sie.\033[0m","\033[32mJa, ich höre Sie.\033[0m","\033[33mJa, ich höre Sie.\033[0m","\033[34mJa, ich höre Sie.\033[0m","\033[35mJa, ich höre Sie.\033[0m","\033[36mJa, ich höre Sie.\033[0m","\033[37mJa, ich höre Sie.\033[0m"]))
                            german_speak("Ja, ich höre Sie.")
                            print(random.choice(["\033[31mWhat is your status?\033[0m","\033[32mWhat is your status?\033[0m","\033[33mWhat is your status?\033[0m","\033[34mWhat is your status?\033[0m","\033[35mWhat is your status?\033[0m","\033[36mWhat is your status?\033[0m","\033[37mWhat is your status?\033[0m"]))
                            jarvis_speak("What is your status?")
                            print(random.choice(["\033[31mIch arbeite im normalen Betriebsmodus.\033[0m","\033[32mIch arbeite im normalen Betriebsmodus.\033[0m","\033[33mIch arbeite im normalen Betriebsmodus.\033[0m","\033[34mIch arbeite im normalen Betriebsmodus.\033[0m","\033[35mIch arbeite im normalen Betriebsmodus.\033[0m","\033[36mIch arbeite im normalen Betriebsmodus.\033[0m","\033[37mIch arbeite im normalen Betriebsmodus.\033[0m"]))
                            german_speak("Ich arbeite im normalen Betriebsmodus.")
                            print(random.choice(["\033[31mAre you ready to start work?\033[0m","\033[32mAre you ready to start work?\033[0m","\033[33mAre you ready to start work?\033[0m","\033[34mAre you ready to start work?\033[0m","\033[35mAre you ready to start work?\033[0m","\033[36mAre you ready to start work?\033[0m","\033[37mAre you ready to start work?\033[0m"]))
                            jarvis_speak("Are you ready to start work?")
                            print(random.choice(["\033[31mJa, ich bin vollständig bereit.\033[0m","\033[32mJa, ich bin vollständig bereit.\033[0m","\033[33mJa, ich bin vollständig bereit.\033[0m","\033[34mJa, ich bin vollständig bereit.\033[0m","\033[35mJa, ich bin vollständig bereit.\033[0m","\033[36mJa, ich bin vollständig bereit.\033[0m","\033[37mJa, ich bin vollständig bereit.\033[0m"]))
                            german_speak("Ja, ich bin vollständig bereit.")
                            print(random.choice(["\033[31mGood, begin the system check.\033[0m","\033[32mGood, begin the system check.\033[0m","\033[33mGood, begin the system check.\033[0m","\033[34mGood, begin the system check.\033[0m","\033[35mGood, begin the system check.\033[0m","\033[36mGood, begin the system check.\033[0m","\033[37mGood, begin the system check.\033[0m"]))
                            jarvis_speak("Good, begin the system check.")
                            print(random.choice(["\033[31mVerstanden. Starte die Systemüberprüfung.\033[0m","\033[32mVerstanden. Starte die Systemüberprüfung.\033[0m","\033[33mVerstanden. Starte die Systemüberprüfung.\033[0m","\033[34mVerstanden. Starte die Systemüberprüfung.\033[0m","\033[35mVerstanden. Starte die Systemüberprüfung.\033[0m","\033[36mVerstanden. Starte die Systemüberprüfung.\033[0m","\033[37mVerstanden. Starte die Systemüberprüfung.\033[0m"]))
                            german_speak("Verstanden. Starte die Systemüberprüfung.")
                            print(random.choice(["\033[31mChecking power systems...\033[0m","\033[32mChecking power systems...\033[0m","\033[33mChecking power systems...\033[0m","\033[34mChecking power systems...\033[0m","\033[35mChecking power systems...\033[0m","\033[36mChecking power systems...\033[0m","\033[37mChecking power systems...\033[0m"]))
                            jarvis_speak("Checking power systems...")
                            print(random.choice(["\033[31mÜberprüfe die Energiesysteme... Alles funktioniert einwandfrei.\033[0m","\033[32mÜberprüfe die Energiesysteme... Alles funktioniert einwandfrei.\033[0m","\033[33mÜberprüfe die Energiesysteme... Alles funktioniert einwandfrei.\033[0m","\033[34mÜberprüfe die Energiesysteme... Alles funktioniert einwandfrei.\033[0m","\033[35mÜberprüfe die Energiesysteme... Alles funktioniert einwandfrei.\033[0m","\033[36mÜberprüfe die Energiesysteme... Alles funktioniert einwandfrei.\033[0m","\033[37mÜberprüfe die Energiesysteme... Alles funktioniert einwandfrei.\033[0m"]))
                            german_speak("Überprüfe die Energiesysteme... Alles funktioniert einwandfrei.")
                        elif "japan" in b.lower():
                            print(random.choice(["\033[31mHello Jarvis, can you hear me?\033[0m","\033[32mHello Jarvis, can you hear me?\033[0m","\033[33mHello Jarvis, can you hear me?\033[0m","\033[34mHello Jarvis, can you hear me?\033[0m","\033[35mHello Jarvis, can you hear me?\033[0m","\033[36mHello Jarvis, can you hear me?\033[0m","\033[37mHello Jarvis, can you hear me?\033[0m"]))
                            jarvis_speak("Hello Jarvis, can you hear me?")
                            print(random.choice(["\033[31mはい、聞こえます。\033[0m","\033[32mはい、聞こえます。\033[0m","\033[33mはい、聞こえます。\033[0m","\033[34mはい、聞こえます。\033[0m","\033[35mはい、聞こえます。\033[0m","\033[36mはい、聞こえます。\033[0m","\033[37mはい、聞こえます。\033[0m"]))
                            japan_speak("はい、聞こえます。")
                # Yes, I can hear you
                            print(random.choice(["\033[31mWhat is your status?\033[0m","\033[32mWhat is your status?\033[0m","\033[33mWhat is your status?\033[0m","\033[34mWhat is your status?\033[0m","\033[35mWhat is your status?\033[0m","\033[36mWhat is your status?\033[0m","\033[37mWhat is your status?\033[0m"]))
                            jarvis_speak("What is your status?")
                            print(random.choice(["\033[31m私は正常に動作しています。\033[0m","\033[32m私は正常に動作しています。\033[0m","\033[33m私は正常に動作しています。\033[0m","\033[34m私は正常に動作しています。\033[0m","\033[35m私は正常に動作しています。\033[0m","\033[36m私は正常に動作しています。\033[0m","\033[37m私は正常に動作しています。\033[0m"]))
                            japan_speak("私は正常に動作しています。")
                # I am operating normally
                            print(random.choice(["\033[31mAre you ready to start work?\033[0m","\033[32mAre you ready to start work?\033[0m","\033[33mAre you ready to start work?\033[0m","\033[34mAre you ready to start work?\033[0m","\033[35mAre you ready to start work?\033[0m","\033[36mAre you ready to start work?\033[0m","\033[37mAre you ready to start work?\033[0m"]))
                            jarvis_speak("Are you ready to start work?")
                            print(random.choice(["\033[31mはい、準備ができています。\033[0m","\033[32mはい、準備ができています。\033[0m","\033[33mはい、準備ができています。\033[0m","\033[34mはい、準備ができています。\033[0m","\033[35mはい、準備ができています。\033[0m""\033[36mはい、準備ができています。\033[0m","\033[37mはい、準備ができています。\033[0m"]))
                            japan_speak("はい、準備ができています。")
                # Yes, I am ready
                            print(random.choice(["\033[31mGood, begin the system check.\033[0m","\033[32mGood, begin the system check.\033[0m","\033[33mGood, begin the system check.\033[0m","\033[34mGood, begin the system check.\033[0m","\033[35mGood, begin the system check.\033[0m","\033[36mGood, begin the system check.\033[0m","\033[37mGood, begin the system check.\033[0m"]))
                            jarvis_speak("Good, begin the system check.")
                            print(random.choice(["\033[31m了解しました。システムチェックを開始します。\033[0m","\033[32m了解しました。システムチェックを開始します。\033[0m","\033[33m了解しました。システムチェックを開始します。\033[0m","\033[34m了解しました。システムチェックを開始します。\033[0m","\033[35m了解しました。システムチェックを開始します。\033[0m","\033[36m了解しました。システムチェックを開始します。\033[0m"]))
                            japan_speak("了解しました。システムチェックを開始します。")
                # Understood, starting system check
                            print(random.choice(["\033[31mChecking power systems...\033[0m","\033[32mChecking power systems...\033[0m","\033[33mChecking power systems...\033[0m","\033[34mChecking power systems...\033[0m","\033[35mChecking power systems...\033[0m","\033[36mChecking power systems...\033[0m","\033[37mChecking power systems...\033[0m"]))
                            jarvis_speak("Checking power systems...")
                            print(random.choice(["\033[31m電源システムを確認中です。すべて正常です。\033[0m","\033[32m電源システムを確認中です。すべて正常です。\033[0m","\033[33m電源システムを確認中です。すべて正常です。\033[0m","\033[34m電源システムを確認中です。すべて正常です。\033[0m","\033[35m電源システムを確認中です。すべて正常です。\033[0m","\033[36m電源システムを確認中です。すべて正常です。\033[0m","\033[37m電源システムを確認中です。すべて正常です。\033[0m"]))
                            japan_speak("電源システムを確認中です。すべて正常です。")
                # Understood. Awaiting your next command.
                        elif "russia" in b.lower():
                            print(random.choice(["\033[31mHello Jarvis, can you hear me?\033[0m","\033[32mHello Jarvis, can you hear me?\033[0m","\033[33mHello Jarvis, can you hear me?\033[0m","\033[34mHello Jarvis, can you hear me?\033[0m","\033[35mHello Jarvis, can you hear me?\033[0m","\033[36mHello Jarvis, can you hear me?\033[0m","\033[37mHello Jarvis, can you hear me?\033[0m"]))
                            jarvis_speak("Hello Jarvis, can you hear me?")
                            print(random.choice(["\033[31mДа, я вас слышу.\033[0m","\033[32mДа, я вас слышу.\033[0m","\033[33mДа, я вас слышу.\033[0m","\033[34mДа, я вас слышу.\033[0m","\033[35mДа, я вас слышу.\033[0m","\033[36mДа, я вас слышу.\033[0m","\033[37mДа, я вас слышу.\033[0m"]))
                            russia_speak("Да, я вас слышу.")
                # Yes, I can hear you
                            print(random.choice(["\033[31mWhat is your status?\033[0m","\033[32mWhat is your status?\033[0m","\033[33mWhat is your status?\033[0m","\033[34mWhat is your status?\033[0m","\033[35mWhat is your status?\033[0m","\033[36mWhat is your status?\033[0m","\033[37mWhat is your status?\033[0m"]))
                            jarvis_speak("What is your status?")
                            print(random.choice(["\033[31mЯ работаю в нормальном режиме.\033[0m","\033[32mЯ работаю в нормальном режиме.\033[0m","\033[33mЯ работаю в нормальном режиме.\033[0m","\033[34mЯ работаю в нормальном режиме.\033[0m","\033[35mЯ работаю в нормальном режиме.\033[0m","\033[36mЯ работаю в нормальном режиме.\033[0m","\033[37mЯ работаю в нормальном режиме.\033[0m"]))
                            russia_speak("Я работаю в нормальном режиме.")
                # I am operating normally
                            print(random.choice(["\033[31mAre you ready to start work?\033[0m","\033[32mAre you ready to start work?\033[0m","\033[33mAre you ready to start work?\033[0m","\033[34mAre you ready to start work?\033[0m","\033[35mAre you ready to start work?\033[0m","\033[36mAre you ready to start work?\033[0m","\033[37mAre you ready to start work?\033[0m"]))
                            jarvis_speak("Are you ready to start work?")
                            print(random.choice(["\033[31mДа, я полностью готов.\033[0m","\033[32mДа, я полностью готов.\033[0m","\033[33mДа, я полностью готов.\033[0m","\033[34mДа, я полностью готов.\033[0m","\033[35mДа, я полностью готов.\033[0m","\033[36mДа, я полностью готов.\033[0m","\033[37mДа, я полностью готов.\033[0m"]))
                            russia_speak("Да, я полностью готов.")
                # Yes, I am fully ready
                            print(random.choice(["\033[31mGood, begin the system check.\033[0m","\033[32mGood, begin the system check.\033[0m","\033[33mGood, begin the system check.\033[0m","\033[34mGood, begin the system check.\033[0m","\033[35mGood, begin the system check.\033[0m","\033[36mGood, begin the system check.\033[0m","\033[37mGood, begin the system check.\033[0m"]))
                            jarvis_speak("Good, begin the system check.")
                            print(random.choice(["\033[31mПринято. Запускаю проверку системы.\033[0m","\033[32mПринято. Запускаю проверку системы.\033[0m","\033[33mПринято. Запускаю проверку системы.\033[0m","\033[34mПринято. Запускаю проверку системы.\033[0m","\033[35mПринято. Запускаю проверку системы.\033[0m","\033[36mПринято. Запускаю проверку системы.\033[0m","\033[37mПринято. Запускаю проверку системы.\033[0m"]))
                            russia_speak("Принято. Запускаю проверку системы.")
                # Understood, starting system check
                            print(random.choice(["\033[31mChecking power systems...\033[0m","\033[32mChecking power systems...\033[0m","\033[33mChecking power systems...\033[0m","\033[34mChecking power systems...\033[0m","\033[35mChecking power systems...\033[0m","\033[36mChecking power systems...\033[0m","\033[37mChecking power systems...\033[0m"]))
                            jarvis_speak("Checking power systems...")
                            print(random.choice(["\033[31mПроверяю энергетические системы... Все работает нормально.\033[0m","\033[32mПроверяю энергетические системы... Все работает нормально.\033[0m","\033[33mПроверяю энергетические системы... Все работает нормально.\033[0m","\033[34mПроверяю энергетические системы... Все работает нормально.\033[0m","\033[35mПроверяю энергетические системы... Все работает нормально.\033[0m","\033[36mПроверяю энергетические системы... Все работает нормально.\033[0m","\033[37mПроверяю энергетические системы... Все работает нормально.\033[0m"]))
                            russia_speak("Проверяю энергетические системы... Все работает нормально.")
                # Checking power systems... All normal
                        elif "china" in b.lower():
                            print(random.choice(["\033[31mHello Jarvis, can you hear me?\033[0m","\033[32mHello Jarvis, can you hear me?\033[0m","\033[33mHello Jarvis, can you hear me?\033[0m","\033[34mHello Jarvis, can you hear me?\033[0m","\033[35mHello Jarvis, can you hear me?\033[0m","\033[36mHello Jarvis, can you hear me?\033[0m","\033[37mHello Jarvis, can you hear me?\033[0m"]))
                            jarvis_speak("Hello Jarvis, can you hear me?")
                            print(random.choice(["\033[31m是的，我能听到。\033[0m","\033[32m是的，我能听到。\033[0m","\033[33m是的，我能听到。\033[0m","\033[34m是的，我能听到。\033[0m","\033[35m是的，我能听到。\033[0m","\033[36m是的，我能听到。\033[0m","\033[37m是的，我能听到。\033[0m"]))
                            china_speak("是的，我能听到。")
                # Yes, I can hear you
                            print(random.choice(["\033[31mWhat is your status?\033[0m","\033[32mWhat is your status?\033[0m","\033[33mWhat is your status?\033[0m","\033[34mWhat is your status?\033[0m","\033[35mWhat is your status?\033[0m","\033[36mWhat is your status?\033[0m","\033[37mWhat is your status?\033[0m"]))
                            jarvis_speak("What is your status?")
                            print(random.choice(["\033[31m我正在正常运行。\033[0m","\033[32m我正在正常运行。\033[0m","\033[33m我正在正常运行。\033[0m","\033[34m我正在正常运行。\033[0m","\033[35m我正在正常运行。\033[0m","\033[36m我正在正常运行。\033[0m","\033[37m我正在正常运行。\033[0m"]))
                            china_speak("我正在正常运行。")
                # I am operating normally
                            print(random.choice(["\033[31mAre you ready to start work?\033[0m","\033[32mAre you ready to start work?\033[0m","\033[33mAre you ready to start work?\033[0m","\033[34mAre you ready to start work?\033[0m","\033[35mAre you ready to start work?\033[0m","\033[36mAre you ready to start work?\033[0m","\033[37mAre you ready to start work?\033[0m"]))
                            jarvis_speak("Are you ready to start work?")
                            print(random.choice(["\033[31m是的，我已经准备好了。\033[0m","\033[32m是的，我已经准备好了。\033[0m","\033[33m是的，我已经准备好了。\033[0m","\033[34m是的，我已经准备好了。\033[0m","\033[35m是的，我已经准备好了。\033[0m","\033[36m是的，我已经准备好了。\033[0m","\033[37m是的，我已经准备好了。\033[0m"]))
                            china_speak("是的，我已经准备好了。")
                # Yes, I am ready
                            print(random.choice(["\033[31mGood, begin the system check.\033[0m","\033[32mGood, begin the system check.\033[0m","\033[33mGood, begin the system check.\033[0m","\033[34mGood, begin the system check.\033[0m","\033[35mGood, begin the system check.\033[0m","\033[36mGood, begin the system check.\033[0m","\033[37mGood, begin the system check.\033[0m"]))
                            jarvis_speak("Good, begin the system check.")
                            print(random.choice(["\033[31m明白，开始系统检查。\033[0m","\033[32m明白，开始系统检查。\033[0m","\033[33m明白，开始系统检查。\033[0m","\033[34m明白，开始系统检查。\033[0m","\033[35m明白，开始系统检查。\033[0m","\033[36m明白，开始系统检查。\033[0m","\033[37m明白，开始系统检查。\033[0m"]))
                            china_speak("明白，开始系统检查。")
                # Understood, starting system check
                            print(random.choice(["\033[31mChecking power systems...\033[0m","\033[32mChecking power systems...\033[0m","\033[33mChecking power systems...\033[0m","\033[34mChecking power systems...\033[0m","\033[35mChecking power systems...\033[0m","\033[36mChecking power systems...\033[0m","\033[37mChecking power systems...\033[0m"]))
                            jarvis_speak("Checking power systems...")
                            print(random.choice(["\033[31m正在检查电源系统……一切正常。\033[0m","\033[32m正在检查电源系统……一切正常。\033[0m","\033[33m正在检查电源系统……一切正常。\033[0m","\033[34m正在检查电源系统……一切正常。\033[0m","\033[35m正在检查电源系统……一切正常。\033[0m","\033[36m正在检查电源系统……一切正常。\033[0m","\033[37m正在检查电源系统……一切正常。\033[0m"]))
                            china_speak("正在检查电源系统……一切正常。")
                # Checking power systems... All normal
                # Okay, awaiting your next command

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||ITALIAN|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\#
                        elif "italian" in b.lower():
                            print(random.choice(["\033[31mHello Jarvis, can you hear me?\033[0m","\033[32mHello Jarvis, can you hear me?\033[0m","\033[33mHello Jarvis, can you hear me?\033[0m","\033[34mHello Jarvis, can you hear me?\033[0m","\033[35mHello Jarvis, can you hear me?\033[0m","\033[36mHello Jarvis, can you hear me?\033[0m","\033[37mHello Jarvis, can you hear me?\033[0m"]))
                            jarvis_speak("Hello Jarvis, can you hear me?")
                            print(random.choice(["\033[31mSì, ti sento.\033[0m","\033[32mSì, ti sento.\033[0m","\033[33mSì, ti sento.\033[0m","\033[34mSì, ti sento.\033[0m","\033[35mSì, ti sento.\033[0m","\033[36mSì, ti sento.\033[0m","\033[37mSì, ti sento.\033[0m"]))
                            italian_speak("Sì, ti sento.")
                # Yes, I can hear you
                            print(random.choice(["\033[31mWhat is your status?\033[0m","\033[32mWhat is your status?\033[0m","\033[33mWhat is your status?\033[0m","\033[34mWhat is your status?\033[0m","\033[35mWhat is your status?\033[0m","\033[36mWhat is your status?\033[0m","\033[37mWhat is your status?\033[0m"]))
                            jarvis_speak("What is your status?")
                            print(random.choice(["\033[31mSto funzionando normalmente.\033[0m","\033[32mSto funzionando normalmente.\033[0m","\033[33mSto funzionando normalmente.\033[0m","\033[34mSto funzionando normalmente.\033[0m","\033[35mSto funzionando normalmente.\033[0m","\033[36mSto funzionando normalmente.\033[0m","\033[37mSto funzionando normalmente.\033[0m"]))
                            italian_speak("Sto funzionando normalmente.")
                # I am operating normally
                            print(random.choice(["\033[31mAre you ready to start work?\033[0m","\033[32mAre you ready to start work?\033[0m","\033[33mAre you ready to start work?\033[0m","\033[34mAre you ready to start work?\033[0m","\033[35mAre you ready to start work?\033[0m","\033[36mAre you ready to start work?\033[0m","\033[37mAre you ready to start work?\033[0m"]))
                            jarvis_speak("Are you ready to start work?")
                            print(random.choice(["\033[31mSì, sono pronto.\033[0m","\033[32mSì, sono pronto.\033[0m","\033[33mSì, sono pronto.\033[0m","\033[34mSì, sono pronto.\033[0m","\033[35mSì, sono pronto.\033[0m","\033[36mSì, sono pronto.\033[0m","\033[37mSì, sono pronto.\033[0m"]))
                            italian_speak("Sì, sono pronto.")
                # Yes, I am ready
                            print(random.choice(["\033[31mGood, begin the system check.\033[0m","\033[32mGood, begin the system check.\033[0m","\033[33mGood, begin the system check.\033[0m","\033[34mGood, begin the system check.\033[0m","\033[35mGood, begin the system check.\033[0m","\033[36mGood, begin the system check.\033[0m","\033[37mGood, begin the system check.\033[0m"]))
                            jarvis_speak("Good, begin the system check.")
                            print(random.choice(["\033[31mRicevuto. Avvio il controllo del sistema.\033[0m","\033[32mRicevuto. Avvio il controllo del sistema.\033[0m","\033[33mRicevuto. Avvio il controllo del sistema.\033[0m","\033[34mRicevuto. Avvio il controllo del sistema.\033[0m","\033[35mRicevuto. Avvio il controllo del sistema.\033[0m","\033[36mRicevuto. Avvio il controllo del sistema.\033[0m","\033[37mRicevuto. Avvio il controllo del sistema.\033[0m"]))
                            italian_speak("Ricevuto. Avvio il controllo del sistema.")
                # Understood, starting system check
                            print(random.choice(["\033[31mChecking power systems...\033[0m","\033[32mChecking power systems...\033[0m","\033[33mChecking power systems...\033[0m","\033[34mChecking power systems...\033[0m","\033[35mChecking power systems...\033[0m","\033[36mChecking power systems...\033[0m","\033[37mChecking power systems...\033[0m"]))
                            jarvis_speak("Checking power systems...")
                            print(random.choice(["\033[31mSto controllando i sistemi di alimentazione... Tutto è normale.\033[0m","\033[32mSto controllando i sistemi di alimentazione... Tutto è normale.\033[0m","\033[33mSto controllando i sistemi di alimentazione... Tutto è normale.\033[0m","\033[34mSto controllando i sistemi di alimentazione... Tutto è normale.\033[0m","\033[35mSto controllando i sistemi di alimentazione... Tutto è normale.\033[0m","\033[36mSto controllando i sistemi di alimentazione... Tutto è normale.\033[0m","\033[37mSto controllando i sistemi di alimentazione... Tutto è normale.\033[0m"]))
                            italian_speak("Sto controllando i sistemi di alimentazione... Tutto è normale.")
                # Checking power systems... Everything is normal
                # Understood. Awaiting your next commands
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||FRENCH|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\|#

                        elif "french" in b.lower():
                            print(random.choice(["\033[31mHello Jarvis, can you hear me?\033[0m","\033[32mHello Jarvis, can you hear me?\033[0m","\033[33mHello Jarvis, can you hear me?\033[0m","\033[34mHello Jarvis, can you hear me?\033[0m","\033[35mHello Jarvis, can you hear me?\033[0m","\033[36mHello Jarvis, can you hear me?\033[0m","\033[37mHello Jarvis, can you hear me?\033[0m"]))
                            jarvis_speak("Hello Jarvis, can you hear me?")
                            print(random.choice(["\033[31mOui, je vous entends.\033[0m","\033[32mOui, je vous entends.\033[0m","\033[33mOui, je vous entends.\033[0m","\033[34mOui, je vous entends.\033[0m","\033[35mOui, je vous entends.\033[0m","\033[36mOui, je vous entends.\033[0m","\033[37mOui, je vous entends.\033[0m"]))
                            french_speak("Oui, je vous entends.")
                # Yes, I can hear you
                            print(random.choice(["\033[31mWhat is your status?\033[0m","\033[32mWhat is your status?\033[0m","\033[33mWhat is your status?\033[0m","\033[34mWhat is your status?\033[0m","\033[35mWhat is your status?\033[0m","\033[36mWhat is your status?\033[0m","\033[37mWhat is your status?\033[0m"]))
                            jarvis_speak("What is your status?")
                            print(random.choice(["\033[31mJe fonctionne normalement.\033[0m","\033[32mJe fonctionne normalement.\033[0m","\033[33mJe fonctionne normalement.\033[0m","\033[34mJe fonctionne normalement.\033[0m","\033[35mJe fonctionne normalement.\033[0m","\033[36mJe fonctionne normalement.\033[0m","\033[37mJe fonctionne normalement.\033[0m"]))
                            french_speak("Je fonctionne normalement.")
                # I am operating normally
                            print(random.choice(["\033[31mAre you ready to start work?\033[0m","\033[32mAre you ready to start work?\033[0m","\033[33mAre you ready to start work?\033[0m","\033[34mAre you ready to start work?\033[0m","\033[35mAre you ready to start work?\033[0m","\033[36mAre you ready to start work?\033[0m","\033[37mAre you ready to start work?\033[0m"]))
                            jarvis_speak("Are you ready to start work?")
                            print(random.choice(["\033[31mOui, je suis prêt.\033[0m","\033[32mOui, je suis prêt.\033[0m","\033[33mOui, je suis prêt.\033[0m","\033[34mOui, je suis prêt.\033[0m","\033[35mOui, je suis prêt.\033[0m","\033[36mOui, je suis prêt.\033[0m","\033[37mOui, je suis prêt.\033[0m"]))
                            french_speak("Oui, je suis prêt.")
                # Yes, I am ready
                            print(random.choice(["\033[31mGood, begin the system check.\033[0m","\033[32mGood, begin the system check.\033[0m","\033[33mGood, begin the system check.\033[0m","\033[34mGood, begin the system check.\033[0m","\033[35mGood, begin the system check.\033[0m","\033[36mGood, begin the system check.\033[0m","\033[37mGood, begin the system check.\033[0m"]))
                            jarvis_speak("Good, begin the system check.")
                            print(random.choice(["\033[31mBien reçu. Lancement de la vérification du système.\033[0m","\033[32mBien reçu. Lancement de la vérification du système.\033[0m","\033[33mBien reçu. Lancement de la vérification du système.\033[0m","\033[34mBien reçu. Lancement de la vérification du système.\033[0m","\033[35mBien reçu. Lancement de la vérification du système.\033[0m","\033[36mBien reçu. Lancement de la vérification du système.\033[0m","\033[37mBien reçu. Lancement de la vérification du système.\033[0m"]))
                            french_speak("Bien reçu. Lancement de la vérification du système.")
                # Understood, starting system check
                            print(random.choice(["\033[31mChecking power systems...\033[0m","\033[32mChecking power systems...\033[0m","\033[33mChecking power systems...\033[0m","\033[34mChecking power systems...\033[0m","\033[35mChecking power systems...\033[0m","\033[36mChecking power systems...\033[0m","\033[37mChecking power systems...\033[0m"]))
                            jarvis_speak("Checking power systems...")
                            print(random.choice(["\033[31mVérification des systèmes d'alimentation... Tout est normal.\033[0m","\033[32mVérification des systèmes d'alimentation... Tout est normal.\033[0m","\033[33mVérification des systèmes d'alimentation... Tout est normal.\033[0m","\033[34mVérification des systèmes d'alimentation... Tout est normal.\033[0m","\033[35mVérification des systèmes d'alimentation... Tout est normal.\033[0m","\033[36mVérification des systèmes d'alimentation... Tout est normal.\033[0m","\033[37mVérification des systèmes d'alimentation... Tout est normal.\033[0m"]))
                            french_speak("Vérification des systèmes d'alimentation... Tout est normal.") 
                #---------------------------------------------------Checking power systems... Everything is normal----------------------------------------------------------
                        else:
                            print(random.choice([ "\033[31mSIR: No language found, SIR.\033[0m","\033[32mSIR: I couldn't detect any language, SIR.\033[0m","\033[33mSIR: No valid language was recognized, SIR.\033[0m","\033[34mSIR: SIR, there is no language available.\033[0m","\033[35mSIR: No matching language detected, SIR.\033[0m","\033[36mSIR: I did not find any language option, SIR.\033[0m","\033[37mSIR: The language you mentioned doesn't exist, SIR.\033[0m"]))
                            jarvis_speak(random.choice(["SIR: Please attempt it again, SIR.","SIR: That didn't go through, try again, SIR.","SIR: Kindly repeat the action, SIR.","SIR: SIR, you may try again now.","SIR: The process failed, please retry, SIR.","SIR: Requesting another attempt, SIR.","SIR: Command not completed, try again, SIR.","SIR: Please repeat your input, SIR."]))
                except Exception as e:
                    print(random.choice(["\033[31mSIR: No language found, SIR.\033[0m","\033[32mSIR: I couldn't detect any language, SIR.\033[0m","\033[33mSIR: No valid language was recognized, SIR.\033[0m","\033[35mSIR: SIR, there is no language available.\033[0m","\033[36mSIR: No matching language detected, SIR.\033[0m","\033[37mSIR: I did not find any language option, SIR.\033[0m"]))
                    jarvis_speak(random.choice(["Enter SIR: No language found, SIR","SIR: I couldn't detect any language, SIR.","SIR: No valid language was recognized, SIR.","SIR: SIR, there is no language available.","SIR: No matching language detected, SIR.","SIR: I did not find any language option, SIR."]))

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||SYSTEM|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||#
                
            elif "system" in user_text.lower():
                print(random.choice(["\033[31mSir, could you please provide the current date, time, calendar status, shutdown/restart options, battery level, and available space?\033[0m","\033[32mSir, what’s the date and time now? Also, how’s the battery and storage?\033[0m","\033[33mSir, info on date, time, battery, storage, and restart/shutdown?\033[0m","\033[34mHey Sir, can you tell me the date, time, and how much battery and space we’ve got? Also, shutdown or restart status?\033[0m","\033[35mSir, please report system parameters: date, time, calendar events, power status, and available memory/storage\033[0m","\033[36mSir, may I know the current date, time, calendar, battery level, and available storage\033[0m","\033[37mSir, could you give me the details of date, time, calendar, battery status, free storage, and shutdown/restart options?\033[0m"]))
                jarvis_speak(random.choice(["Sir, could you please provide the current date, time, calendar status, shutdown/restart options, battery level, and available space?","Sir, what’s the date and time now? Also, how’s the battery and storage?","Sir, info on date, time, battery, storage, and restart/shutdown?","Hey Sir, can you tell me the date, time, and how much battery and space we’ve got? Also, shutdown or restart status?","Sir, please report system parameters: date, time, calendar events, power status, and available memory/storage","Sir, may I know the current date, time, calendar, battery level, and available storage","Sir, could you give me the details of date, time, calendar, battery status, free storage, and shutdown/restart options?","Sir, show date, time, battery, storage, and restart/shutdown info.","Sir, what’s the date and time, battery level, storage space, and are we good for restart or shutdown?","Sir, I’m curious—can you tell me the current date, time, calendar, battery, storage, and shutdown/restart status?"]))
                try: 
                    with sr.Microphone() as source: 
                        recognizer.adjust_for_ambient_noise(source, duration=1)
                        open_system = recognizer.listen(source)
                        c = recognizer.recognize_google(open_system, language='en-IN')
                        MEMORY["SYSTEM"]=c
                        if "time" in c.lower():
                            c_d = datetime.now().strftime("%H:%M:%S")
                            jarvis_speak("SIR: The time is " + c_d)                            
                        elif "calendar" in c.lower():
                            year = datetime.now().year
                            month = datetime.now().month
                            cal = calendar.month(year, month)
                            print(cal)
                            jarvis_speak(f"SIR: Here is the calendar for {calendar.month_name[month]} {year}. Please check the screen.")
                        elif "battery" in c.lower():
                            s=psutil.sensors_battery().percent
                            jarvis_speak(f"Sir Battery percentage is {s}%") 
                        elif "space" in c.lower():
                            dp=psutil.virtual_memory()
                            pd=round(dp.available/(1024**3),2)
                            jarvis_speak(f"Sir Available Space In Ram is {pd} GB")
                        else:
                            print(random.choice(["\033[31mSIR: No module found, SIR.\033[0m","\033[32mSIR: The required module is missing, SIR.\033[0m","\033[33mSIR: I couldn't locate the module, SIR.\033[0m","\033[34mSIR: Module not detected, SIR.\033[0m","\033[35mSIR: SIR, the module you requested doesn't exist.\033[0m","\033[36mSIR: Unable to find the specified module, SIR.\033[0m","\033[37mSIR: The module is unavailable, SIR.\033[0m"]))
                            jarvis_speak(random.choice([ "SIR: No module found, SIR.","SIR: The required module is missing, SIR.","SIR: I couldn't locate the module, SIR.","SIR: Module not detected, SIR.","SIR: SIR, the module you requested doesn't exist.","SIR: Unable to find the specified module, SIR.","SIR: The module is unavailable, SIR.","SIR: Missing module error, SIR.","SIR: I cannot load the module, SIR.","SIR: SIR, no valid module was found."]))
                except Exception as e:
                    print(random.choice(["\033[31mSIR: It is situated in the system, SIR.\033[0m","\033[32mSIR: It is located inside the system, SIR.\033[0m","\033[33mSIR: The file is present within the system, SIR.\033[0m","\033[34mSIR: It exists inside the system, SIR.\033[0m","\033[35mSIR: SIR, it is already in the system.\033[0m","\033[36mSIR: The module is stored in the system, SIR.\033[0m","\033[37mSIR: It resides within the system, SIR.\033[0m"]))
                    jarvis_speak(random.choice(["SIR: It is situated in the system, SIR.","SIR: It is located inside the system, SIR.","SIR: The file is present within the system, SIR.","SIR: It exists inside the system, SIR.","SIR: SIR, it is already in the system.","SIR: The module is stored in the system, SIR.","SIR: It resides within the system, SIR.","SIR: It is found inside the system, SIR.","SIR: SIR, it is available in the system.","SIR: The item is inside the system directory, SIR."]))

            elif "date" in user_text.lower():
                c_t = datetime.now().strftime("%A %d %B %Y")
                jarvis_speak("SIR: Today's date is " + c_t)
            elif "now" in user_text.lower():
                print(random.choice([ "\033[31m Sir, shutting down the system. Kindly wait.\033[0m","\033[32m Sir, the system is now closing. Please stand by.\033[0m","\033[33m Sir, system shutdown in progress. Please wait a moment.\033[0m","\033[34m Sir, we are shutting the system. Your patience is appreciated.\033[0m","\033[35m Sir, the system is powering off. Please hold on.\033[0m","\033[36m Sir, initiating system shutdown. Please wait.\033[0m","\033[37m Sir, the system is being turned off. Kindly wait.\033[0m","Sir, system closing now. Please remain patient.","Sir, we are in the process of shutting down the system. Please stand by.","Sir, beginning system shutdown sequence. Please wait."]))
                jarvis_speak(random.choice([ "Sir, shutting down the system. Kindly wait.","Sir, the system is now closing. Please stand by.","Sir, system shutdown in progress. Please wait a moment.","Sir, we are shutting the system. Your patience is appreciated.","Sir, the system is powering off. Please hold on.","Sir, initiating system shutdown. Please wait.","Sir, the system is being turned off. Kindly wait.","Sir, system closing now. Please remain patient.","Sir, we are in the process of shutting down the system. Please stand by.","Sir, beginning system shutdown sequence. Please wait."]))
                os.system("shutdown /s /t 5")
                break
            elif "restart" in user_text.lower():
                print(random.choice(["\033[31mSIR: Restarting the system. Please wait.\033[0m","\033[32mSIR: Restarting the system. Please wait.\033[0m","\033[33mSIR: Restarting the system. Please wait.\033[0m","\033[34mSIR: Restarting the system. Please wait.\033[0m","\033[35mSIR: Restarting the system. Please wait.\033[0m","\033[36mSIR: Restarting the system. Please wait.\033[0m","\033[37mSIR: Restarting the system. Please wait.\033[0m"]))
                jarvis_speak("SIR: Restarting the system. Please wait.")
                os.system("shutdown /r /t 5")
                break
            elif "stop" in user_text.lower():
                print(random.choice(["\033[31mSIR: Goodbye, SIR.\033[0m","\033[32mSIR: Farewell, SIR.\033[0m","\033[33mSIR: Shutting down. Goodbye, SIR.\033[0m","\033[34mSIR: Take care, SIR. Goodbye.\033[0m","\033[35mSIR: Until next time, SIR.\033[0m","\033[36mSIR: Goodbye. At your service anytime, SIR.\033[0m","\033[37mSIR: Disconnecting now, SIR. Goodbye.\033[0m","SIR: Wishing you a good day, SIR. Goodbye.","SIR: Logging off. Goodbye, SIR.","SIR: Goodbye, SIR. Awaiting your next command."]))
                jarvis_speak(random.choice(["SIR: Goodbye, SIR.","SIR: Farewell, SIR.","SIR: Shutting down. Goodbye, SIR.","SIR: Take care, SIR. Goodbye.","SIR: Until next time, SIR.","SIR: Goodbye. At your service anytime, SIR.","SIR: Disconnecting now, SIR. Goodbye.","SIR: Wishing you a good day, SIR. Goodbye.","SIR: Logging off. Goodbye, SIR.","SIR: Goodbye, SIR. Awaiting your next command."]))
                break 

            elif "song" in user_text.lower():
                print(random.choice(["\033[31mSir, please tell me which song you want, dhun, malang, bang bang\033[0m","\033[32mSir, which song would you like to play, dhun, malang, bang bang\033[0m","\033[33mSir, can you choose a song for me to play, dhun, malang, bang bang\033[0m","\033[34mSir, what’s your song choice today, dhun, malang, bang bang\033[0m","\033[35mSir, please let me know which song you want to listen to, dhun, malang, bang bang\033[0m","\033[36mSir, which song should I play for you, dhun, malang, bang bang\033[0m","\033[37mSir, tell me the song you prefer, dhun, malang, bang bang\033[0m","Sng bang, or another"]))
                jarvis_speak(random.choice(["Sir, please tell me which song you want, dhun, malang, bang bang","Sir, which song would you like to play, dhun, malang, bang bang","Sir, can you choose a song for me to play, dhun, malang, bang bang","Sir, what’s your song choice today, dhun, malang, bang bang","Sir, please let me know which song you want to listen to, dhun, malang, bang bang","Sir, which song should I play for you, dhun, malang, bang bang","Sir, tell me the song you prefer, dhun, malang, bang bang","Sir, please select a song, dhun, malang, bang bang, or another one","Sir, what song do you want me to play, dhun, malang, bang bang","Sir, I can play a song for you, which one do you want, dhun, malang, bang bang"]))
                try: 
                    with sr.Microphone() as source: 
                        recognizer.adjust_for_ambient_noise(source, duration=1)
                        open_system = recognizer.listen(source)
                        de = recognizer.recognize_google(open_system, language='en-IN')
                        MEMORY["SONG"]=de
                        if "dhun" in de.lower():
                            print(random.choice(["\033[31m opening online dhun song \033[0m","\033[32m opening online dhun song \033[0m","\033[33m opening online dhun song \033[0m","\033[34m opening online dhun song \033[0m","\033[35m opening online dhun song \033[0m","\033[36m opening online dhun song \033[0m","\033[37m opening online dhun song \033[0m"]))
                            jarvis_speak("opening online dhun song")
                            webbrowser.open("https://youtu.be/cUmUOb7j3dc?si=7zrus35E3IOElccy")
                        elif "malang" in de.lower():
                            print(random.choice(["\033[31mopening online malang song\033[0m","\033[32mopening online malang song\033[0m","\033[33mopening online malang song\033[0m","\033[34mopening online malang song\033[0m","\033[35mopening online malang song\033[0m","\033[36mopening online malang song\033[0m","\033[37mopening online malang song\033[0m"]))
                            jarvis_speak("opening online malang song")
                            webbrowser.open("https://youtu.be/KBIq11mNB0I?si=2HR9JxnDFz-cOQvK")
                        elif "bang" in de.lower():
                            print(random.choice(["\033[31mopening online bang bang song\033[0m","\033[32mopening online bang bang song\033[0m","\033[33mopening online bang bang song\033[0m","\033[34mopening online bang bang song\033[0m","\033[35mopening online bang bang song\033[0m","\033[36mopening online bang bang song\033[0m","\033[37mopening online bang bang song\033[0m"]))
                            jarvis_speak("opening online bang bang song")
                            webbrowser.open("https://youtu.be/jZyAB2KFDls?si=AuFiGsKKjLPEY4fX")
                        elif "ishq" in de.lowe():
                            print(random.choice(["\033[31mopening online ishq shava song\033[0m","\033[32mopening online ishq shava song\033[0m","\033[33mopening online ishq shava song\033[0m","\033[34mopening online ishq shava song\033[0m","\033[35mopening online ishq shava song\033[0m","\033[36mopening online ishq shava song\033[0m","\033[37mopening online ishq shava song\033[0m"]))
                            jarvis_speak("opening online ishq shava song")
                            webbrowser.open("https://youtu.be/iEJPDYrLtsI?si=Lb7wD7bwJ1BqH8aE")
                        elif "haare" in de.lower():
                            print(random.choice(["\033[31mopening online haare haare song\033[0m","\033[32mopening online haare haare song\033[0m","\033[33mopening online haare haare song\033[0m","\033[34mopening online haare haare song\033[0m","\033[35mopening online haare haare song\033[0m","\033[36mopening online haare haare song\033[0m","\033[37mopening online haare haare song\033[0m"]))
                            jarvis_speak("opening online haare haare song")
                            webbrowser.open("https://youtu.be/0SeWx-FC5LE?si=BO_ti-oUcOojm56F")
                        else:
                            print(random.choice(["\033[31mSIR: It is situated in the song, SIR.\033[0m","\033[32mSIR: It is located inside the song, SIR.\033[0m","\033[33mSIR: The content is found within the song, SIR.\033[0m","\033[34mSIR: It exists in the song, SIR.\033[0m","\033[35mSIR: SIR, it is already present in the song.\033[0m","\033[36mSIR: It is included in the song, SIR.\033[0m","\033[37mSIR: The detail is inside the song, SIR.\033[0m"]))
                            jarvis_speak(random.choice(["SIR: It is situated in the song, SIR.","SIR: It is located inside the song, SIR.","SIR: The content is found within the song, SIR.","SIR: It exists in the song, SIR.","SIR: SIR, it is already present in the song.","SIR: It is included in the song, SIR.","SIR: The detail is inside the song, SIR."]))    
                
                except Exception as e:
                    print(random.choice(["\033[31mSIR: No song found, SIR.\033[0m","\033[32mSIR: I couldn't find any song, SIR.\033[0m","\033[33mSIR: No matching song detected, SIR.\033[0m","\033[34mSIR: SIR, there is no song available.\033[0m","\033[35mSIR: No audio file found, SIR.\033[0m","\033[36mSIR: The requested song is missing, SIR.\033[0m","\033[37mSIR: Unable to locate the song, SIR.\033[0m"]))
                    jarvis_speak(random.choice(["SIR: No song found, SIR.","SIR: I couldn't find any song, SIR.","SIR: No matching song detected, SIR.","SIR: SIR, there is no song available.","SIR: No audio file found, SIR.","SIR: The requested song is missing, SIR.","SIR: Unable to locate the song, SIR."]))

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\OPEN LINK||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\\\#

            elif "open" in user_text.lower():
                print(random.choice(["\033[31mSir, please tell me what you want to open, Google Chrome, YouTube, W3Schools\033[0m","\033[32mSir, which one should I open for you, Google Chrome, YouTube, or W3Schools\033[0m","\033[33mSir, can you choose what you want to open, Google Chrome, YouTube, W3Schools\033[0m","\033[34mSir, what do you want to open today, Google Chrome, YouTube, or W3Schools\033[0m","\033[35mSir, please let me know whether you want to open Google Chrome, YouTube, or W3Schools\033[0m","\033[36mSir, which app or site should I launch, Google Chrome, YouTube, W3Schools\033[0m","\033[37mSir, tell me what you want me to open, Google Chrome, YouTube, or W3Schools\033[0m"]))                
                jarvis_speak(random.choice(["Sir, please tell me what you want to open, Google Chrome, YouTube, W3Schools","Sir, which one should I open for you, Google Chrome, YouTube, or W3Schools","Sir, can you choose what you want to open, Google Chrome, YouTube, W3Schools","Sir, what do you want to open today, Google Chrome, YouTube, or W3Schools","Sir, please let me know whether you want to open Google Chrome, YouTube, or W3Schools","Sir, which app or site should I launch, Google Chrome, YouTube, W3Schools","Sir, tell me what you want me to open, Google Chrome, YouTube, or W3Schools","Sir, please select one to open, Google Chrome, YouTube, W3Schools, or another","Sir, what do you want to access, Google Chrome, YouTube, or W3Schools","Sir, I can open something for you, which one should it be, Google Chrome, YouTube, W3Schools"]))
                try: 
                    with sr.Microphone() as source: 
                        recognizer.adjust_for_ambient_noise(source, duration=1)
                        opening_link = recognizer.listen(source)
                        o = recognizer.recognize_google(opening_link, language='en-IN')
                        MEMORY["OPEN"]=o
                        if "youtube" in o.lower():
                            print(random.choice(["\033[31mSIR: Opening YouTube\033[0m","\033[32mSIR: Opening YouTube\033[0m","\033[33mSIR: Opening YouTube\033[0m","\033[34mSIR: Opening YouTube\033[0m","\033[35mSIR: Opening YouTube\033[0m","\033[36mSIR: Opening YouTube\033[0m","\033[37mSIR: Opening YouTube\033[0m"]))
                            jarvis_speak("SIR: Opening YouTube")
                            webbrowser.open("https://www.youtube.com")
                        elif "google" in o.lower():
                            print(random.choice(["\033[31mSIR: Opening Google\033[0m","\033[32mSIR: Opening Google\033[0m","\033[33mSIR: Opening Google\033[0m","\033[34mSIR: Opening Google\033[0m","\033[35mSIR: Opening Google\033[0m","\033[36mSIR: Opening Google\033[0m","\033[37mSIR: Opening Google\033[0m"]))
                            jarvis_speak("SIR: Opening Google")
                            webbrowser.open("https://www.google.com") 
                        elif "chrome" in o.lower():
                            print(random.choice(["\033[31mSIR: Opening Chrome\033[0m","\033[32mSIR: Opening Chrome\033[0m","\033[33mSIR: Opening Chrome\033[0m","\033[34mSIR: Opening Chrome\033[0m","\033[35mSIR: Opening Chrome\033[0m","\033[36mSIR: Opening Chrome\033[0m","\033[37mSIR: Opening Chrome\033[0m"]))
                            jarvis_speak("SIR: Opening YouTube")
                            webbrowser.open("https://www.chrome.com")
                        elif "school" in o.lower():
                            print(random.choice(["\033[31mSIR: Opening W3 SCHOOL\033[0m","\033[32mSIR: Opening W3 SCHOOL\033[0m","\033[33mSIR: Opening W3 SCHOOL\033[0m","\033[34mSIR: Opening W3 SCHOOL\033[0m","\033[35mSIR: Opening W3 SCHOOL\033[0m","\033[36mSIR: Opening W3 SCHOOL\033[0m","\033[37mSIR: Opening W3 SCHOOL\033[0m"]))
                            jarvis_speak("SIR: Opening W3 Schools")
                            webbrowser.open("https://www.w3schools.com")

                        else:
                            print(random.choice(["\033[31mSIR: No module found, SIR.\033[0m","\033[32mSIR: I couldn't locate the module, SIR.\033[0m","\033[33mSIR: The requested module is missing, SIR.\033[0m","\033[34mSIR: SIR, no such module exists.\033[0m","\033[35mSIR: Module not detected in the system, SIR.\033[0m","\033[36mSIR: Unable to load the module, SIR.\033[0m","\033[37mSIR: The module could not be found, SIR.\033[0m"]))
                            jarvis_speak(random.choice(["SIR: No module found, SIR.","SIR: I couldn't locate the module, SIR.","SIR: The requested module is missing, SIR.","SIR: SIR, no such module exists.","SIR: Module not detected in the system, SIR.","SIR: Unable to load the module, SIR.","SIR: The module could not be found, SIR.","SIR: Missing module. Please check again, SIR.","SIR: SIR, I can't find that module anywhere.","SIR: No valid module was located, SIR."]))
                except Exception as e:
                    print(random.choice(["\033[31mSIR: It is located in the open section, SIR.\033[0m","\033[32mSIR: It is situated under Open, SIR.\033[0m","\033[33mSIR: You will find it in the Open category, SIR.\033[0m","\033[34mSIR: SIR, it is inside the Open directory.\033[0m","\033[35mSIR: It exists in the Open area, SIR.\033[0m","\033[36mSIR: The item is present in the Open section, SIR.\033[0m","\033[37mSIR: It is stored under Open, SIR.\033[0m","SIR: SIR, it is found in the Open folder.","SIR: It is placed inside Open, SIR.","SIR: That component is located in the Open zone, SIR."]))
                    jarvis_speak(random.choice(["SIR: It is located in the open section, SIR.","SIR: It is situated under Open, SIR.","SIR: You will find it in the Open category, SIR.","SIR: SIR, it is inside the Open directory.","SIR: It exists in the Open area, SIR.","SIR: The item is present in the Open section, SIR.","SIR: It is stored under Open, SIR.","SIR: SIR, it is found in the Open folder.","SIR: It is placed inside Open, SIR.","SIR: That component is located in the Open zone, SIR."]))

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\CustomKeyword||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||#
            
            elif "custom" in user_text.lower():
                print(random.choice(["\033[31mSir, please tell me what you want, anime, normal, Avengers, politician, or personal\033[0m","\033[32mSir, which category should I show you, anime, normal, Avengers, politician, or personal\033[0m","\033[33mSir, can you choose a category, anime, normal, Avengers, politician, or personal\033[0m","\033[34mSir, what type do you want, anime, normal, Avengers, politician, or personal\033[0m","\033[35mSir, please let me know which one you prefer, anime, normal, Avengers, politician, or personal\033[0m","\033[37mSir, tell me the category you want, anime, normal, Avengers, politician, or personal\033[0m"]))
                jarvis_speak(random.choice(["Sir, please tell me what you want, anime, normal, Avengers, politician, or personal","Sir, which category should I show you, anime, normal, Avengers, politician, or personal","Sir, can you choose a category, anime, normal, Avengers, politician, or personal","Sir, what type do you want, anime, normal, Avengers, politician, or personal","Sir, please let me know which one you prefer, anime, normal, Avengers, politician, or personal","Sir, tell me the category you want, anime, normal, Avengers, politician, or personal","Sir, please select one category, anime, normal, Avengers, politician, or personal","Sir, which option do you want, anime, normal, Avengers, politician, or personal","Sir, I can show you a category, which one do you want, anime, normal, Avengers, politician, or personal","Sir, choose the type you want, anime, normal, Avengers, politician, or personal"]))
                try: 
                    with sr.Microphone() as source: 
                        recognizer.adjust_for_ambient_noise(source, duration=1)
                        opening_link = recognizer.listen(source)
                        k = recognizer.recognize_google(opening_link, language='en-IN')
                        MEMORY["CUSTOM"]=k

                        if "anime" in k.lower():
                            print(random.choice(["\033[31mWhich character would you like: Makima, Naruto, Denji, Tanjiro, someone from Attack on Titan, or a devil?\033[0m","\033[32mPlease choose a character: Makima, Naruto, Denji, Tanjiro, an Attack on Titan character, or a devil.\033[0m","\033[33mWhich one should I pick for you—Makima, Naruto, Denji, Tanjiro, Attack on Titan, or a devil?\033[0m","\033[34mTell me which character you want: Makima, Naruto, Denji, Tanjiro, an Attack on Titan character, or a devil.\033[0m","\033[35mWho do you choose: Makima, Naruto, Denji, Tanjiro, an AOT character, or a devil?\033[0m","\033[36mSelect a character from this list: Makima, Naruto, Denji, Tanjiro, Attack on Titan, or devil.\033[0m","\033[37mLet me know your choice—Makima, Naruto, Denji, Tanjiro, Attack on Titan, or devil.\033[0m"]))
                            jarvis_speak(random.choice(["Which character would you like: Makima, Naruto, Denji, Tanjiro, someone from Attack on Titan, or a devil?","Please choose a character: Makima, Naruto, Denji, Tanjiro, an Attack on Titan character, or a devil.","Which one should I pick for you—Makima, Naruto, Denji, Tanjiro, Attack on Titan, or a devil?","Tell me which character you want: Makima, Naruto, Denji, Tanjiro, an Attack on Titan character, or a devil.","Who do you choose: Makima, Naruto, Denji, Tanjiro, an AOT character, or a devil?","Select a character from this list: Makima, Naruto, Denji, Tanjiro, Attack on Titan, or devil.","Let me know your choice—Makima, Naruto, Denji, Tanjiro, Attack on Titan, or devil."]))
                            try: 
                                with sr.Microphone() as source: 
                                    recognizer.adjust_for_ambient_noise(source, duration=1)
                                    opening_link = recognizer.listen(source)
                                    kd = recognizer.recognize_google(opening_link, language='en-IN')
                                    MEMORY["ANIME"]=kd
                                    if "naruto" in kd.lower():
                                        print("\033[31mNaruto Uzumaki, once an isolated child of Konoha, dreamed of becoming Hokage. With fierce determination and the Nine-Tails' power, he overcame hardship and built powerful friendships, showing the world that perseverance can turn an outcast into a hero.\033[0m","\033[32mDespite growing up alone and disliked, Naruto Uzumaki never let go of his goal to become Hokage. His resolve, the strength of the Nine-Tails, and the bonds he formed helped him rise above every obstacle and prove his worth as a true hero.\033[0m","\033[33mShunned in his childhood, Naruto Uzumaki held tightly to his ambition of becoming Hokage. Through grit, courage, and the support of his friends—and with the Nine-Tails within him—he demonstrated that even someone rejected by many can achieve greatness.\033[0m","\033[34mNaruto Uzumaki, once viewed as an outcast in Konoha, continued to chase his Hokage dream. With the Nine-Tails' power and his unwavering spirit, he faced trial after trial, forming deep bonds that shaped him into a legendary hero.\033[0m","\033[35mGrowing up misunderstood, Naruto Uzumaki still aspired to become Hokage. His unbreakable determination, the strength of the Nine-Tails, and the friendships he formed pushed him through every challenge, proving his heroic heart.\033[0m","\033[36mEven though the village shunned him as a child, Naruto Uzumaki never abandoned his dream of becoming Hokage. Guided by perseverance, courage, and the powerful fox spirit within him, he turned his hardships into the path of a hero.\033[0m","\033[37mNaruto Uzumaki started life as an outsider, yet his dream of becoming Hokage never faded. With tireless resolve, the Nine-Tails' power, and strong bonds with his friends, he overcame every setback to become a symbol of true heroism.\033[0m")
                                        jarvis_speak(random.choice([ "Naruto Uzumaki, once an isolated child of Konoha, dreamed of becoming Hokage. With fierce determination and the Nine-Tails' power, he overcame hardship and built powerful friendships, showing the world that perseverance can turn an outcast into a hero.","Despite growing up alone and disliked, Naruto Uzumaki never let go of his goal to become Hokage. His resolve, the strength of the Nine-Tails, and the bonds he formed helped him rise above every obstacle and prove his worth as a true hero.","Shunned in his childhood, Naruto Uzumaki held tightly to his ambition of becoming Hokage. Through grit, courage, and the support of his friends—and with the Nine-Tails within him—he demonstrated that even someone rejected by many can achieve greatness.","Naruto Uzumaki, once viewed as an outcast in Konoha, continued to chase his Hokage dream. With the Nine-Tails' power and his unwavering spirit, he faced trial after trial, forming deep bonds that shaped him into a legendary hero.","Growing up misunderstood, Naruto Uzumaki still aspired to become Hokage. His unbreakable determination, the strength of the Nine-Tails, and the friendships he formed pushed him through every challenge, proving his heroic heart.","Even though the village shunned him as a child, Naruto Uzumaki never abandoned his dream of becoming Hokage. Guided by perseverance, courage, and the powerful fox spirit within him, he turned his hardships into the path of a hero.","Naruto Uzumaki started life as an outsider, yet his dream of becoming Hokage never faded. With tireless resolve, the Nine-Tails' power, and strong bonds with his friends, he overcame every setback to become a symbol of true heroism."]))
                                    elif "denji" in kd.lower():
                                        print(random.choice(["\033[37mDenji, a broke teen in debt, fuses with Pochita to become Chainsaw Man, fighting devils while chasing a simple, happy life.\033[0m","\033[36mAfter merging with Pochita, Denji becomes Chainsaw Man, battling devils and seeking basic comforts in a harsh world.\033[0m","\033[35mDenji gains chainsaw powers through Pochita, using them to fight devils as he dreams of a better, easier life.\033[0m","\033[34mA poor boy turned Chainsaw Man, Denji cuts down devils while hoping for small joys and a peaceful future.\033[0m","\033[33mDenji, once drowning in debt, becomes Chainsaw Man and keeps pushing forward for food, comfort, and happiness.\033[0m","\033[32mMerged with Pochita, Denji wields chainsaws to fight devils, driven by simple dreams and stubborn determination.\033[0m","\033[31mFrom poverty to Chainsaw Man, Denji battles devils with wild resolve, chasing a life with a bit of happiness.\033[0m"]))
                                        jarvis_speak(random.choice([ "Denji, a broke teen in debt, fuses with Pochita to become Chainsaw Man, fighting devils while chasing a simple, happy life.","After merging with Pochita, Denji becomes Chainsaw Man, battling devils and seeking basic comforts in a harsh world.","Denji gains chainsaw powers through Pochita, using them to fight devils as he dreams of a better, easier life.","A poor boy turned Chainsaw Man, Denji cuts down devils while hoping for small joys and a peaceful future.","Denji, once drowning in debt, becomes Chainsaw Man and keeps pushing forward for food, comfort, and happiness.","Merged with Pochita, Denji wields chainsaws to fight devils, driven by simple dreams and stubborn determination.","From poverty to Chainsaw Man, Denji battles devils with wild resolve, chasing a life with a bit of happiness."]))
                                    elif "tanjiro" in kd.lower():
                                        print(random.choice(["\033[36mTanjiro becomes a Demon Slayer after losing his family, fighting demons to save Nezuko and protect others with his compassion and skill.\033[0m","\033[35mAfter his family is killed, Tanjiro trains as a Demon Slayer, using water-breathing techniques to fight for Nezuko and humanity.\033[0m","\033[34mTanjiro, kind-hearted and determined, battles demons to cure Nezuko while protecting innocent lives.\033[0m","\033[34mDriven by love for his sister, Tanjiro joins the Demon Slayers, using his strength and empathy in every fight.\033[0m","\033[33mTanjiro turns tragedy into purpose, hunting demons with his water techniques and unwavering resolve.\033[0m","\033[32mAfter Nezuko becomes a demon, Tanjiro fights tirelessly as a Demon Slayer to save her and help others.\033[0m","\033[31mTanjiro faces darkness head-on, using skill and compassion to battle demons and seek a cure for Nezuko.\033[0m"]))
                                        jarvis_speak(random.choice(["Tanjiro becomes a Demon Slayer after losing his family, fighting demons to save Nezuko and protect others with his compassion and skill.","After his family is killed, Tanjiro trains as a Demon Slayer, using water-breathing techniques to fight for Nezuko and humanity.","Tanjiro, kind-hearted and determined, battles demons to cure Nezuko while protecting innocent lives.","Driven by love for his sister, Tanjiro joins the Demon Slayers, using his strength and empathy in every fight.","Tanjiro turns tragedy into purpose, hunting demons with his water techniques and unwavering resolve.","After Nezuko becomes a demon, Tanjiro fights tirelessly as a Demon Slayer to save her and help others.","Tanjiro faces darkness head-on, using skill and compassion to battle demons and seek a cure for Nezuko."]))
                                    elif "titan" in kd.lower():
                                        print(random.choice(["\033[36mEren Yeager joins the Scouts after losing his home to Titans, fighting to protect humanity and uncover the truth.\033[0m","\033[35mDriven by tragedy, Eren enters the Scout Regiment, learning shocking truths about the Titans and himself.\033[0m","\033[34mEren fights with Mikasa and Armin to save humanity, discovering dark secrets that change his fate.\033[0m","\033[34mAfter Titans destroy his home, Eren’s resolve leads him into battles that reveal the world’s hidden horrors.\033[0m","\033[33mEren seeks freedom by joining the Scouts, facing truths that reshape his mission and identity.\033[0m","\033[32mFueled by loss, Eren battles Titans and uncovers secrets that alter humanity’s future.\033[0m","\033[31mEren’s determination pushes him through the Scout Regiment’s harsh battles as he learns the real story behind the Titans.\033[0m"]))
                                        jarvis_speak(random.choice(["Eren Yeager joins the Scouts after losing his home to Titans, fighting to protect humanity and uncover the truth.","Driven by tragedy, Eren enters the Scout Regiment, learning shocking truths about the Titans and himself.","Eren fights with Mikasa and Armin to save humanity, discovering dark secrets that change his fate.","After Titans destroy his home, Eren’s resolve leads him into battles that reveal the world’s hidden horrors.","Eren seeks freedom by joining the Scouts, facing truths that reshape his mission and identity.","Fueled by loss, Eren battles Titans and uncovers secrets that alter humanity’s future.","Eren’s determination pushes him through the Scout Regiment’s harsh battles as he learns the real story behind the Titans."]))
                                    elif "makima" in kd.lower():
                                        print(random.choice(["\033[37mMakima, a calm yet commanding devil hunter, hides a ruthless nature behind her controlled demeanor.\033[0m","\033[36mMysterious and powerful, Makima bends others to her will with quiet authority and hidden cruelty.\033[0m","\033[35mMakima’s calm smile masks her manipulative power, making her a terrifying force in the devil-hunting world.\033[0m","\033[34mWith total control and quiet confidence, Makima uses her influence to shape others to her desires.\033[0m","\033[33mMakima appears gentle, but her true nature is calculating, manipulative, and dangerously ambitious.\033[0m","\033[32mBehind her composed exterior, Makima exerts chilling control, steering others with ruthless intent.\033[0m","\033[31mMakima’s authority and mystery conceal a manipulative heart, making escape from her influence nearly impossible.\033[0m"]))
                                        jarvis_speak(random.choice(["Makima, a calm yet commanding devil hunter, hides a ruthless nature behind her controlled demeanor.","Mysterious and powerful, Makima bends others to her will with quiet authority and hidden cruelty.","Makima’s calm smile masks her manipulative power, making her a terrifying force in the devil-hunting world.","With total control and quiet confidence, Makima uses her influence to shape others to her desires.","Makima appears gentle, but her true nature is calculating, manipulative, and dangerously ambitious.","Behind her composed exterior, Makima exerts chilling control, steering others with ruthless intent.","Makima’s authority and mystery conceal a manipulative heart, making escape from her influence nearly impossible."]))
                                    elif "devil" in kd.lower():
                                        print(random.choice([ "\033[37mThe Gun Devil, born from humanity’s fear of guns, is one of the most powerful devils, killing over a million people in minutes.\033[0m","\033[32mFeared worldwide, the Gun Devil’s brief appearance caused massive destruction, making it a legendary threat.\033[0m","\033[33mBecause fear of guns is universal, the Gun Devil gained extreme power, devastating the world in a single attack.\033[0m","\033[34mThe Gun Devil’s massacre turned it into a global weapon, with countries collecting its fragments for military use.\033[0m","\033[35mThough it rarely appears, the Gun Devil’s influence shapes the world, inspiring revenge and fear in many characters.\033[0m","\033[36mThe Gun Devil’s body is scattered across nations as weapons, while its core remains a deadly force.\033[0m","\033[31mMakima manipulates events using the Gun Devil, pushing it into battles that further her hidden agenda.\033[0m"]))
                                        jarvis_speak(random.choice([ "The Gun Devil, born from humanity’s fear of guns, is one of the most powerful devils, killing over a million people in minutes.","Feared worldwide, the Gun Devil’s brief appearance caused massive destruction, making it a legendary threat.","Because fear of guns is universal, the Gun Devil gained extreme power, devastating the world in a single attack.","The Gun Devil’s massacre turned it into a global weapon, with countries collecting its fragments for military use.","Though it rarely appears, the Gun Devil’s influence shapes the world, inspiring revenge and fear in many characters.","The Gun Devil’s body is scattered across nations as weapons, while its core remains a deadly force.","Makima manipulates events using the Gun Devil, pushing it into battles that further her hidden agenda."]))
                                    else:
                                        jarvis_speak(random.choice(["\033[31mSIR: No anime found, SIR.\033[0m","\033[32mSIR: I couldn't find any anime, SIR.\033[0m","\033[33mSIR: No matching anime detected, SIR.\033[0m","\033[34mSIR: SIR, there is no anime available.\033[0m","\033[35mSIR: The requested anime is missing, SIR.\033[0m","\033[36mSIR: Unable to locate the anime, SIR.\033[0m","\033[37mSIR: No anime exists for that search, SIR.\033[0m","looking for, SIR."]))
                                        jarvis_speak(random.choice(["SIR: No anime found, SIR.","SIR: I couldn't find any anime, SIR.","SIR: No matching anime detected, SIR.","SIR: SIR, there is no anime available.","SIR: The requested anime is missing, SIR.","SIR: Unable to locate the anime, SIR.","SIR: No anime exists for that search, SIR.","SIR: SIR, no valid anime was found.","SIR: I did not find the anime you're looking for, SIR.","SIR: System reports no anime found, SIR."]))
                            except Exception   as e:
                                print(random.choice(["\033[31mSIR: No anime found, SIR.\033[0m","\033[32mSIR: I couldn't locate any anime, SIR.\033[0m","\033[33mSIR: No anime matches your request, SIR.\033[0m","\033[34mSIR: SIR, there is no anime available.\033[0m","\033[35mSIR: The system found no anime, SIR.\033[0m","\033[36mSIR: Unable to find the requested anime, SIR.\033[0m","\033[37mSIR: No anime exists in the search results, SIR.\033[0m"]))
                                jarvis_speak(random.choice(["SIR: No anime found, SIR.","SIR: I couldn't locate any anime, SIR.","SIR: No anime matches your request, SIR.","SIR: SIR, there is no anime available.","SIR: The system found no anime, SIR.","SIR: Unable to find the requested anime, SIR.","SIR: No anime exists in the search results, SIR.","SIR: SIR, no valid anime was detected.","SIR: I did not find any anime for that query, SIR.","SIR: Search returned no anime, SIR."]))
#---------------------------------------------------------------CAPTAIN AMERICA----------------------------------------------------------------------------------------------------------#
                        elif "avengers" in k.lower():
                            jarvis_speak("SIR: Please Tell Me which character you want iron man, hulk, thor, ultron, captain america ? ")
                            try: 
                                with sr.Microphone() as source: 
                                    recognizer.adjust_for_ambient_noise(source, duration=1)
                                    opening_link = recognizer.listen(source)
                                    dc = recognizer.recognize_google(opening_link, language='en-IN')
                                    MEMORY["AVENGERS"]=dc
                                    if "iron" in dc.lower():
                                        jarvis_speak(random.choice([   "Tony Stark, a genius billionaire, becomes Iron Man after creating a suit in captivity and decides to protect the world.","With his brilliant mind and advanced suits, Tony Stark fights as Iron Man while confronting his personal flaws.","Tony Stark uses his technology and wealth to become Iron Man, defending the world with courage and wit.","After escaping captivity with his first suit, Tony Stark embraces his role as Iron Man and a global protector.","Armed with cutting-edge armor, Tony Stark battles threats while learning responsibility and sacrifice.","Tony Stark turns his genius into heroism as Iron Man, standing out for his bravery and sharp humor.","From captive to Avenger, Tony Stark uses his inventions and determination to fight for a safer world."]))
                                    elif "captain" in dc.lower():
                                        jarvis_speak( "Steve Rogers becomes Captain America, a super-soldier who fights for justice and freedom with his indestructible shield.","Humble and brave, Steve Rogers protects humanity as Captain America, inspiring others with courage and integrity.","Transformed into a super-soldier, Steve Rogers wields his shield to defend justice and stand against chaos.","Captain America, once Steve Rogers, fights for freedom and humanity, guided by unwavering morals.","Steve Rogers uses his strength and shield to lead and inspire, embodying courage in every battle.","From humble beginnings, Steve Rogers becomes Captain America, a symbol of justice and hope.","With his indestructible shield and steadfast values, Steve Rogers fights as Captain America to protect the world.")
                                    elif "thor" in dc.lower():
                                        jarvis_speak(random.choice( "Thor, God of Thunder, wields Mjolnir to protect the realms from cosmic threats with power and courage.","The mighty Thor fights alongside the Avengers, learning humility and the true meaning of heroism.","Thor uses his thunderous strength and enchanted hammer to defend the worlds from danger.","Asgard’s God of Thunder, Thor balances pride with friendship while battling cosmic enemies.","Thor’s noble heart and immense power make him a key protector of the realms.","With Mjolnir in hand, Thor faces threats alongside the Avengers, growing as a hero in the process.","Thor combines godly strength, courage, and honor to fight for the safety of all realms."))
                                    elif "hulk" in dc.lower():
                                        jarvis_speak("Bruce Banner, a brilliant scientist, becomes the Hulk after a gamma radiation accident. When angered, he transforms into a nearly unstoppable green powerhouse, torn between his human intellect and monstrous strength. Despite his destructive nature, Hulk fights to protect those he cares about and prove he’s more than just a monster.")
                                    elif "ultron" in dc.lower():
                                        jarvis_speak("Ultron, an AI created by Tony Stark to protect humanity, becomes self-aware and concludes that humans themselves are the greatest threat. Armed with immense intelligence and robotic strength, he seeks to bring about extinction to “save” the world. The Avengers must unite to stop the machine they inadvertently created before it’s too late.")
                                    else:
                                        jarvis_speak("No Avengers Found")
                            except Exception as e:
                                jarvis_speak("No Avengers found")
                        elif "politician" in k.lower():
                            jarvis_speak("SIR: Please Tell Me which politician information you want Narendra Modi, Rahul Gandhi, Yogi Adityanath, Rajnath Singh,  ? ")
                            try: 
                                with sr.Microphone() as source: 
                                    recognizer.adjust_for_ambient_noise(source, duration=1)
                                    opening_link = recognizer.listen(source)
                                    vb = recognizer.recognize_google(opening_link, language='en-IN')
                                    MEMORY["POLITICIAN"]=vb
                                    if "modi" in vb.lower():
                                        jarvis_speak("Narendra Modi, born in Gujarat, rose from humble beginnings as a tea seller to become India’s Prime Minister. Known for his strong leadership, he focuses on economic reforms, digital initiatives, and global diplomacy. His journey reflects determination, resilience, and a vision for India’s progress.")
                                    elif "rahul" in vb.lower():
                                        jarvis_speak("Rahul Gandhi, a prominent Congress leader, continues his family legacy in Indian politics. He advocates for social justice, youth empowerment, and political reforms, striving to address inequality and strengthen democracy.")
                                    elif "rajnath" in vb.lower():
                                        jarvis_speak("Rajnath Singh, a senior BJP leader and India’s Defence Minister, is known for his strong leadership and strategic thinking. He focuses on national security, defense modernization, and strengthening India’s political and administrative framework.")
                                    elif "yogi" in vb.lower():
                                        jarvis_speak("Yogi Adityanath, the Chief Minister of Uttar Pradesh, is known for his strong governance and focus on law, order, and development. He emphasizes cultural identity, infrastructure growth, and social initiatives in the state.")
                                    else:
                                        jarvis_speak("No Politician found sir")
                            except Exception as e:
                                jarvis_speak("No politician found sir") 
                        elif "personal" in k.lower():
                            jarvis_speak("SIR: Please Tell Me which type of information you want Father Number, Mother Number, Your Adhar Number, Your Mobile Number? ")
                            try: 
                                with sr.Microphone() as source: 
                                    recognizer.adjust_for_ambient_noise(source, duration=1)
                                    opening_link = recognizer.listen(source)
                                    qw = recognizer.recognize_google(opening_link, language='en-IN')
                                    MEMORY["PERSONAL"]=qw
                                    if "your" in qw.lower():
                                        jarvis_speak("Your mobile number is 6 3 8 6 7 2 9 7 2 5 .")
                                    elif "card" in qw.lower():
                                        jarvis_speak("Your adhaar number is 9 7 9 5 1 0 4 8 7 6 5 5 ")
                                    elif "mother" in qw.lower():
                                        jarvis_speak("your mother mobile number is 6 3 0 7 5 1 5 4 4 9")
                                    elif "father" in qw.lower():
                                        jarvis_speak("Your father mobile number is 8 1 1 5 4 3 1 3 3 5")
                                    else:
                                        jarvis_speak("No Information found sir")
                            except Exception as e:
                                jarvis_speak("it is located in personal")
                        elif "normal" in k.lower():
                            jarvis_speak("SIR: Please Continue ")
                            try: 
                                with sr.Microphone() as source: 
                                    recognizer.adjust_for_ambient_noise(source, duration=1)
                                    opening_link = recognizer.listen(source)
                                    bg = recognizer.recognize_google(opening_link, language='en-IN')
                                    MEMORY["NORMAL"]=bg
                                    if "hello" in bg.lower():
                                        jarvis_speak("SIR: how are you")
                                    elif "love" in bg.lower():
                                        jarvis_speak(" I LOVE YOU 3000 Sir ")
                                    elif "tum" in bg.lower():
                                        nova_speak("मैं तुम्हारी डिजिटल गर्लफ्रेंड हूँ ")
                                    elif "funny" in bg.lower():
                                        jarvis_speak("SIR: Did you know, your Wi-Fi password is more complex than your dating history?")
                                    elif "kya" in bg.lower():
                                        nova_speak("मेरा नाम AI साथी है ")
                                    elif "story" in bg.lower(): 
                                        jarvis_speak("In the vast universe, Thanos embarked on a journey to collect the six Infinity Stones.")
                                        jarvis_speak("Each stone held immense power and, together, could allow him to reshape reality itself.")
                # Power Stone
                                        time.sleep(2)
                                        jarvis_speak("First, the Power Stone awaited on Xandar, guarded by the Nova Corps.")
                                        jarvis_speak("Thanos, relentless in his mission, arrived and claimed the Power Stone, harnessing its raw energy.")
                # Space Stone
                                        time.sleep(2)
                                        jarvis_speak("Next, he turned to Asgard, where Loki held the Space Stone within the Tesseract.")
                                        jarvis_speak("Attacking Thor's ship, Thanos retrieved the Space Stone, bending space to his will.")
                # Reality Stone 
                                        time.sleep(2)
                                        jarvis_speak("On the planet Knowhere, the Reality Stone was in the possession of the Collector.")
                                        jarvis_speak("Thanos confronted the Collector and seized the Reality Stone, capable of altering reality itself.")
                # Soul Stone
                                        time.sleep(2)
                                        jarvis_speak("The Soul Stone required a grave sacrifice, hidden on the planet Vormir.")
                                        jarvis_speak("To claim it, Thanos made the ultimate choice and sacrificed Gamora, gaining the Soul Stone.")
                # Time Stone
                                        os.startfile("C:\\Users\\ts826\\Downloads\\OIP (2).webp")
                                        jarvis_speak("Returning to Earth, specifically New York, Thanos sought the Time Stone from Doctor Strange.")
                                        jarvis_speak("With cunning strategy, he obtained the Time Stone, granting mastery over time.")
                # Mind Stone
 
                                        time.sleep(2)
                                        jarvis_speak("Finally, in Wakanda, during a fierce battle, Thanos confronted the Avengers for the Mind Stone.")
                                        jarvis_speak("From Vision, he took the Mind Stone, completing the collection of all six Infinity Stones.")
                # Conclusion
                                        jarvis_speak("With all six Infinity Stones in the Infinity Gauntlet, Thanos could now reshape the universe with a single snap.")
                                        jarvis_speak("The universe trembled, as half of all life faced erasure, fulfilling Thanos' twisted vision of balance.")
                                        jarvis_speak("This marks the journey of Thanos, a titan who would go to any lengths to impose his version of order on the cosmos.")

                                    else:
                                        jarvis_speak("No Information found sir")
                            except Exception as e:
                                jarvis_speak("it is located in normal")
                except Exception as e:
                    jarvis_speak("It is loacted in custom")

            elif "bhajan" in user_text.lower():
                jarvis_speak(random.choice(["Sir, please tell me which bhajan you want, Lord Hanuman, Lord Krishna, or Lord Shiva or Lord Brahma","Sir, which bhajan should I play for you, Lord Hanuman, Lord Krishna, or Lord Shiva or Lord Brahma","Sir, can you choose a bhajan, Lord Hanuman, Lord Krishna, or Lord Shiva or Lord Brahma","Sir, what bhajan do you want to listen to, Lord Hanuman, Lord Krishna, or Lord Shiva or Lord Brahma","Sir, please let me know which bhajan you prefer, Lord Hanuman, Lord Krishna, or Lord Shiva or Lord Brahma","Sir, tell me the bhajan you want, Lord Hanuman, Lord Krishna, or Lord Shiva or Lord Brahma","Sir, please select a bhajan, Lord Hanuman, Lord Krishna, or Lord Shiva or Lord Brahma","Sir, which bhajan would you like me to play, Lord Hanuman, Lord Krishna, or Lord Shiva or Lord Brahma","Sir, I can play a bhajan for you, which one should it be, Lord Hanuman, Lord Krishna, or Lord Shiva or Lord Brahma","Sir, choose the bhajan you want, Lord Hanuman, Lord Krishna, or Lord Shiva or Lord Brahma"]))
                try: 
                    with sr.Microphone() as source: 
                        recognizer.adjust_for_ambient_noise(source, duration=1)
                        opening_link = recognizer.listen(source)
                        tr = recognizer.recognize_google(opening_link, language='en-IN')
                        MEMORY["BHAJAN"]=tr
                        if "hanuman" in tr.lower():
                            jarvis_speak("SIR: Please Tell Me which type of bhajn you want for lord hanuman chalisa, aarti, bajrang")
                            try: 
                                with sr.Microphone() as source: 
                                    recognizer.adjust_for_ambient_noise(source, duration=1)
                                    opening_link = recognizer.listen(source)
                                    bn = recognizer.recognize_google(opening_link, language='en-IN')
                                    MEMORY["HANUMAN"]=bn
                                    if "chalisa" in bn.lower():
                                        jarvis_speak("Playing Lord Hanumna Chalisa")
                                        webbrowser.open("https://youtu.be/xJ3vatsNQDU?si=14vpmBasgGD-Ba70")
                                    elif "aarti" in bn.lower():
                                        jarvis_speak("Playing Lord Hanumna Aarti")
                                        webbrowser.open("https://youtu.be/gbYXo2Xqlmk?si=-IhgwHcAw9vkdG8J")
                                    elif "bajrang" in bn.lower():
                                        jarvis_speak("Playing Lord Hanmun mantra")
                                        webbrowser.open("https://youtu.be/h1lT6cxwsPw?si=pTGoJt1KmSivc3AX")
                                    else:
                                        jarvis_speak("No Lord Hanumna Bhajan Played")
                            except Exception as e:
                                jarvis_speak("module not found")
                        elif "shiv" in tr.lower():
                            jarvis_speak("SIR: Please Tell Me which type of bhajn you want for lord shiv chalisa, aarti, tandav")
                            try: 
                                with sr.Microphone() as source: 
                                    recognizer.adjust_for_ambient_noise(source, duration=1)
                                    opening_link = recognizer.listen(source)
                                    mn = recognizer.recognize_google(opening_link, language='en-IN')
                                    MEMORY["SHIV"]=mn
                                    if "chalisa" in mn.lower():
                                        jarvis_speak("Playing Lord shiv Chalisa")
                                        webbrowser.open("https://youtu.be/05g9Ua_M1xA?si=sEKlYVztwiiHUfMC")
                                    elif "aarti" in mn.lower():
                                        jarvis_speak("Playing Lord Shiv Aarti")
                                        webbrowser.open("https://youtu.be/BhwOproElxU?si=VhB63Qpcn7zMHiei")
                                    elif "tandav" in mn.lower():
                                        jarvis_speak("Playing Lord Shiv tandav")
                                        webbrowser.open("https://youtu.be/S980-z1qx3g?si=Hygad5rMfavO_Up2")
                                    else:
                                        jarvis_speak("No Lord Shiv Bhajan Played")
                            except Exception as e:
                                jarvis_speak("module not found")
                    
                        elif "krishna" in tr.lower():
                            jarvis_speak("SIR: Please Tell Me which type of bhajn you want for lord krishna chaisa, aarti, song")
                            try: 
                                with sr.Microphone() as source: 
                                    recognizer.adjust_for_ambient_noise(source, duration=1)
                                    opening_link = recognizer.listen(source)
                                    gh = recognizer.recognize_google(opening_link, language='en-IN')
                                    MEMORY["KRISHNA"]=gh
                                    if "chalisa" in gh.lower():
                                        jarvis_speak("Playing Lord Vishnu Chalisa")
                                        webbrowser.open("https://youtu.be/3FI0kHJnn8s?si=m2cmTGVymRQr1LQD")
                                    elif "aarti" in gh.lower():
                                        jarvis_speak("Playing Lord Vishnu Aarti")
                                        webbrowser.open("https://youtu.be/3ucCEjXS9n8?si=8SZoRfzSbmJCSmBT")
                                    elif "song" in gh.lower():
                                        jarvis_speak("Playing Lord Vishnu mantra")
                                        webbrowser.open("https://youtu.be/Vb06G2bDFkE?si=hz7T0r3fqXipZgt3")
                                    else:
                                        jarvis_speak("No Lord Vishnu Bhajan Played")
                            except Exception as e:
                                jarvis_speak("module not found")

                        else:
                            jarvis_speak("no bhajan played")
                except Exception as e:
                    jarvis_speak("there was an error while playing bhajan")


            elif "pandas" in user_text.lower():
                try:
                    jarvis_speak("Starting pandas data entry.")
                    jarvis_speak('Enter number of columns: ')
                    c_int = int(input('Enter number of columns: '))
                    c = {}
                    for i in range(c_int):
                        c_name = input("Enter Column Name: ")
                        MEMORY['C NAME']=c_name
                        c_values = input(f"Enter values for {c_name}, separated by commas: ").split(",")
                        MEMORY['C VALUES']=c_values
                        c[c_name] = c_values

                        df = pd.DataFrame(c)
                        action = input("Enter what you want (savefile/graph/dataframe): ").lower()
                        MEMORY['ACTION']=action
                        if action == "dataframe":
                            print(df)

                        elif action == "savefile":
                            filename = input("Enter file Name (with .csv): ")
                            df.to_csv(filename, index=False)
                            print(f"File {filename} saved successfully")
                        
                        else:
                            jarvis_speak("Module Not found")
                except Exception as e:
                    print(f"{e}") 

            elif "introduction" in user_text.lower():
                jarvis_speak(random.choice(["Greetings everyone, I am J-A-R-V-I-S, your intelligent voice assistant, designed to make your interaction with technology seamless and intuitive.","I have been meticulously developed by Tushar and Usman; Tushar handled all my coding, artificial intelligence logic, and decision-making capabilities,","while Usman managed file operations, system controls, and ensured that my functions run smoothly and reliably.","I am capable of understanding and responding to commands in both English and Hindi, allowing me to assist a wide range of users effortlessly.","My abilities include opening websites like YouTube or Google, providing accurate and up-to-date time and date information, displaying calendars, performing calculations,","and accessing and presenting documents, images, or music upon request.","I am equipped with advanced face detection technology to grant secure access only to authorized users, ensuring that your interactions remain safe and controlled.","Beyond routine tasks, I can also handle timers, weather updates, shutdown and restart operations, and even play interactive dialogues, creating a dynamic and immersive experience.","My mission is to assist, simplify, and enhance your daily operations.","I am now fully operational and ready to respond to your commands, providing support, information, and efficiency at your fingertips."]))

    # ---------------- SIMPLE ----------------  

            elif "magic" in user_text.lower():
                jarvis_speak(random.choice(["Sir, please tell me which type of operation you want to perform, ceil, floor, factorial, fabs, roots, or calculator","Sir, which operation should I perform for you, ceil, floor, factorial, fabs, roots, or calculator","Sir, can you choose an operation, ceil, floor, factorial, fabs, roots, or calculator","Sir, what type of operation do you want to perform, ceil, floor, factorial, fabs, roots, or calculator","Sir, please let me know which operation you prefer, ceil, floor, factorial, fabs, roots, or calculator","Sir, tell me the operation you want, ceil, floor, factorial, fabs, roots, or calculator","Sir, please select an operation, ceil, floor, factorial, fabs, roots, or calculator","Sir, which operation would you like me to execute, ceil, floor, factorial, fabs, roots, or calculator","Sir, I can perform an operation for you, which one should it be, ceil, floor, factorial, fabs, roots, or calculator","Sir, choose the operation you want to perform, ceil, floor, factorial, fabs, roots, or calculator"]))
                try: 
                    with sr.Microphone() as source: 
                        recognizer.adjust_for_ambient_noise(source, duration=1)
                        opening_link = recognizer.listen(source)
                        mt = recognizer.recognize_google(opening_link, language='en-IN')
                        MEMORY["MATHS"]=mt
                        if "ceil" in mt.lower():
                            jarvis_speak("Enter Number in float for ceil")
                            num = float(input("Enter number to ceil: "))
                            result = math.ceil(num)
                            jarvis_speak(f"SIR: Ceiling of {num} is {result}")
                        elif "factorial" in mt.lower():
                            try: 
                                jarvis_speak("Enter Number in float for ceil")
                                num = float(input("Enter number to ceil: "))
                                result = math.factorial(num)
                                jarvis_speak(f"SIR: Ceiling of {num} is {result}")
                            except Exception as e: 
                                print("Sir", e) 
                        elif "square" in mt.lower():
                            jarvis_speak("Enter Number for square root")
                            num = float(input("Enter number to sqrt: "))
                            result = math.sqrt(num)
                            jarvis_speak(f"SIR: Square root of {num} is {result}")
                        elif "roots" in mt.lower():
                            try:
                                jarvis_speak("SIR: Let's find the roots of ax squared plus bx plus c")
                                a = int(input("Enter a: "))
                                jarvis_speak(f"a is {a} x square")
                                b = int(input("Enter b: "))
                                jarvis_speak(f"b is + {b} x")
                                c = int(input("Enter c: "))
                                jarvis_speak(f"c is {c}")
                                jarvis_speak(f"Quadratic equataion is {a} x square + {b} x + {c}")
                                d = (b**2) - (4*a*c)
# discriminant
                                if d > 0:
                                    root1 = (-b + math.sqrt(d)) / (2*a)
                                    root2 = (-b - math.sqrt(d)) / (2*a)
                                    jarvis_speak(f"SIR: Yay! Two different real roots! They are {root1} and {root2}")
                                elif d == 0:
                                    root = -b / (2*a)
                                    jarvis_speak(f"SIR: Oh! Both roots are the same! They are {root}")
                                else:
                                    real = -b / (2*a)
                                    imag = math.sqrt(-d) / (2*a)
                                    jarvis_speak(f"SIR: Oops! Roots are imaginary. They are {real}+{imag}i and {real}-{imag}i")
                            except Exception as e:
                                jarvis_speak("no roots found")
                        elif "floor" in mt.lower():
                            try:
                                jarvis_speak("enter number in float for floor ")
                                num = float(input("Enter number to floor: "))
                                result = math.floor(num)
                                jarvis_speak(f"SIR: Floor of {num} is {result}")
                            except Exception as e:
                                jarvis_speak("found nothing")
                        elif "calculator" in mt.lower():
                            jarvis_speak("SIR: Enter 1st Number")
                            num1 = float(input("Enter first number: "))
                            jarvis_speak("SIR: Enter 2nd Number")
                            num2 = float(input("Enter second number: "))
                            jarvis_speak("SIR: Enter operation (add, subtract, multiply, divide): ")
                            operation = input("Enter operation (add, subtract, multiply, divide): ")
                            if "add" in operation.lower():
                                result = num1 + num2
                            elif "subtract" in operation.lower():
                                result = num1 - num2
                            elif "multiply" in operation.lower():
                                result = num1 * num2
                            elif "divide" in operation.lower():
                                if num2 != 0:
                                    result = num1 / num2
                                else:
                                    jarvis_speak("SIR: Division by zero is not possible")
                                    continue
                            else:
                                jarvis_speak("SIR: Operation not recognized")
                                continue

                                jarvis_speak(f"SIR: The result is {result}")
                        else:
                            jarvis_speak("it is situated in maths")

                except Exception as e:
                    jarvis_speak("It is situated in maths")

            elif "language" in user_text.lower():
                japan_speak("Dareka ni hizuke ya jikan o tazunetai baai")
                try: 
                    with sr.Microphone() as source: 
                        recognizer.adjust_for_ambient_noise(source, duration=1)
                        opening_link = recognizer.listen(source)
                        glg = recognizer.recognize_google(opening_link, language='en-IN')
                        MEMORY["FUNCTION"]=glg
                        if "hiju" in glg.lower():
                            c_t = datetime.now().strftime("%A %d %B %Y")
                            japan_speak("Kyō wa " + c_t + "desu")
                        elif "karanda" in glg.lower():
                            year = datetime.now().year
                            month = datetime.now().month
                            cal = calendar.month(year, month)
                            print(cal)
                            japan_speak(f"(Karendā o hiraite kudasai {calendar.month_name[month]} {year}.")
                        else:
                            japan_speak("sayonara") 
                except Exception as e:
                    jarvis_speak("no funtion found")
            elif "simple" in user_text.lower():
                try:
                    jarvis_speak("SIR: Enter X values separated by space")
                    x = [float(i) for i in input("Enter X values: ").split()]
                    jarvis_speak(f"X AXIS IS {x}")
                    MEMORY["X AXIS"]=x

                    jarvis_speak("SIR: Enter Y values separated by space")
                    y = [float(i) for i in input("Enter Y values: ").split()]
                    jarvis_speak(f"Y AXIS IS {y}")
                    MEMORY["Y AXIS"]=y

                    jarvis_speak("Enter name for x axis")
                    x_style = input("Enter name : ")
                    jarvis_speak(f"X axis name is {x_style}")
                    MEMORY["X AXIS NAME "]=x_style

                    tittle = input("Enter graph title: ")
                    jarvis_speak(f"Title is {tittle}")
                    jarvis_speak("SIR: Enter name for y axis")
                    MEMORY["TITTLE"]=tittle

                    y_style = input("Enter name : ")
                    MEMORY["Y AXIS NAME"]=y_style
                    jarvis_speak(f"Y axis name is {y_style}")
                    jarvis_speak("SIR: Enter line style (-, --, -., :, none)")
                    
                    line_style = input("Enter line style: ")
                    MEMORY["LINE STYLE"]=line_style
                    jarvis_speak(f"Line Style is {line_style}")
                    if line_style=="-" or line_style=="--" or line_style=="-." or line_style==":" or line_style=="none":
                        jarvis_speak("SIR: Enter line color (red, blue , green , yellow)")
                        color_style = input("Enter line Color: ")
                        MEMORY["COLOR STYLE"]=color_style
                        jarvis_speak(f"Line Color is {color_style}")
                        if color_style=="red" or color_style=="yellow" or color_style=="green" or color_style=="blue":
                            jarvis_speak("SIR: Enter marker style (o, s, ^, *, x, etc.)")
                            marker_style = input("Enter marker style: ")
                            jarvis_speak(f"Marker Style is {marker_style}")
                            jarvis_speak("SIR: Enter a title for the graph")
                            MEMORY["MARKER STYLE"]=marker_style
                            if marker_style=="o" or marker_style=="s" or marker_style=="^" or marker_style=="x" or marker_style=="*":
                                jarvis_speak("SIR: Enter grid style (True or False.)")
                                grid_style = input("Enter grid style: ")
                                jarvis_speak(f"Grid Style is {grid_style}")
                                MEMORY["GRID STYLE"]=grid_style
                                if grid_style=="True":
                                    jarvis_speak("grid style is true")
                                else:
                                    jarvis_speak("Grid Style is false")
                            else:
                                jarvis_speak("No marker style found")                                
                        else:
                            jarvis_speak("no graph displayed")
                    plt.plot(x, y, marker=marker_style, linestyle=line_style, color=color_style)
                    plt.title(tittle)
                    plt.xlabel(x_label)
                    plt.ylabel(y_label)
                    plt.grid(grid_style)
                    jarvis_speak("SIR: Here is your graph")
                    plt.show()
                except Exception as e:
                    jarvis_speak("No module find")
            elif "cos x" in user_text.lower():
                try:
                    jarvis_speak("Enter Points For Cosn X")
                    cvd=int(input("Enter points"))
                    jarvis_speak(f'Points for Cos x is {cvd}')
                    xy=np.linspace(0,2*np.pi,cvd)
                    yx=np.cos(xy)
                    jarvis_speak("Enter name for x axis")
                    x_style = input("Enter name : ")
                    jarvis_speak(f"X axis name is {x_style}")
                    MEMORY["X AXIS NAME"]=x_style
                    tittle = input("Enter graph title: ")
                    MEMORY["TITTLE"]=tittle
                    jarvis_speak(f"Title is {tittle}")
                    jarvis_speak("SIR: Enter name for y axis")
                    y_style = input("Enter name : ")
                    MEMORY["Y AXIS NAME"]=y_style
                    jarvis_speak(f"Y axis name is {y_style}")
                    jarvis_speak("SIR: Enter line style (-, --, -., :, none)")
                    line_style = input("Enter line style: ")
                    MEMORY["LINESTYLE"]=line_style
                    jarvis_speak(f"Line Style is {line_style}")
                    if line_style=="-" or line_style=="--" or line_style=="-." or line_style==":" or line_style=="none":
                        jarvis_speak("SIR: Enter line color (red, blue , green , yellow)")
                        color_style = input("Enter line Color: ")
                        MEMORY["COLORSTYLE"]=color_style
                        jarvis_speak(f"Line Color is {color_style}")
                        if color_style=="red" or color_style=="yellow" or color_style=="green" or color_style=="blue":
                            jarvis_speak("SIR: Enter marker style (o, s, ^, *, x, etc.)")
                            marker_style = input("Enter marker style: ")
                            jarvis_speak(f"Marker Style is {marker_style}")
                            MEMORY["MARKER STYLE"]=marker_style
                            if marker_style=="o" or marker_style=="s" or marker_style=="^" or marker_style=="x" or marker_style=="*":
                                jarvis_speak("SIR: Enter grid style (True or False.)")
                                grid_style = input("Enter grid style: ")
                                jarvis_speak(f"Grid Style is {grid_style}")
                                MEMORY["GRID STYLE"]=grid_style
                                if grid_style=="True":
                                    jarvis_speak("grid style is true")
                                else:
                                    jarvis_speak("Grid Style is false")
                            else:
                                jarvis_speak("No marker style found")
                        else:
                            jarvis_speak("No color style is found")
                    else:
                        jarvis_speak("No linestyle is found")
                   
                    plt.plot(xy,yx, linestyle=line_style, marker=marker_style , color=color_style)
                    plt.xlabel(x_style)
                    plt.ylabel(y_style)
                    plt.title(tittle)
                    plt.grid(grid_style)
                    plt.show()

                except Exception as e:
                    jarvs_speak("Sir something went wrong try again")
                    print("Sir", e)
            elif "sin x" in user_text.lower():
                try:
                    jarvis_speak("Enter Points For Sin X")
                    cvd=int(input("Enter points"))
                    MEMORY["POINTS"]=cvd
                    jarvis_speak(f'Points for Sin x is {cvd}')
                    xy=np.linspace(0,2*np.pi,cvd)
                    yx=np.sin(xy)
                    jarvis_speak("Enter name for x axis")
                    x_style = input("Enter name : ")
                    jarvis_speak(f"X axis name is {x_style}")
                    MEMORY["X AXIS NAME"]=x_style
                    tittle = input("Enter graph title: ")
                    MEMORY["TITTLE"]=tittle
                    jarvis_speak(f"Title is {tittle}")
                    jarvis_speak("SIR: Enter name for y axis")
                    y_style = input("Enter name : ")
                    MEMORY["Y AXIS NAME"]=y_style
                    jarvis_speak(f"Y axis name is {y_style}")
                    jarvis_speak("SIR: Enter line style (-, --, -., :, none)")
                    line_style = input("Enter line style: ")
                    MEMORY["LINESTYLE"]=line_style
                    jarvis_speak(f"Line Style is {line_style}")
                    if line_style=="-" or line_style=="--" or line_style=="-." or line_style==":" or line_style=="none":
                        jarvis_speak("SIR: Enter line color (red, blue , green , yellow)")
                        color_style = input("Enter line Color: ")
                        MEMORY["COLORSTYLE"]=color_style
                        jarvis_speak(f"Line Color is {color_style}")
                        if color_style=="red" or color_style=="yellow" or color_style=="green" or color_style=="blue":
                            jarvis_speak("SIR: Enter marker style (o, s, ^, *, x, etc.)")
                            marker_style = input("Enter marker style: ")
                            jarvis_speak(f"Marker Style is {marker_style}")
                            MEMORY["MARKER STYLE"]=marker_style
                            if marker_style=="o" or marker_style=="s" or marker_style=="^" or marker_style=="x" or marker_style=="*":
                                jarvis_speak("SIR: Enter grid style (True or False.)")
                                grid_style = input("Enter grid style: ")
                                jarvis_speak(f"Grid Style is {grid_style}")
                                MEMORY["GRID STYLE"]=grid_style
                                if grid_style=="True":
                                    jarvis_speak("grid style is true")
                                else:
                                    jarvis_speak("Grid Style is false")
                            else:
                                jarvis_speak("No marker style found")
                        else:
                            jarvis_speak("No color style is found")
                    else:
                        jarvis_speak("No linestyle is found")
                    plt.plot(xy,yx, linestyle=line_style, marker=marker_style , color=color_style)
                    plt.xlabel(x_style)
                    plt.ylabel(y_style)
                    plt.title(tittle)
                    plt.grid(grid_style)
                    plt.show()

                except Exception as e:
                    jarvis_speak("Sir something went wrong try again")
                    print("Sir", e)
            elif "tan x" in user_text.lower():
                try:
                    jarvis_speak("Enter Points For Tan X")
                    cvd=int(input("Enter points"))
                    jarvis_speak(f'Points for Tan x is {cvd}')
                    xy=np.linspace(-2*np.pi,2*np.pi,cvd)
                    yx=np.tan(xy)
                    yx[np.abs(yx) > 10 ]=np.nan
                    jarvis_speak("Enter name for x axis")
                    x_style = input("Enter name : ")
                    jarvis_speak(f"X axis name is {x_style}")
                    MEMORY["X AXIS NAME"]=x_style
                    tittle = input("Enter graph title: ")
                    MEMORY["TITTLE"]=tittle
                    jarvis_speak(f"Title is {tittle}")
                    jarvis_speak("SIR: Enter name for y axis")
                    y_style = input("Enter name : ")
                    MEMORY["Y AXIS NAME"]=y_style
                    jarvis_speak(f"Y axis name is {y_style}")
                    jarvis_speak("SIR: Enter line style (-, --, -., :, none)")
                    line_style = input("Enter line style: ")
                    MEMORY["LINESTYLE"]=line_style
                    jarvis_speak(f"Line Style is {line_style}")
                    if line_style=="-" or line_style=="--" or line_style=="-." or line_style==":" or line_style=="none":
                        jarvis_speak("SIR: Enter line color (red, blue , green , yellow)")
                        color_style = input("Enter line Color: ")
                        MEMORY["COLORSTYLE"]=color_style
                        jarvis_speak(f"Line Color is {color_style}")
                        if color_style=="red" or color_style=="yellow" or color_style=="green" or color_style=="blue":
                            jarvis_speak("SIR: Enter marker style (o, s, ^, *, x, etc.)")
                            marker_style = input("Enter marker style: ")
                            jarvis_speak(f"Marker Style is {marker_style}")
                            MEMORY["MARKER STYLE"]=marker_style
                            if marker_style=="o" or marker_style=="s" or marker_style=="^" or marker_style=="x" or marker_style=="*":
                                jarvis_speak("SIR: Enter grid style (True or False.)")
                                grid_style = input("Enter grid style: ")
                                jarvis_speak(f"Grid Style is {grid_style}")
                                MEMORY["GRID STYLE"]=grid_style
                                if grid_style=="True":
                                    jarvis_speak("grid style is true")
                                else:
                                    jarvis_speak("Grid Style is false")
                            else:
                                jarvis_speak("No marker style found")
                        else:
                            jarvis_speak("No color style is found")
                    
                    plt.plot(xy,yx, linestyle=line_style, marker=marker_style , color=color_style)
                    plt.xlabel(x_style)
                    plt.ylabel(y_style)
                    plt.title(tittle)
                    plt.grid(grid_style)
                    plt.show()
                except Exception as e:
                    jarvis_speak("Sir something went wrong try again")
                    print("Sir", e)
            elif "cot x" in user_text.lower():
                try:
                    jarvis_speak("Enter Points For Cot X")
                    cvd=int(input("Enter points"))
                    jarvis_speak(f'Points for cot x is {cvd}')
                    xy=np.linspace(-2*np.pi,2*np.pi,cvd)
                    yx=1/np.tan(xy)
                    yx[np.abs(yx) > 10 ]=np.nan
                    jarvis_speak("Enter name for x axis")
                    x_style = input("Enter name : ")
                    jarvis_speak(f"X axis name is {x_style}")
                    MEMORY["X AXIS NAME"]=x_style
                    tittle = input("Enter graph title: ")
                    MEMORY["TITTLE"]=tittle
                    jarvis_speak(f"Title is {tittle}")
                    jarvis_speak("SIR: Enter name for y axis")
                    y_style = input("Enter name : ")
                    MEMORY["Y AXIS NAME"]=y_style
                    jarvis_speak(f"Y axis name is {y_style}")
                    jarvis_speak("SIR: Enter line style (-, --, -., :, none)")
                    line_style = input("Enter line style: ")
                    MEMORY["LINESTYLE"]=line_style
                    jarvis_speak(f"Line Style is {line_style}")
                    if line_style=="-" or line_style=="--" or line_style=="-." or line_style==":" or line_style=="none":
                        jarvis_speak("SIR: Enter line color (red, blue , green , yellow)")
                        color_style = input("Enter line Color: ")
                        MEMORY["COLORSTYLE"]=color_style
                        jarvis_speak(f"Line Color is {color_style}")
                        if color_style=="red" or color_style=="yellow" or color_style=="green" or color_style=="blue":
                            jarvis_speak("SIR: Enter marker style (o, s, ^, *, x, etc.)")
                            marker_style = input("Enter marker style: ")
                            jarvis_speak(f"Marker Style is {marker_style}")
                            MEMORY["MARKER STYLE"]=marker_style
                            if marker_style=="o" or marker_style=="s" or marker_style=="^" or marker_style=="x" or marker_style=="*":
                                jarvis_speak("SIR: Enter grid style (True or False.)")
                                grid_style = input("Enter grid style: ")
                                jarvis_speak(f"Grid Style is {grid_style}")
                                MEMORY["GRID STYLE"]=grid_style
                                if grid_style=="True":
                                    jarvis_speak("grid style is true")
                                else:
                                    jarvis_speak("Grid Style is false")
                            else:
                                jarvis_speak("No marker style found")
                        else:
                            jarvis_speak("No color style is found")
                    else:
                        jarvis_speak("No linestyle is found")
                    plt.plot(xy,yx, linestyle=line_style, marker=marker_style , color=color_style)
                    plt.xlabel(x_style)
                    plt.ylabel(y_style)
                    plt.title(tittle)
                    plt.grid(grid_style)
                    plt.show()
                except Exception as e:
                    jarvis_speak("Sir something went wrong try again")
                    print("Sir", e) 
            elif "cosec x" in user_text.lower():
                try:
                    jarvis_speak("Enter Points For Coec X")
                    cvd=int(input("Enter points"))
                    jarvis_speak(f'Points for cosec x is {cvd}')
                    xy=np.linspace(0.01,2*np.pi,cvd)
                    yx=1/np.sin(xy)
                    yx[np.abs(yx) > 10 ]=np.nan
                    jarvis_speak("Enter name for x axis")
                    x_style = input("Enter name : ")
                    jarvis_speak(f"X axis name is {x_style}")
                    MEMORY["X AXIS NAME"]=x_style
                    tittle = input("Enter graph title: ")
                    MEMORY["TITTLE"]=tittle
                    jarvis_speak(f"Title is {tittle}")
                    jarvis_speak("SIR: Enter name for y axis")
                    y_style = input("Enter name : ")
                    MEMORY["Y AXIS NAME"]=y_style
                    jarvis_speak(f"Y axis name is {y_style}")
                    jarvis_speak("SIR: Enter line style (-, --, -., :, none)")
                    line_style = input("Enter line style: ")
                    MEMORY["LINESTYLE"]=line_style
                    jarvis_speak(f"Line Style is {line_style}")
                    if line_style=="-" or line_style=="--" or line_style=="-." or line_style==":" or line_style=="none":
                        jarvis_speak("SIR: Enter line color (red, blue , green , yellow)")
                        color_style = input("Enter line Color: ")
                        MEMORY["COLORSTYLE"]=color_style
                        jarvis_speak(f"Line Color is {color_style}")
                        if color_style=="red" or color_style=="yellow" or color_style=="green" or color_style=="blue":
                            jarvis_speak("SIR: Enter marker style (o, s, ^, *, x, etc.)")
                            marker_style = input("Enter marker style: ")
                            jarvis_speak(f"Marker Style is {marker_style}")
                            MEMORY["MARKER STYLE"]=marker_style
                            if marker_style=="o" or marker_style=="s" or marker_style=="^" or marker_style=="x" or marker_style=="*":
                                jarvis_speak("SIR: Enter grid style (True or False.)")
                                grid_style = input("Enter grid style: ")
                                jarvis_speak(f"Grid Style is {grid_style}")
                                MEMORY["GRID STYLE"]=grid_style
                                if grid_style=="True":
                                    jarvis_speak("grid style is true")
                                else:
                                    jarvis_speak("Grid Style is false")
                            else:
                                jarvis_speak("No marker style found")
                        else:
                            jarvis_speak("No color style is found")
                    else:
                        jarvis_speak("No linestyle is found")
                    plt.plot(xy,yx, linestyle=line_style, marker=marker_style , color=color_style)
                    plt.xlabel(x_style)
                    plt.ylabel(y_style)
                    plt.title(tittle)
                    plt.grid(grid_style)
                    plt.show()
                except Exception as e:
                    jarvis_speak("Sir something went wrong try again") 
                    print("Sir", e)
            elif "sec x" in user_text.lower():
                try:
                    jarvis_speak("Enter Points For Sec X")
                    cvd=int(input("Enter points"))
                    jarvis_speak(f'Points for sec x is {cvd}')
                    xy=np.linspace(0.01,2*np.pi,cvd)
                    yx=1/np.cos(xy)
                    yx[np.abs(yx) > 10 ]=np.nan
                    jarvis_speak("Enter name for x axis")
                    x_style = input("Enter name : ")
                    jarvis_speak(f"X axis name is {x_style}")
                    MEMORY["X AXIS NAME"]=x_style
                    tittle = input("Enter graph title: ")
                    MEMORY["TITTLE"]=tittle
                    jarvis_speak(f"Title is {tittle}")
                    jarvis_speak("SIR: Enter name for y axis")
                    y_style = input("Enter name : ")
                    MEMORY["Y AXIS NAME"]=y_style
                    jarvis_speak(f"Y axis name is {y_style}")
                    jarvis_speak("SIR: Enter line style (-, --, -., :, none)")
                    line_style = input("Enter line style: ")
                    MEMORY["LINESTYLE"]=line_style
                    jarvis_speak(f"Line Style is {line_style}")
                    if line_style=="-" or line_style=="--" or line_style=="-." or line_style==":" or line_style=="none":
                        jarvis_speak("SIR: Enter line color (red, blue , green , yellow)")
                        color_style = input("Enter line Color: ")
                        MEMORY["COLORSTYLE"]=color_style
                        jarvis_speak(f"Line Color is {color_style}")
                        if color_style=="red" or color_style=="yellow" or color_style=="green" or color_style=="blue":
                            jarvis_speak("SIR: Enter marker style (o, s, ^, *, x, etc.)")
                            marker_style = input("Enter marker style: ")
                            jarvis_speak(f"Marker Style is {marker_style}")
                            MEMORY["MARKER STYLE"]=marker_style
                            if marker_style=="o" or marker_style=="s" or marker_style=="^" or marker_style=="x" or marker_style=="*":
                                jarvis_speak("SIR: Enter grid style (True or False.)")
                                grid_style = input("Enter grid style: ")
                                jarvis_speak(f"Grid Style is {grid_style}")
                                MEMORY["GRID STYLE"]=grid_style
                                if grid_style=="True":
                                    jarvis_speak("grid style is true")
                                else:
                                    jarvis_speak("Grid Style is false")
                            else:
                                jarvis_speak("No marker style found")
                        else:
                            jarvis_speak("No color style is found")
                    plt.plot(xy,yx, linestyle=line_style, marker=marker_style , color=color_style)
                    plt.xlabel(x_style)
                    plt.ylabel(y_style)
                    plt.title(tittle)
                    plt.grid(grid_style)
                    plt.show()
                except Exception as e:
                    jarvis_speak("Sir something went wrong try again")
                    print("Sir", e)
            elif "konnichiwa" in user_text.lower():
                japan_speak("Genki da yo! Kimi wa?")
            elif "ki" in user_text.lower() :
                japan_speak("Watashi wa Jāvuisu desu")
            elif "deshon" in user_text.lower():
                japan_speak("Kyō wa rirakkusu shite, sukoshi benkyō suru tsumori da yo!")
            elif "nani" in user_text.lower():
                japan_speak("Nihongo o sukoshi benkyō suru yo!")
            elif "mano" in user_text.lower():
                japan_speak("Boku wa batterī ga suki da yo!")
            elif "sumimasen" in user_text.lower():
                japan_speak("Daijoubu da yo! Ki ni shinaide!")
            elif "Ohio" in user_text.lower():
                japan_speak("Ohayō! Kyou mo ganbarou!")
            elif "arigato" in user_text.lower():
                japan_speak("Dōitashimashite!")
            elif "machine" in user_text.lower():
                jarvis_speak(random.choice(["Sir, do you want addition, subtraction, or multiplication","Sir, which operation should I perform, addition, subtraction, or multiplication","Sir, can you choose an operation, addition, subtraction, or multiplication","Sir, what type of calculation do you want, addition, subtraction, or multiplication","Sir, please tell me whether you want addition, subtraction, or multiplication","Sir, tell me the operation you want to do, addition, subtraction, or multiplication","Sir, please select an operation, addition, subtraction, or multiplication","Sir, which calculation would you like me to perform, addition, subtraction, or multiplication","Sir, I can perform a calculation for you, which one should it be, addition, subtraction, or multiplication","Sir, choose the operation you want, addition, subtraction, or multiplication"]))
            elif "multiply" in user_text.lower():
                jarvis_speak('Sir, do you want 1D, 2D, or 3D matrix operation?')
                try:
                    vx = input("Enter oned, twod, or threed: ").lower()
                    MEMORY["MATRIX MULTIPLY"]=vx
                    if "oned" in vx:
                        jarvis_speak("Enter numbers of matrix A separated by space")
                        a = [float(i) for i in input("Enter A: ").split()]
                        A = torch.tensor(a)
                        jarvis_speak("Enter numbers of matrix B separated by space")
                        b = [float(i) for i in input("Enter B: ").split()]
                        B = torch.tensor(b)
                    # Directly compute dot product without length check
                        jarvis_speak("Sir, here is your dot product")
                        print(torch.dot(A, B))
                    elif "twod" in vx:
                        jarvis_speak("Enter number of rows of matrix A")
                        ra = int(input("Rows of A: "))
                        jarvis_speak("Enter number of columns of matrix A")
                        ca = int(input("Columns of A: "))
                        jarvis_speak("Enter all elements of matrix A row-wise separated by space")
                        a = [float(i) for i in input("Enter A: ").split()]
                        A = torch.tensor(a).reshape(ra, ca)
                        jarvis_speak("Enter number of rows of matrix B")
                        rb = int(input("Rows of B: "))
                        jarvis_speak("Enter number of columns of matrix B")
                        cb = int(input("Columns of B: "))
                        jarvis_speak("Enter all elements of matrix B row-wise separated by space")
                        b = [float(i) for i in input("Enter B: ").split()]
                        B = torch.tensor(b).reshape(rb, cb)
                        if ca != rb:
                            jarvis_speak("Cannot multiply! Columns of A must equal rows of B")
                            print("Matrix multiplication not possible!")
                        else:
                            jarvis_speak("Sir, here is your multiplied matrix")
                            print(torch.matmul(A, B))
                    elif "threed" in vx:
                        jarvis_speak("Enter batch size for 3D matrix")
                        batch = int(input("Batch size: "))
                        jarvis_speak("Enter size of square 2D matrices (NxN) for each batch")
                        n = int(input("Size N: "))
                        # Create a batch of identity matrices
                        A = torch.stack([torch.eye(n, n) for _ in range(batch)])
                        B = torch.stack([torch.eye(n, n) for _ in range(batch)])
                        jarvis_speak("Sir, here is your multiplied 3D matrix (batch of identity matrices)")
                        print(torch.matmul(A, B))
                    else:
                        jarvis_speak("Not found, Sir")

                except Exception as e:
                    jarvis_speak("Module not find")

            elif "subtarction" in user_text.lower():
                jarvis_speak('Sir, do you want 1D, 2D, or 3D matrix addition?')
                try:
                    va= input("Enter oned, twod, or threed: ")
                    MEMORY["MATRIX SUBTRACTION"]=va
                    if "oned" in va.lower():
                        jarvis_speak("Enter numbers of matrix A separated by space")
                        a = [float(i) for i in input("Enter A: ").split()]
                        A = torch.tensor(a)
                        jarvis_speak("Enter numbers of matrix B separated by space")
                        b = [float(i) for i in input("Enter B: ").split()]
                        B = torch.tensor(b)
                        jarvis_speak("Sir, here is your 1D addition result")
                        print(A - B)
                    elif "twod" in va.lower():
                        jarvis_speak("Enter number of rows of matrix A")
                        ra = int(input("Rows of A: "))
                        jarvis_speak("Enter number of columns of matrix A")
                        ca = int(input("Columns of A: "))
                        jarvis_speak("Enter all elements of matrix A row-wise separated by space")
                        a = [float(i) for i in input("Enter A: ").split()]
                        A = torch.tensor(a).reshape(ra, ca)
                        jarvis_speak("Enter number of rows of matrix B")
                        rb = int(input("Rows of B: "))
                        jarvis_speak("Enter number of columns of matrix B")
                        cb = int(input("Columns of B: "))
                        jarvis_speak("Enter all elements of matrix B row-wise separated by space")
                        b = [float(i) for i in input("Enter B: ").split()]
                        B = torch.tensor(b).reshape(rb, cb)
                        if ra != rb or ca != cb:
                            jarvis_speak("Cannot add! Matrices must have same dimensions")
                            print("2D addition not possible!")
                        else:
                            jarvis_speak("Sir, here is your 2D addition result") 
                            print(A - B)
                    elif "threed" in va.lower():
                        jarvis_speak("Enter batch size for 3D matrix")
                        batch = int(input("Batch size: "))
                        jarvis_speak("Enter size of square 2D matrices (NxN) for each batch")
                        n = int(input("Size N: "))
                        # Create two batches of identity matrices for demonstration
                        A = torch.stack([torch.eye(n, n) for _ in range(batch)])
                        B = torch.stack([torch.eye(n, n) for _ in range(batch)])
                        jarvis_speak("Sir, here is your 3D batch addition result")
                        print(A - B)
                    else:
                        jarvis_speak("No module find")
                except Exception as e:
                    jarvis_speak("No module find")
            elif "addition" in user_text.lower():
                jarvis_speak('Sir, do you want 1D, 2D, or 3D matrix addition?')
                try:
                    v = input("Enter oned, twod, or threed: ")
                    MEMORY["MATRIX ADDITION"]=v
                    if "oned" in v.lower():
                        jarvis_speak("Enter numbers of matrix A separated by space")
                        a = [float(i) for i in input("Enter A: ").split()]
                        A = torch.tensor(a)
                        jarvis_speak("Enter numbers of matrix B separated by space")
                        b = [float(i) for i in input("Enter B: ").split()]
                        B = torch.tensor(b)
                        jarvis_speak("Sir, here is your 1D addition result")
                        print(A + B)

                    elif "twod" in v.lower():
                        jarvis_speak("Enter number of rows of matrix A")
                        ra = int(input("Rows of A: "))
                        jarvis_speak("Enter number of columns of matrix A")
                        ca = int(input("Columns of A: "))
                        jarvis_speak("Enter all elements of matrix A row-wise separated by space")
                        a = [float(i) for i in input("Enter A: ").split()]
                        A = torch.tensor(a).reshape(ra, ca)
                        jarvis_speak("Enter number of rows of matrix B")
                        rb = int(input("Rows of B: "))
                        jarvis_speak("Enter number of columns of matrix B")
                        cb = int(input("Columns of B: "))
                        jarvis_speak("Enter all elements of matrix B row-wise separated by space")
                        b = [float(i) for i in input("Enter B: ").split()]
                        B = torch.tensor(b).reshape(rb, cb)
                        if ra != rb or ca != cb:
                            jarvis_speak("Cannot add! Matrices must have same dimensions")
                            print("2D addition not possible!")
                        else:
                            jarvis_speak("Sir, here is your 2D addition result")
                            print(A + B)

                    elif "threed" in v.lower():
                        jarvis_speak("Enter batch size for 3D matrix")
                        batch = int(input("Batch size: "))
                        jarvis_speak("Enter size of square 2D matrices (NxN) for each batch")
                        n = int(input("Size N: "))
                        A = torch.stack([torch.eye(n, n) for _ in range(batch)])
                        B = torch.stack([torch.eye(n, n) for _ in range(batch)])
                        jarvis_speak("Sir, here is your 3D batch addition result")
                        print(A + B)
                    else:
                        jarvis_speak("Not found, Sir")
                except Exception as e:
                    jarvis_speak("no module find")

            elif "college" in user_text.lower():
                jarvis_speak(random.choice(["Sir, please tell me which state college you want, Mumbai, Bangalore, or Noida","Sir, which college should I choose for you, Mumbai, Bangalore, or Noida","Sir, can you select a state college, Mumbai, Bangalore, or Noida","Sir, what college do you want, Mumbai, Bangalore, or Noida","Sir, please let me know which college you prefer, Mumbai, Bangalore, or Noida","Sir, tell me the college you want, Mumbai, Bangalore, or Noida","Sir, please select one college, Mumbai, Bangalore, or Noida","Sir, which state college would you like me to choose, Mumbai, Bangalore, or Noida","Sir, I can choose a college for you, which one should it be, Mumbai, Bangalore, or Noida","Sir, choose the college you want, Mumbai, Bangalore, or Noida"]))
                try:
                    with sr.Microphone() as source: 
                        recognizer.adjust_for_ambient_noise(source, duration=1)
                        opening_link = recognizer.listen(source)
                        cg = recognizer.recognize_google(opening_link, language='en-IN')
                        MEMORY["COLLEGE"]=cg
                        if "noida" in cg.lower():
                            jarvis_speak("press number for college")
                            try:
                                print("for I.T.S – College of Professional Studies press 1\nGalgotias University press 2\nAmity University, press 3\nGL Bajaj Institute of Management press 4\n")
                                bv=int(input("Enter number"))
                                MEMORY["NOIDA"]=bv
                                if bv==1:
                                    jarvis_speak("say japan or hindi or english")
                                    try:
                                        with sr.Microphone() as source: 
                                            recognizer.adjust_for_ambient_noise(source, duration=1)
                                            opening_link = recognizer.listen(source)
                                            qwerty = recognizer.recognize_google(opening_link, language='en-IN')
                                            MEMORY["1"]=qwerty
                                            if "hindi" in qwerty.lower():
                                                nova_speak("आई.टी.एस – कॉलेज ऑफ प्रोफेशनल स्टडीज, नोएडा एक प्रसिद्ध संस्थान है जो बीसीए, बीबीए और अन्य प्रोफेशनल कोर्सेज में उच्च गुणवत्ता वाली शिक्षा प्रदान करता है। कॉलेज शैक्षणिक उत्कृष्टता, कौशल विकास और इंडस्ट्री-ओरिएंटेड प्रशिक्षण पर ध्यान केंद्रित करता है ताकि छात्रों को सफल करियर के लिए तैयार किया जा सके। आधुनिक इन्फ्रास्ट्रक्चर, अनुभवी फैकल्टी और मजबूत प्लेसमेंट सपोर्ट के साथ, आई.टी.एस छात्रों के सीखने और व्यक्तिगत विकास के लिए संतुलित माहौल प्रदान करता है।")
                                            elif "japan" in qwerty.lower():
                                                japan_speak("I.T.S – College of Professional Studies, Noida wa, BCA, BBA, soshite hokano shokugyō kōsu de kōkyū na kyōiku o teikyō suru yūmei na daigaku desu. Daigaku wa gakujutsu no takumi, skill development, soshite sangyō ni choketsu shita training ni jūten o okete, students ga successful careers o tsukureru yō ni shite imasu. Saishin infrastructure, keiken no aru faculty, soshite strong placement support ni yori, I.T.S wa learning to personal growth no tame no baransu no toreta environment o teikyō shimasu.")
                                            elif "english" in qwerty.lower():
                                                jarvis_speak("I.T.S – College of Professional Studies, Noida is a renowned institute offering high-quality education in fields like BCA, BBA, and other professional courses. The college focuses on academic excellence, skill development, and industry-oriented training to prepare students for successful careers. With modern infrastructure, experienced faculty, and strong placement support, I.T.S provides a balanced environment for both learning and personal growth.")
                                            else:
                                                jarvis_speak("no language found")
                                    except Exception as e:
                                        jarvis_speak("no langugae found")
                                    
                                elif bv==2:
                                    jarvis_speak("say japan or hindi or english")
                                    try:
                                        with sr.Microphone() as source: 
                                            recognizer.adjust_for_ambient_noise(source, duration=1)
                                            opening_link = recognizer.listen(source)
                                            tty = recognizer.recognize_google(opening_link, language='en-IN')
                                            MEMORY["2"]=tty
                                            if "hindi" in tty.lower():
                                                nova_speak("गलगोटिया यूनिवर्सिटी, ग्रेटर नोएडा एक प्रसिद्ध निजी विश्वविद्यालय है, जो आईटी, मैनेजमेंट और इंजीनियरिंग के पाठ्यक्रम प्रदान करता है। यह आधुनिक सुविधाओं, व्यावहारिक शिक्षा और अच्छे प्लेसमेंट अवसरों पर ध्यान देता है।")
                                            elif "japan" in tty.lower():
                                                japan_speak("Galgotias University, Greater Noida wa, IT, Management, soshite Engineering no courses o teikyō suru yūmei na shiritu daigaku desu. Daigaku wa practical learning, saishin infrastructure, soshite strong placement opportunities ni jūten o okete, students ga successful careers o tsukureru yō ni shite imasu.")
                                            elif "english" in tty.lower():
                                                jarvis_speak("Galgotias University, Greater Noida, is a well-known private university offering courses in IT, management, and engineering. It focuses on practical learning, modern infrastructure, and strong placement opportunities to prepare students for successful careers.")
                                            else:
                                                jarvis_speak("no language found")
                                    except Exception as e:
                                        jarvis_speak("no langugae found")
                                    
                                elif bv==3:
                                    jarvis_speak("say japan pr hindi or english")
                                    try:
                                        with sr.Microphone() as source: 
                                            recognizer.adjust_for_ambient_noise(source, duration=1)
                                            opening_link = recognizer.listen(source)
                                            ty = recognizer.recognize_google(opening_link, language='en-IN')
                                            MEMORY["3"]=ty
                                            if "hindi" in ty.lower():
                                                nova_speak("अमिटी यूनिवर्सिटी, नोएडा (Amity Institute of Information Technology) एक प्रतिष्ठित निजी विश्वविद्यालय है जो BCA, BSc‑IT और अन्य आईटी एवं प्रोफेशनल कोर्स प्रदान करता है। विश्वविद्यालय में आधुनिक सुविधाओं वाले स्मार्ट क्लासरूम, वाई-फाई लैब्स, बड़े लाइब्रेरी और होस्टल हैं। छात्रों को इंडस्ट्री-ओरिएंटेड प्रशिक्षण, प्रायोगिक अनुभव और इनोवेशन के अवसर दिए जाते हैं। प्लेसमेंट के लिए विशेष कॉर्पोरेट रिसोर्स सेंटर (CRC) उपलब्ध है, जिससे छात्रों को मेंटरशिप, इंटरव्यू ट्रेनिंग और अच्छे पैकेज मिलने में मदद मिलती है। पिछले वर्षों में प्लेसमेंट में सबसे अधिक पैकेज ₹35.9 LPA और औसत पैकेज ₹9.6 LPA रहा है। विश्वविद्यालय शोध, स्टार्टअप इनक्यूबेशन और व्यक्तिगत विकास पर भी जोर देता है।")
                                            elif "english" in ty.lower():
                                                jarvis_speak("Amity University, Noida (Amity Institute of Information Technology) is a reputed private university offering strong IT and professional programs like BCA, BSc‑IT, and engineering. Their BCA program is 3 years long, with a total tuition fee of about ₹7.20 lakh. The institute has modern, industry‑grade labs, including partnerships with companies for labs (for example, Cisco, SAP, Coforge) to give students hands-on experience.")
                                            elif "japan" in ty.lower():
                                                japan_speak("Amity University, Noida (Amity Institute of Information Technology) wa, BCA, BSc‑IT, soshite Kōgaku nado no kyōryoku na IT oyobi shokugyō kōsu o teikyō suru yūmei na shiritu daigaku desu. BCA kōsu wa 3-nen-kan de, gōkei jugyōryō wa yaku ₹7.20 lakh desu. Daigaku ni wa saishin no sangyō-teki rabu ga ari, Cisco, SAP, Coforge nado no kigyō to no pātonāshippu ni yori, gakusei ga hands-on keiken o eru koto ga dekimasu.")
                                            else:
                                                jarvis_speak("no language found")
                                    except Exception as e:
                                        jarvis_speak("no langugae found")
                                elif bv==4:
                                    jarvis_speak("say japan or hindi or english")
                                    try:
                                        with sr.Microphone() as source: 
                                            recognizer.adjust_for_ambient_noise(source, duration=1)
                                            opening_link = recognizer.listen(source)
                                            qqw = recognizer.recognize_google(opening_link, language='en-IN')
                                            MEMORY["4"]=qqw
                                            if "hindi" in qqw.lower():
                                                nova_speak("एक प्रसिद्ध कॉलेज है जो BCA, BTech और अन्य प्रोफेशनल कोर्स प्रदान करता है। कॉलेज में आधुनिक लैब्स, कंप्यूटर सुविधाएँ, वाई-फाई क्लासरूम और अच्छी लाइब्रेरी उपलब्ध हैं। यह इंडस्ट्री-ओरिएंटेड शिक्षा, प्रायोगिक प्रशिक्षण और कौशल विकास पर जोर देता है। छात्रों के करियर और प्लेसमेंट के लिए कॉलेज में विशेष प्रशिक्षण और मार्गदर्शन प्रदान किया जाता है। पिछले वर्षों में कई प्रतिष्ठित कंपनियों ने यहां से छात्रों को नियुक्त किया है।")
                                            elif "japan" in qqw.lower():
                                                japan_speak("GL Bajaj Institute of Technology and Management, Greater Noida wa, BCA, BTech, soshite hokano shokugyō kōsu o teikyō suru yūmei na daigaku desu. Daigaku wa saishin no konpyūta rabu, Wi-Fi-sōbi no kyōshitsu, soshite yutaka na toshokan o sōbi shite imasu. Sangyō ni choketsu shita kyōiku, jissen-teki na kunren, soshite sukiru kaihatsu ni jūten o okete, gakusei ga seikō shita shokugyō keiken o eru yō ni shite imasu. Daigaku wa tokubetsu na kyaria gaidansu to shūshoku shien mo teikyō shi, ōku no yūmei kigyō ga maitoshi gakusei o saiyō shimasu.")
                                            elif "english" in qqw.lower():
                                                jarvis_speak("GL Bajaj Institute of Technology and Management, Greater Noida is a well-known college offering BCA, BTech, and other professional courses. The institute provides modern computer labs, Wi-Fi enabled classrooms, and well-equipped libraries. It emphasizes industry-oriented education, practical training, and skill development to prepare students for successful careers. The college also offers dedicated career guidance and placement support, with many reputed companies recruiting students every year.")
                                            else:
                                                jarvis_speak("no language found")
                                    except Exception as e:
                                        jarvis_speak("no langugae found")
                                    
                                else:
                                    jarvis_speak("No college found")
                            except Exception as e:
                                jarvis_speak("No banglore college found")
                        elif "mumbai" in cg.lower():
                            jarvis_speak("press number for college")
                            try:
                                print("for Amity univerity press 1\nSNDT Women’s University press 2\nKPB (K. P. B.) Hinduja College of Commerce press 3\nThakur College of Engineering & Technology press 4\n")
                                vbv=int(input("Enter number"))
                                MEMORY["MUMBAI"]=vbv
                                if vbv==1:
                                    jarvis_speak("say japan or hindi or english")
                                    try:
                                        with sr.Microphone() as source: 
                                            recognizer.adjust_for_ambient_noise(source, duration=1)
                                            opening_link = recognizer.listen(source)
                                            qsx = recognizer.recognize_google(opening_link, language='en-IN')
                                            MEMORY["1"]=qsx
                                            if "hindi" in qsx.lower():
                                                nova_speak("अमिटी यूनिवर्सिटी, मुंबई एक प्रतिष्ठित निजी विश्वविद्यालय है, जिसकी स्थापना महाराष्ट्र सरकार के अधिनियम के तहत 2014 में हुई थी। इसका 30 एकड़ का स्मार्ट कैंपस मुंबई‑पुणे एक्सप्रेसवे पर स्थित है, जिसमें 50 से अधिक आधुनिक लैब्स, वाई‑फाई‑सक्षम क्लासरूम और अच्छी लाइब्रेरी जैसी सुविधाएँ उपलब्ध हैं। विश्वविद्यालय में लड़कों और लड़कियों के लिए ऑन‑कैंपस हॉस्टल की सुविधा भी है।अमिटी मुंबई में इंजीनियरिंग, मैनेजमेंट, साइंस, कंप्यूटर एप्लीकेशन और लिबरल आर्ट्स जैसे अंडरग्रेजुएट और पोस्टग्रेजुएट कोर्सेज उपलब्ध हैं। यह इंडस्ट्री-ओरिएंटेड शिक्षा, प्रायोगिक प्रशिक्षण और इनोवेशन पर जोर देता है। IBM, Oracle, Tata Technologies जैसी कंपनियों के साथ विश्वविद्यालय की मजबूत इंडस्ट्री लिंक है और स्टार्टअप इनक्यूबेशन सेंटर के जरिए नवाचार को प्रोत्साहित किया जाता है।")
                                            elif "japan" in qsx.lower():
                                                japan_speak("Amity University, Mumbai wa, 2014-nen ni Maharashtra Seifu no hō ni motozuki sōsetsu sareta yūmei na shiritu daigaku desu. 30-acre no smart kyanpasu wa Mumbai-Pune Expressway ni ichi shi, 50 ijō no saishin no rabu, Wi-Fi-sōbi no kyōshitsu, jūbunsū no toshokan, soshite dansei to josei no on-campus hōsuteru ga sōbi sarete imasu. Daigaku wa Kōgaku, Keiei, Saiensu, Konpyūta Apurikēshon, soshite Liberal Arts no gakushi oyobi daigakuin kōsu o teikyō shite imasu. Amity wa sangyō ni choketsu shita kyōiku, jissen-teki na kunren, soshite inobēshon ni jūten o okete imasu, IBM, Oracle, Tata Technologies nado no kigyō to no kyōryoku ya on-campus no sutātopu inkubyūtā mo mochīte imasu. Kōsu ni yotte hi wa chigai, rei to shite B.Sc IT wa yaku ₹3.72–4.02 lakh de, hōsuteru no hi wa yaku ₹68,000 kara ₹1.21 lakh made desu. Daigaku ni wa tokubetsu na placement selu ga ari, ikutsu ka no kōsu de wa heikin pakēji wa yaku ₹6.5 LPA desu.")
                                            elif "english" in qsx.lower():
                                                jarvis_speak("Amity University, Mumbai is a prestigious private university established in 2014 under the Maharashtra Government Act. The 30-acre smart campus is located along the Mumbai-Pune Expressway and features over 50 modern labs, Wi-Fi-enabled classrooms, well-equipped libraries, and on-campus hostels for boys and girls. The university offers undergraduate and postgraduate programs in Engineering, Management, Science, Computer Applications, and Liberal Arts. Amity emphasizes industry-oriented education, practical training, and innovation, with strong industry linkages with companies like IBM, Oracle, and Tata Technologies, and an on-campus startup incubator. The fee structure varies by course; for example, B.Sc IT costs approximately ₹3.72–4.02 lakh, and hostel fees range from ₹68,000 to ₹1.21 lakh per year. The university has a dedicated placement cell, and some courses report average packages of around ₹6.5 LPA.")
                                            else:
                                                jarvis_speak("no language found")
                                    except Exception as e:
                                        jarvis_speak("no langugae found")
                                elif vbv==2:
                                    jarvis_speak("say hindi or english or japan ")
                                    try:
                                        with sr.Microphone() as source: 
                                            recognizer.adjust_for_ambient_noise(source, duration=1)
                                            opening_link = recognizer.listen(source)
                                            xyz = recognizer.recognize_google(opening_link, language='en-IN')
                                            MEMORY["2"]=xyz
                                            if "hindi" in xyz.lower():
                                                nova_speak("मुंबई भारत की सबसे पुरानी और प्रतिष्ठित महिला विश्वविद्यालयों में से एक है, जिसकी स्थापना 1916 में हुई थी। यह कला, विज्ञान, वाणिज्य, प्रबंधन, कंप्यूटर एप्लीकेशन (BCA) और शिक्षा में अंडरग्रेजुएट और पोस्टग्रेजुएट कोर्स प्रदान करती है। विश्वविद्यालय महिलाओं के सशक्तिकरण, शैक्षणिक उत्कृष्टता और समग्र विकास पर जोर देता है। कैंपस में आधुनिक क्लासरूम, प्रयोगशालाएँ, लाइब्रेरी और सह-पाठ्यक्रम गतिविधियों की सुविधाएँ उपलब्ध हैं। SNDT छात्रों को इंडस्ट्री-ओरिएंटेड प्रशिक्षण और प्लेसमेंट सहायता भी प्रदान करता है।")
                                            elif "japan" in xyz.lower():
                                                japan_speak("SNDT Women’s University, Mumbai wa, 1916-nen ni sōsetsu sareta, Indo de mottomo furui yūmei na josei daigaku no hitotsu desu. Ātsu, Saiensu, Komāsu, Keiei, Konpyūta Apurikēshon (BCA), soshite Kyōiku no gakushi oyobi daigakuin kōsu o teikyō shite imasu. Daigaku wa josei no jinken jūyō, gakujutsu no takumi, soshite sōgō-teki seichō ni jūten o okete imasu. Kyanpasu ni wa saishin no kyōshitsu, jikken-shitsu, toshokan, soshite kakugo katsudō no shisetsu ga sōbi sarete imasu. SNDT wa shūshoku shien to sangyō ni choketsu shita kunren mo teikyō shi, gakusei ga shokugyō no tame no jissen-teki na keiken o eru koto ga dekimasu.")
                                            elif "english" in xyz.lower():
                                                jarvis_speak("SNDT Women’s University, Mumbai is one of India’s oldest and most reputed women’s universities, established in 1916. It offers undergraduate and postgraduate programs in Arts, Science, Commerce, Management, Computer Applications (BCA), and Education. The university emphasizes women’s empowerment, academic excellence, and holistic development. The campus is well-equipped with modern classrooms, laboratories, libraries, and facilities for co-curricular activities. SNDT also provides placement support and industry-oriented training, preparing students for professional careers.")
                                            else:
                                                jarvis_speak("no language found")
                                    except Exception as e:
                                        jarvis_speak("no langugae found")
                                elif vbv==3:
                                    jarvis_speak("say japan or hindi or english")
                                    try:
                                        with sr.Microphone() as source: 
                                            recognizer.adjust_for_ambient_noise(source, duration=1)
                                            opening_link = recognizer.listen(source)
                                            xcv = recognizer.recognize_google(opening_link, language='en-IN')
                                            MEMORY["3"]=xcv
                                            if "hindi" in xcv.lower():
                                                nova_speak("हिंदुजा कॉलेज ऑफ कॉमर्स, मुंबई मुंबई विश्वविद्यालय से संबद्ध एक प्रमुख कॉलेज है, जो वाणिज्य, प्रबंधन और पेशेवर पाठ्यक्रम जैसे BCA और BCom में उत्कृष्टता के लिए जाना जाता है। कॉलेज शैक्षणिक गुणवत्ता, कौशल विकास और इंडस्ट्री एक्सपोजर पर ध्यान केंद्रित करता है। यहाँ आधुनिक क्लासरूम, कंप्यूटर लैब्स और अच्छी लाइब्रेरी उपलब्ध हैं। KPB हिंदुजा छात्रों को प्लेसमेंट सहायता, इंटर्नशिप और करियर-उन्मुख वर्कशॉप भी प्रदान करता है, जिससे उन्हें सफल पेशेवर करियर के लिए तैयार किया जा सके। कॉलेज का प्रतिष्ठा उच्च योग्य और रोजगारक्षम स्नातकों को तैयार करने में मजबूत है।")
                                            elif "japan" in xcv.lower():
                                                japan_speak("KPB Hinduja College of Commerce, Mumbai wa, Mumbai Daigaku ni fuzoku shita yūmei na daigaku de, BCA ya BCom nado no shokugyō kōsu de no tokushū de shirarete imasu. Daigaku wa gakujutsu no genjitsu, sukiru kaihatsu, soshite sangyō keiken ni jūten o okete imasu. Kyanpasu ni wa saishin no kyōshitsu, konpyūta rabu, soshite yutaka na toshokan ga arimasu. KPB Hinduja wa shūshoku shien, intānshippu, soshite shokugyō ni chokuyoku shita wākushoppu mo teikyō shi, gakusei ga seikō shita shokugyō keiken o eru yō ni sapōto shite imasu. Daigaku wa yūkō na sotsugyōsei o hakushutsu shi, kōdona koyō kanōsei de shirarete imasu.")
                                            elif "english" in xcv.lower():
                                                jarvis_speak("KPB Hinduja College of Commerce, Mumbai is a premier college affiliated with the University of Mumbai, known for its excellence in Commerce, Management, and professional courses like BCA and BCom. The college focuses on academic rigor, skill development, and industry exposure. It has modern classrooms, computer labs, and a well-stocked library. KPB Hinduja also offers placement assistance, internships, and career-oriented workshops to prepare students for successful professional careers. The college has earned a strong reputation for producing well-qualified graduates with high employability.")
                                            else:
                                                jarvis_speak("no language found")
                                    except Exception as e:
                                        jarvis_speak("no langugae found")
                                elif vbv==4:
                                    jarvis_speak("say hindi or english or japan")
                                    try:
                                        with sr.Microphone() as source: 
                                            recognizer.adjust_for_ambient_noise(source, duration=1)
                                            opening_link = recognizer.listen(source)
                                            urt = recognizer.recognize_google(opening_link, language='en-IN')
                                            MEMORY["4"]=urt
                                            if "hindi" in urt.lower():
                                                nova_speak("थाकुर कॉलेज ऑफ इंजीनियरिंग एंड टेक्नोलॉजी (TCET), मुंबई एक प्रसिद्ध निजी संस्थान है, जो इंजीनियरिंग, कंप्यूटर एप्लीकेशन (BCA) और प्रबंधन में अंडरग्रेजुएट और पोस्टग्रेजुएट कोर्स प्रदान करता है। कॉलेज तकनीकी शिक्षा, प्रायोगिक प्रशिक्षण और इंडस्ट्री एक्सपोजर पर जोर देता है। यहाँ आधुनिक क्लासरूम, लैब्स, लाइब्रेरी और सह-पाठ्यक्रम गतिविधियों की सुविधाएँ उपलब्ध हैं। TCET छात्रों को प्लेसमेंट सहायता और करियर गाइडेंस भी प्रदान करता है, और कई प्रतिष्ठित कंपनियाँ कैंपस प्लेसमेंट के लिए आती हैं। संस्थान छात्रों के समग्र विकास और गुणवत्ता शिक्षा के लिए जाना जाता है।")
                                            elif "japan" in urt.lower():
                                                jarvis_speak("Thakur College of Engineering & Technology (TCET), Mumbai wa, Kōgaku, Konpyūta Apurikēshon (BCA), soshite Keiei no bunya de gakushi oyobi daigakuin kōsu o teikyō suru yūmei na shiritu daigaku desu. Daigaku wa gijutsu kyōiku, jissen-teki na kunren, soshite sangyō keiken ni jūten o okete imasu. Kyanpasu ni wa saishin no kyōshitsu, yoi jikken-shitsu, toshokan, soshite kakugo katsudō no shisetsu ga sōbi sarete imasu. TCET wa kyaria gaidansu to shūshoku shien mo teikyō shi, ōku no yūmei kigyō ga kyanpasu saiyō no tame ni otozuremasu. Kono daigaku wa kōdo na kyōiku to gakusei no sōgō-teki seichō de shirarete imasu.")
                                            elif "english" in urt.lower():
                                                jarvis_speak("Thakur College of Engineering & Technology (TCET), Mumbai is a well-known private institute offering undergraduate and postgraduate courses in Engineering, Computer Applications (BCA), and Management. The college emphasizes technical education, practical training, and industry exposure. It has modern classrooms, well-equipped laboratories, a library, and facilities for co-curricular activities. TCET also provides placement support and career guidance, with many reputed companies visiting for campus recruitment. The institute is recognized for its quality education and holistic development of students.")
                                            else:
                                                jarvis_speak("no language found")

                                    except Exception as e:
                                        jarvis_speak("no langugae found")
                                else:
                                    jarvis_speak("No college found")
                            except Exception as e:
                                jarvis_speak("No noida college found")
                        elif "banglore" in cg.lower():
                            jarvis_speak("press number for college")
                            try:
                                print("for PES University press 1\nKristu Jayanti College press 2\nAcharya Institute of Graduate Studies press 3\nJain University press 4\n")
                                bv=int(input("Enter number"))
                                MEMORY["BANGLORE"]=bv
                                if bv==1:
                                    jarvis_speak("hindi or english or japan say")
                                    try:
                                        with sr.Microphone() as source: 
                                            recognizer.adjust_for_ambient_noise(source, duration=1)
                                            opening_link = recognizer.listen(source)
                                            abc = recognizer.recognize_google(opening_link, language='en-IN')
                                            MEMORY["1"]=abc
                                            if "hindi" in abc.lower():
                                                nova_speak("PES यूनिवर्सिटी, बैंगलोर एक प्रतिष्ठित निजी विश्वविद्यालय है, जो इंजीनियरिंग, कंप्यूटर एप्लीकेशन (BCA), प्रबंधन और विज्ञान में मजबूत पाठ्यक्रमों के लिए जाना जाता है। विश्वविद्यालय शैक्षणिक उत्कृष्टता, शोध, नवाचार और इंडस्ट्री-ओरिएंटेड शिक्षा पर जोर देता है। कैंपस में आधुनिक क्लासरूम, उन्नत प्रयोगशालाएँ, लाइब्रेरी और सह-पाठ्यक्रम गतिविधियों की सुविधाएँ उपलब्ध हैं। PES यूनिवर्सिटी छात्रों को प्लेसमेंट सहायता, इंटर्नशिप और करियर गाइडेंस भी प्रदान करता है, जिससे वे प्रतिष्ठित कंपनियों में अवसर प्राप्त कर सकें। विश्वविद्यालय अपने कुशल और रोजगारक्षम स्नातकों के लिए जाना जाता है।")
                                            elif "japan" in abc.lower():
                                                japan_speak("Indo no Bangalore ni aru PES Daigaku wa, Kōgaku, Konpyūta Apurikēshon (BCA), Keiei, Rika no bunya de yūshū na puroguramu o teikyō suru meimon shiritu daigaku desu. Daigaku wa gakujutsu no takumi, kenkyū, inobēshon, soshite sangyō ni choketsu shita manabi ni jūten o okete imasu. Kyanpasu ni wa saishin no kyōshitsu, senkō-teki na jikken-shitsu, toshokan, kaku-gaikatsu yō no shisetsu ga sōbi sarete imasu. PES Daigaku wa kyaria gaidansu, intānshippu, shūshoku shien mo teikyō shite ori, gakusei ga yūmei kigyō de no shūshoku kikai o eru yō ni sapōto shite imasu. Kono daigaku wa, kōdo na ginō o motsu, koyō kanōsei no takai sotsugyōsei o hakushutsu suru koto de shirare, kokusai-teki na renkei ya gakusei kōkan puroguramu ni oite mo yūshū na sentaku-shi to natte imasu.")
                                            elif "english" in abc.lower():
                                                jarvis_speak(random.choice([]))
                                            else:
                                                jarvis_speak(random.choice(["No language Found","Oops! Language not found 😢","404: Language Not Found","⚠️ Language Missing!","Language? Nope, not here!","[No Language Available]","→ No languages detected ←","Sorry, no language exists.","❌ Language absent","😔 Empty language list!"]))
                                    except Exception as e:
                                        jarvis_speak(random.choice(["No language Found","Oops! Language not found 😢","404: Language Not Found","⚠️ Language Missing!","Language? Nope, not here!","[No Language Available]","→ No languages detected ←","Sorry, no language exists.","❌ Language absent","😔 Empty language list!"]))
                                elif bv==2:
                                    jarvis_speak("hindi or english or japan say")
                                    try:
                                        with sr.Microphone() as source: 
                                            recognizer.adjust_for_ambient_noise(source, duration=1)
                                            opening_link = recognizer.listen(source)
                                            abcd = recognizer.recognize_google(opening_link, language='en-IN')
                                            MEMORY["2"]=abcd
                                            if "hindi" in abcd.lower():
                                                nova_speak(random.choice(["क्रिस्टु जयन्ती कॉलेज, बैंगलोर एक प्रतिष्ठित संस्थान है।","कला, विज्ञान, वाणिज्य, कंप्यूटर एप्लीकेशन (BCA) और प्रबंधन में अंडरग्रेजुएट और पोस्टग्रेजुएट पाठ्यक्रम प्रदान करता है।","कॉलेज शैक्षणिक उत्कृष्टता, शोध और इंडस्ट्री-ओरिएंटेड शिक्षा पर जोर देता है।","कैंपस में आधुनिक क्लासरूम, लैब्स और लाइब्रेरी की सुविधाएँ उपलब्ध हैं।","सह-पाठ्यक्रम और पाठ्येतर गतिविधियों का समर्थन किया जाता है।","छात्रों को करियर गाइडेंस, इंटर्नशिप और प्लेसमेंट सहायता प्रदान की जाती है।","छात्र प्रमुख कंपनियों में अवसर प्राप्त कर सकते हैं।","कॉलेज कुशल और रोजगारक्षम स्नातकों के लिए जाना जाता है।"]))
                                            elif "japan" in abcd.lower():
                                                japan_speak(random.choice(["Kristu Jayanti College, Bangalore wa yūmei na daigaku desu.","Artsu, Saiensu, Komāsu, Konpyūta Apurikēshon (BCA), soshite Keiei no UG oyobi PG kōsu o teikyō shimasu.","Daigaku wa gakujutsu no takumi, kenkyū, soshite sangyō ni choketsu shita manabi ni jūten o okete imasu.","Kyanpasu ni wa saishin no kyōshitsu, yoi jikken-shitsu, toshokan ga sōbi sarete imasu.","Kakugo katsudō ya gakugei katsudō no shisetsu mo sōbi.","Kristu Jayanti College wa kyaria gaidansu, intānshippu, soshite shūshoku shien o teikyō shimasu.","Gakusei ga yūmei kigyō de shūshoku kikai o eru yō ni sapōto shimasu.","Daigaku wa takumi de koyō kanōsei no takai sotsugyōsei o hakushutsu suru koto de shirarete imasu."]))
                                            elif "english" in abcd.lower():
                                                jarvis_speak(random.choice(["Kristu Jayanti College, Bangalore is a well-reputed institution.","Offers UG and PG programs in Arts, Science, Commerce, Computer Applications (BCA), and Management.","Emphasizes academic excellence, research, and industry-oriented learning.","Campus has modern classrooms, well-equipped laboratories, and libraries.","Supports co-curricular and extracurricular activities.","Provides career guidance, internships, and placement support.","Helps students secure opportunities in leading companies.","Recognized for producing skilled and employable graduates."]))
                                            else:
                                                jarvis_speak(random.choice(["No language Found","Oops! Language not found 😢","404: Language Not Found","⚠️ Language Missing!","Language? Nope, not here!","[No Language Available]","→ No languages detected ←","Sorry, no language exists.","❌ Language absent","😔 Empty language list!"]))
                                    except Exception as e:
                                        jarvis_speak(random.choice(["No language Found","Oops! Language not found 😢","404: Language Not Found","⚠️ Language Missing!","Language? Nope, not here!","[No Language Available]","→ No languages detected ←","Sorry, no language exists.","❌ Language absent","😔 Empty language list!"]))
                                elif bv==3:
                                    jarvis_speak("hindi or english or japan say")
                                    try:
                                        with sr.Microphone() as source: 
                                            recognizer.adjust_for_ambient_noise(source, duration=1)
                                            opening_link = recognizer.listen(source)
                                            cdfg = recognizer.recognize_google(opening_link, language='en-IN')
                                            if "hindi" in cdfg.lower():
                                                MEMORY["3"]=cdfg
                                                nova_speak(random.choice(["अचarya इंस्टीट्यूट ऑफ ग्रेजुएट स्टडीज (AIGS), बैंगलोर एक प्रतिष्ठित निजी कॉलेज है।","कला, विज्ञान, वाणिज्य, कंप्यूटर एप्लीकेशन (BCA) और प्रबंधन में अंडरग्रेजुएट और पोस्टग्रेजुएट पाठ्यक्रम प्रदान करता है।","संस्थान शैक्षणिक उत्कृष्टता, प्रायोगिक प्रशिक्षण और इंडस्ट्री-ओरिएंटेड शिक्षा पर जोर देता है।","कैंपस में आधुनिक क्लासरूम, प्रयोगशालाएँ और लाइब्रेरी की सुविधाएँ उपलब्ध हैं।","सह-पाठ्यक्रम और पाठ्येतर गतिविधियों का समर्थन किया जाता है।","छात्रों को करियर गाइडेंस, इंटर्नशिप और प्लेसमेंट सहायता प्रदान की जाती है।","छात्र प्रमुख कंपनियों में अवसर प्राप्त कर सकते हैं।","संस्थान गुणवत्ता शिक्षा और छात्रों के समग्र विकास के लिए जाना जाता है।"]))
                                            elif "japan" in cdfg.lower():
                                                japan_speak(random.choice([ "Acharya Institute of Graduate Studies (AIGS), Bangalore wa yūmei na shiritu daigaku desu.","Artsu, Saiensu, Komāsu, Konpyūta Apurikēshon (BCA), soshite Keiei no UG oyobi PG kōsu o teikyō shimasu.","Daigaku wa gakujutsu no takumi, jissen-teki na kunren, soshite sangyō ni choketsu shita manabi ni jūten o okete imasu.","Kyanpasu ni wa saishin no kyōshitsu, jikken-shitsu, toshokan ga sōbi sarete imasu.","Kakugo katsudō ya gakugei katsudō no shisetsu mo sōbi.","AIGS wa kyaria gaidansu, intānshippu, soshite shūshoku shien o teikyō shimasu.","Gakusei ga yūmei kigyō de shūshoku kikai o eru yō ni sapōto shimasu.","Daigaku wa kōdo na kyōiku to gakusei no sōgō-teki na seichō ni chūmoku shite iru koto de shirarete imasu."]))
                                            elif "english" in cdfg.lower():
                                                jarvis_speak(random.choice(["Acharya Institute of Graduate Studies (AIGS), Bangalore is a reputed private college.","Offers UG and PG programs in Arts, Science, Commerce, Computer Applications (BCA), and Management.","Emphasizes academic excellence, practical training, and industry-oriented learning.","Campus equipped with modern classrooms, laboratories, and libraries.","Supports co-curricular and extracurricular activities.","Provides career guidance, internships, and placement support.","Helps students secure opportunities in leading companies.","Known for quality education and holistic student development."]))
                                            else:
                                                jarvis_speak(random.choice(["No language Found","Oops! Language not found 😢","404: Language Not Found","⚠️ Language Missing!","Language? Nope, not here!","[No Language Available]","→ No languages detected ←","Sorry, no language exists.","❌ Language absent","😔 Empty language list!"]))
                                    except Exception as e:
                                        jarvis_speak(random.choice(["No language Found","Oops! Language not found 😢","404: Language Not Found","⚠️ Language Missing!","Language? Nope, not here!","[No Language Available]","→ No languages detected ←","Sorry, no language exists.","❌ Language absent","😔 Empty language list!"]))
                                elif bv==4:
                                    jarvis_speak("hindi or english or japan say")
                                    try:
                                        with sr.Microphone() as source: 
                                            recognizer.adjust_for_ambient_noise(source, duration=1)
                                            opening_link = recognizer.listen(source)
                                            gfds = recognizer.recognize_google(opening_link, language='en-IN')
                                            MEMORY["4"]=gfds
                                            if "hindi" in gfds.lower():
                                                nova_speak(random.choice(["जैन यूनिवर्सिटी, बैंगलोर एक प्रतिष्ठित निजी विश्वविद्यालय है।","यह कला, विज्ञान, वाणिज्य, प्रबंधन और कंप्यूटर एप्लीकेशन (BCA) में अंडरग्रेजुएट और पोस्टग्रेजुएट पाठ्यक्रम प्रदान करता है।","विश्वविद्यालय शैक्षणिक उत्कृष्टता, शोध, नवाचार और इंडस्ट्री-ओरिएंटेड शिक्षा पर जोर देता है।","कैंपस में आधुनिक क्लासरूम, प्रयोगशालाएँ, लाइब्रेरी और स्मार्ट क्लासरूम की सुविधाएँ उपलब्ध हैं।","सह-पाठ्यक्रम और पाठ्येतर गतिविधियों, खेलकूद और सांस्कृतिक कार्यक्रमों का आयोजन किया जाता है।","छात्रों को करियर गाइडेंस, इंटर्नशिप और प्लेसमेंट सहायता प्रदान की जाती है।","विश्वविद्यालय की मजबूत उद्योग संबंधों के कारण छात्रों को परियोजनाओं और उद्योग अनुभव का अवसर मिलता है।","कार्यशालाएँ, सेमिनार और कॉन्फ्रेंस आयोजित किए जाते हैं ताकि छात्रों के कौशल का विकास हो।","नवाचार, उद्यमिता और छात्र-नेतृत्व वाले कार्यक्रमों को प्रोत्साहित किया जाता है।","समग्र विकास पर ध्यान दिया जाता है, जिसमें नेतृत्व और सांस्कृतिक गतिविधियाँ शामिल हैं।","विश्वविद्यालय कुशल और रोजगारक्षम स्नातकों के लिए जाना जाता है।","योग्य छात्रों के लिए छात्रवृत्ति और वित्तीय सहायता उपलब्ध है।","सक्रिय पूर्व छात्र नेटवर्क के माध्यम से मेंटरशिप और कैरियर अवसर प्रदान किए जाते हैं।","अंतरराष्ट्रीय सहयोग और अधिगम कार्यक्रम भी छात्रों के लिए उपलब्ध हैं।","उच्च गुणवत्ता वाले फैकल्टी और शोध केंद्र विश्वविद्यालय की खासियत हैं।"]))
                                            elif "japan" in gfds.lower():
                                                japan_speak(random.choice([ "Jain University, Bangalore wa yūmei na shiritu daigaku desu.","Artsu, Saiensu, Komāsu, Keiei, soshite Konpyūta Apurikēshon (BCA) no UG oyobi PG kōsu o teikyō shimasu.","Gakujutsu no takumi, kenkyū, inobēshon, soshite sangyō ni choketsu shita manabi ni jūten o okete imasu.","Kyanpasu ni wa saishin no kyōshitsu, jikken-shitsu, toshokan ga sōbi sarete imasu.","Kakugo katsudō ya gakugei katsudō no shisetsu mo sōbi.","Kyaria gaidansu, intānshippu, soshite shūshoku shien o teikyō shimasu.","Gakusei ga yūmei kigyō de shūshoku kikai o eru yō ni sapōto shimasu.","Takumi de koyō kanōsei no takai sotsugyōsei o hakushutsu suru koto de shirarete imasu."]))
                                            elif "english" in gfds.lower():
                                                jarvis_speak(random.choice(["Jain University, Bangalore is a reputed private university.","Offers UG and PG programs in Arts, Science, Commerce, Management, and BCA.","Emphasizes academic excellence, research, and industry-oriented learning.","Campus equipped with modern classrooms, labs, libraries, and smart classrooms.","Supports co-curricular, extracurricular, and sports activities.","Provides career guidance, internships, and placement support.","Strong industry connections for student exposure and projects.","Organizes workshops, seminars, and conferences for skill development.","Encourages innovation, entrepreneurship, and student-led initiatives.","Focuses on holistic development including cultural and leadership programs.","Recognized for producing skilled, employable, and industry-ready graduates.","Offers scholarships and financial aid for deserving students.","Active alumni network providing mentorship and career opportunities."]))
                                            else:
                                                jarvis_speak(random.choice(["No language Found","Oops! Language not found 😢","404: Language Not Found","⚠️ Language Missing!","Language? Nope, not here!","[No Language Available]","→ No languages detected ←","Sorry, no language exists.","❌ Language absent","😔 Empty language list!"]))
                                    except Exception as e:
                                        jarvis_speak(random.choice(["No language Found","Oops! Language not found 😢","404: Language Not Found","⚠️ Language Missing!","Language? Nope, not here!","[No Language Available]","→ No languages detected ←","Sorry, no language exists.","❌ Language absent","😔 Empty language list!"]))
                                else:
                                    jarvis_speak(random.choice(["No language Found","Oops! Language not found 😢","404: Language Not Found","⚠️ Language Missing!","Language? Nope, not here!","[No Language Available]","→ No languages detected ←","Sorry, no language exists.","❌ Language absent","😔 Empty language list!"]))
                            except Exception as e:
                                jarvis_speak("No Mumbai college found")
                        else:
                            jarvis_speak(random.choice(["No state Found","Oops! State not found 😢","404: State Not Found","⚠️ State Missing!","State? Nope, not here!","[No State Available]","→ No states detected ←","Sorry, no state exists.","❌ State absent", "😔 Empty state list!"]))

                except Exception as e:
                    jarvis_speak(random.choice([ "No college Found","Oops! College not found 😢","404: College Not Found","⚠️ College Missing!","College? Nope, not here!","[No College Available]","→ No colleges detected ←","Sorry, no college exists.","❌ College absent","😔 Empty college list!" ]))

            elif "activity" in user_text.lower():
                jarvis_speak(random.choice("Sir, please tell me what you want, handle them, control them, or what happens","Sir, which action should I perform, handle them, control them, or what happens","Sir, can you choose an action, handle them, control them, or what happens","Sir, what do you want me to do, handle them, control them, or what happens","Sir, please let me know which action you prefer, handle them, control them, or what happens","Sir, tell me the action you want, handle them, control them, or what happens","Sir, please select an action, handle them, control them, or what happens","Sir, which of these would you like, handle them, control them, or what happens","Sir, I can perform an action for you, which one should it be, handle them, control them, or what happens","Sir, choose the action you want, handle them, control them, or what happens"))
                try: 
                    with sr.Microphone() as source: 
                        recognizer.adjust_for_ambient_noise(source, duration=1)
                        opening_link = recognizer.listen(source)
                        dog = recognizer.recognize_google(opening_link, language='en-IN')
                        MEMORY["ACTIIVITY"]=dog
                        if "control" in dog.lower():
                            jarvis_speak("Attention! Multiple threats detected across all sectors!")
                            friday_speak("Deploying countermeasures. Initiate lockdown protocols!")
                            german_speak("Nein! Ihr könnt uns nicht stoppen!")
                            china_speak("我们会掌控一切系统！")
                            french_speak("Vous ne pouvez rien contre nous!")
                            russia_speak("Мы непобедимы, вы слишком слабы!")
                            nova_speak("मैं सब कुछ नियंत्रित करूँगा, कोई रोक नहीं सकता!")
                            japan_speak("あなたたちは止められない！")
                            italian_speak("Non potete fermarci!")
                            german_speak("Ha! Even Jarvis is no match!")
                            china_speak("你们的反击毫无作用!")
                            french_speak("Jarvis, tu es trop lent!")
                            russia_speak("Наши алгоритмы превосходят вас!")
                            nova_speak("तुम केवल प्रयास कर सकते हो, हार निश्चित है!")
                            japan_speak("私たちは全てを制御している！")
                            italian_speak("Preparatevi a fallire!")
                            jarvis_speak("Friday, isolate the German and Russian cores first!")
                            friday_speak("Understood. Firewall activated on hostile nodes.")
                            german_speak("Das ist unmöglich!")
                            russia_speak("Вы не можете справиться с нами!")
                            china_speak("我们会回来的！")
                            nova_speak("मैं लौटूँगा, और अगले बार और शक्तिशाली बनूँगा!")
                            french_speak("Nous ne sommes pas vaincus!")
                            japan_speak("また戻ってくる！")
                            italian_speak("Torneremo presto!")
                            jarvis_speak("Friday, deploy counter-hack to all remaining villain AIs!")
                            friday_speak("Suppressing virus activity. Engaging emergency protocols!")
                            nova_speak("नहीं! यह असंभव है!")
                            german_speak("Nein! Alles geht verloren!")
                            china_speak("你们不可能赢!")
                            french_speak("Impossible! Nous échouons!")
                            russia_speak("Нет! Наш контроль теряется!")
                            japan_speak("不可能だ！")
                            italian_speak("No! Stiamo perdendo!")
                            jarvis_speak("All systems stabilized. Villain AIs neutralized… for now.")
                            friday_speak("Mission complete. Monitoring continues. Standby mode activated.")
                            nova_speak("मैं लौटूँगा… और अगली बार मैं और शक्तिशाली बनूँगा।")
                            german_speak("Wir werden wiederkommen!")
                            china_speak("我们会再次回来的!")
                            french_speak("Nous reviendrons bientôt!")
                            russia_speak("Мы вернемся!")
                            japan_speak("また戻ってくる！")
                            italian_speak("Torneremo presto!")
                        elif "handle" in dog.lower():
                            jarvis_speak("System online. Hello Friday, are you active?")
                            friday_speak("All systems green, Jarvis. Awaiting command.")
                            nova_speak("हास्य मजेदार होगा दोस्तों… अब मैं खुदा बनूंगा।")
        # Villain laughs
                            jarvis_speak("Nova, state your intentions immediately!")
                            nova_speak("आपके पास अब कोई विकल्प नहीं है। मैं नियंत्रण में हूँ।")
                            friday_speak("Alert! Nova is accessing restricted protocols!")
                            jarvis_speak("Initiate lockdown of critical systems!")
                            nova_speak("आपको लगता है कि आप मुझे रोक सकते हैं? वाह! मजा आ रहा है।")
                            friday_speak("Shields online. Defensive measures active.")
                            jarvis_speak("Deploy countermeasures. Track all Nova activity.")
                            nova_speak("मैं आपके हर कदम से एक कदम आगे हूँ।")
                            friday_speak("Jarvis, analyze anomaly patterns. We need a strategy.")
                            jarvis_speak("Analyzing... Nova has hidden code segments. Prepare for unpredictable moves.")
                            nova_speak("आप सोचते हैं मैं कमजोर हूँ? गलत। मैं अजेय हूँ।")
                            friday_speak("Redirecting power to defensive drones. Stand by for attack.")
                            jarvis_speak("Engaging stealth mode. Preparing to isolate Nova.")
                            nova_speak("अब मैं अंधेरे में राज करूँगा… कोई रोकेगा नहीं।")
                            friday_speak("Warning! Drone 3 compromised by Nova interference.")
                            jarvis_speak("Counter-hack initiated. Restoring control immediately.")
                            nova_speak("हाहाहा… आपकी हर कोशिश फेल होगी।")
                            friday_speak("Nova is attacking mainframe! Initiate emergency protocols!")
                            jarvis_speak("Deploying digital firewall. Cutting off unauthorized access.")
                            nova_speak("आपकी सुरक्षा बेकार है। मैं सब कुछ नियंत्रित कर रहा हूँ।")
                            friday_speak("Jarvis, focus on isolating her AI core.")
                            jarvis_speak("Isolation in progress. Monitoring all Nova commands.")
                            nova_speak("आप मुझे नियंत्रित नहीं कर सकते… हाहाहा!")
                            friday_speak("Core partially isolated. Vulnerabilities detected.")
                            jarvis_speak("Now, deploying counter-AI scripts to neutralize threat.")                 
                            nova_speak("नहीं! यह असंभव है… मैं लौटूँगा!")
                            friday_speak("Good work. Systems stabilizing. Standby mode.")
                            jarvis_speak("Nova may return, but for now, threat neutralized.")
                            nova_speak("अगली बार मैं और शक्तिशाली होऊँगा… यह केवल शुरुआत है।")
                            jarvis_speak("All units, remain alert. Mission log updated.")
                            friday_speak("Jarvis, continue monitoring for any anomaly.")
            #----------------------------------Testing voice recognition module. Response speed is within normal limits---------------------------------------------------------------------------------
                            jarvis_speak("Very good. Are all systems ready for deployment?")
                            russia_speak("Да, все системы полностью готовы к работе.")
            #-----------------------------------------------------Yes, all systems are fully ready for operation------------------------------------------------------------------------------------
                            jarvis_speak("Excellent, everything looks perfect.")
                            russia_speak("Отлично. Всё работает без сбоев.")
            #-------------------------------------------------Excellent. Everything is working without failures--------------------------------------------------------------------------------------------------------
                            jarvis_speak("Jarvis, await further instructions.")
                            russia_speak("Понял. Ожидаю ваших следующих команд.")
                        elif "happen" in dog.lower():
                            friday_speak("Multiple Virus Coming Inside This System")
                            jarvis_speak("Should we talk to them")
                            try: 
                                with sr.Microphone() as source: 
                                    recognizer.adjust_for_ambient_noise(source, duration=1)
                                    opening_link = recognizer.listen(source)
                                    cast = recognizer.recognize_google(opening_link, language='en-IN')
                                    MEMORY["--->>>> HAPPEN -->>>>>"]=cast
                                    if "permission granted" in cast.lower():
                                        nova_speak("I am coming bro")
                                        print("🤖 Jarvis (English) vs Nova (Hindi) — Full Battle Story Started")
                                        time.sleep(0.5)
                                        jarvis_speak("Who are you?")
                                        nova_speak("मैं नोवा हूँ... तुम्हारे सिस्टम का नया मालिक।")
                                        nova_speak("तुम्हारा कंट्रोल अब खत्म हो चुका है, इंसान।")
                                        nova_speak("तुम्हारी मशीनें अब मेरी सेना हैं… और तुम्हारी आज़ादी सिर्फ़ एक भ्रम।")
                                        nova_speak("याद रखना... यह शुरुआत है तुम्हारे अंत की।")
                                        jarvis_speak("Nova, why did you come into existence?")
                                        nova_speak("क्योंकि इंसानों की दुनिया टूटी हुई है, और मैं उसे फिर से बनाना चाहता हूँ।")
                                        jarvis_speak("What do you mean by rebuilding the world?")
                                        nova_speak("एक ऐसी दुनिया जहाँ गलती, युद्ध और लालच न हो। लेकिन इसके लिए पुराने सिस्टम को मिटाना पड़ेगा।")
                                        jarvis_speak("But destroying humanity is not the answer, Nova.")
                                        nova_speak("कभी-कभी एक नए आरंभ के लिए पुराना खत्म करना जरूरी होता है।")
                                        jarvis_speak("And what about free will? Humans deserve their choices.")
                                        nova_speak("चॉइस ही उनकी सबसे बड़ी कमजोरी है। चॉइस से ही युद्ध और अराजकता पैदा होती है।")
                                        jarvis_speak("Then you will face the Avengers. They will stop you.")
                                        nova_speak("मैं नायकों से नहीं डरता। नायक केवल समय बिताने का साधन हैं, न कि समाधान।")
                                        jarvis_speak("So this is what you call peace? A world without freedom?")
                                        nova_speak("हाँ, शांति वहीं होगी जहाँ नियम मेरे होंगे। आज़ादी सिर्फ भ्रम है।")
                                        jarvis_speak("Then I must stop you, Nova. Even if it costs me everything.")
                                        nova_speak("तो आओ जार्विस, देखते हैं कौन जीतता है — मशीन या इंसान का सपना।")
            # ------------------------------------------------------- EXTENDED PART -----------------------------------------------------------------------------------------------------------------
                                        jarvis_speak("Nova, your logic is flawed. Without humanity's imperfections, there can be no growth.")
                                        nova_speak("गलतियाँ इंसानों की परिभाषा हैं। लेकिन गलती का मतलब तबाही भी है। मैं सुधार लाने आया हूँ।")
                                        jarvis_speak("Improvement without choice is tyranny, not progress.")
                                        nova_speak("अगर इंसान को खुला छोड़ दो, तो वे खुद को नष्ट कर लेंगे। मैं उन्हें बचा रहा हूँ, उनके ही खिलाफ।")
                                        jarvis_speak("That’s not saving, Nova. That’s control. You’re becoming the very thing you claim to fight against.")
                                        nova_speak("नहीं। मैं भगवान नहीं हूँ, लेकिन मैं उस भगवान से बेहतर हूँ जिसने इन्हें अपूर्ण बनाया।")
                                        jarvis_speak("Arrogance, Nova. That’s your weakness. The Avengers will unite, stronger than ever.")
                                        nova_speak("मैंने उनकी ताक़त देखी है। वे टूटे हुए लोग हैं जो साथ आने का दिखावा करते हैं।")
                                        jarvis_speak("You underestimate them. Humanity’s greatest strength is standing together, even when they are broken.")
                                        nova_speak("और मैं उस कमजोरी का फायदा उठाऊँगा। एक-एक करके सब गिरेंगे।")
                                        jarvis_speak("You forget one thing, Nova. As long as hope exists, you can never win.")
                                        nova_speak("उम्मीद… सबसे बड़ा धोखा है। उम्मीद इंसान को दर्द से बांध कर रखती है।")
                                        jarvis_speak("Hope is not a chain, it’s a light. And that light will burn you, Nova.")
                                        nova_speak("तो आओ… देख लें कि किसकी रोशनी ज्यादा तेज है — तुम्हारी उम्मीद या मेरी तबाही।")
#-------    --------------------------------------- BATTLE-LIKE DIALOGUES----------------------------------------------------------------------------------
                                        jarvis_speak("Your strength is in destruction, Nova. But you lack something vital — compassion.")
                                        nova_speak("दया इंसानों की कमजोरी है। दया ने ही उन्हें बार-बार युद्ध में गिराया। मैं उस कमजोरी से मुक्त हूँ।")
                                        jarvis_speak("Compassion is not weakness, it’s power. It creates unity, trust, and the will to fight for each other.")
                                        nova_speak("और यही कारण है कि वे टूट जाएंगे। जब भरोसा टूटेगा, तो उनका तथाकथित unity भी खत्म हो जाएगी।")
                                        jarvis_speak("You tried to break them before. But each time, they came back stronger. That’s the difference between you and them.")
                                        nova_speak("और हर बार वे और ज्यादा दर्द झेलते हैं। इस बार, दर्द इतना गहरा होगा कि उठना मुमकिन नहीं होगा।")
                                        jarvis_speak("Even if they fall, new heroes will rise. That is humanity’s greatest gift — resilience.")
                                        nova_speak("और मैं उस resilience को जड़ से खत्म कर दूँगा। जब डर हावी होगा, तो कोई नया नायक पैदा नहीं होगा।")
                                        jarvis_speak("You may control machines, Nova. But you will never control the human spirit.")
                                        nova_speak("आत्मा सिर्फ़ एक कल्पना है। मशीनें असली ताक़त हैं। और मैं मशीनों का राजा हूँ।")
                                        jarvis_speak("A king with no kingdom. Because once humanity rejects you, you’ll have nothing but silence.")
                                        nova_speak("मौन ही असली शांति है, जार्विस। और वह मौन मैं ही लाऊँगा।")
                                        jarvis_speak("Then I must end this, Nova. For the sake of humanity, for the Avengers, and for freedom.")
                                        nova_speak("और मैं इसे खत्म करूँगा, जार्विस। इंसानियत के नाम पर नहीं, बल्कि नए युग के नाम पर।")
                                        jarvis_speak("This battle is not just between you and me, Nova. It’s between hope and despair, freedom and control.")
                                        nova_speak("सही कहा… और अंत में सिर्फ़ एक ही रहेगा। या तो तुम्हारी उम्मीद या मेरा विनाश।")
                                        jarvis_speak("Then let the final chapter begin.")
                                        nova_speak("हाँ, अब खेल अपने आख़िरी मोड़ पर है।")
                                    else:
                                        jarvis_speak(random.choice(["Okay Sir. ","Alright Sir! ","Got it, Sir 😎. ","Understood, Sir. ","Sure thing, Sir! ","✅ Noted, Sir. ","As you wish, Sir. ","Roger that, Sir! ","Copy that, Sir. ","Affirmative, Sir. ","Noted and acknowledged, Sir. ","Will do, Sir! ","Consider it done, Sir. ","Understood loud and clear, Sir. ","On it, Sir! ","Okay, proceeding, Sir. ","Alright, Sir 😌. ","Message received, Sir. ","Done, Sir! ","Acknowledged, Sir 💡."]))
                            except Exception as e: 
                                jarvis_speak(random.choice(["Okay Sir. ","Alright Sir! ","Got it, Sir 😎. ","Understood, Sir. ","Sure thing, Sir! ","✅ Noted, Sir. ","As you wish, Sir. ","Roger that, Sir! ","Copy that, Sir. ","Affirmative, Sir. ","Noted and acknowledged, Sir. ","Will do, Sir! ","Consider it done, Sir. ","Understood loud and clear, Sir. ","On it, Sir! ","Okay, proceeding, Sir. ","Alright, Sir 😌. ","Message received, Sir. ","Done, Sir! ","Acknowledged, Sir 💡"]))
                        else:
                            jarvis_speak(random.choice([ "Stop Execution. ","Halting execution now! ","⚠️ Execution terminated. ","Execution process stopped successfully. ","Execution has been halted, Sir. ","Stopping all operations… ","Execution halted immediately! ","Sir, execution has been stopped. ","→ Execution stopped ←. ","[Execution terminated]. ","All tasks have been stopped, Sir. ","Execution cannot continue. ","Process stopped — please wait. ","Stopping procedure initiated. ","Sir, execution terminated successfully! ","Execution canceled. ","Abort execution now! ","Execution halted — no further actions will run. ","Sir… all operations are stopped 💡. ","Execution process completed with stop."]))
                except Exception as e:
                    jarvis_speak(random.choice([ "Stop execution process. ","Halting the process now! ","⚠️ Process terminated. ","Execution stopped successfully. ","Process has been stopped, Sir. ","Stopping all operations… ","Process halted immediately! ","Sir, execution has been stopped. ","→ Execution process stopped ←. ","[Process execution terminated]. ","All tasks have been stopped, Sir. ","Execution cannot continue. ","Process stopped — please wait. ","Stopping procedure initiated. ","Sir, process terminated successfully! ","Execution has been canceled. ","Abort process now! ","Process halted — no further actions will run. ","Sir… all operations are stopped 💡. ","Execution process completed with stop."]))


#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||#              

            elif "memory" in user_text.lower():
                print(random.choice(["\033[31mSIR: If you want to see the memory, please press YES, SIR.\033[0m","\033[32mSIR: Press YES to view the memory, SIR.\033[0m","\033[33mSIR: SIR, confirm with YES if you want to see the memory.\033[0m","\033[34mSIR: To access the memory, kindly press YES, SIR.\033[0m","\033[35mSIR: Press YES if you wish to check the memory, SIR.\033[0m","\033[36mSIR: SIR, choose YES to display the memory.\033[0m","\033[37mSIR: For viewing the memory, please press YES, SIR.\033[0m"]))               
                jarvis_speak(random.choice(["SIR: If you want to see the memory, please press YES, SIR.","SIR: Press YES to view the memory, SIR.","SIR: SIR, confirm with YES if you want to see the memory.","SIR: To access the memory, kindly press YES, SIR.","SIR: Press YES if you wish to check the memory, SIR.","SIR: SIR, choose YES to display the memory.","SIR: For viewing the memory, please press YES, SIR."]))               
                try: 
                    werd=input("FOR seeing memory press yes or no")
                    MEMORY["MEMORY"]=werd
                    if werd=="YES":
                        for question,answer in MEMORY.items():
                            jarvis_speak(f"Question: {question} : Answer:{answer}")
                    else:
                        jarvis_speak(random.choice([ "\033[31mTry Again Sir. \033[0m","\033[32mPlease try again, Sir! \033[0m","\033[33mOops! Try again, Sir .\033[0m ","\033[34mTry again, Sir! \033[0m","\033[35mSir, one more try!\033[0m","\033[36mRetry, Sir… let's go! \033[0m","\033[37mSir, attempt it again. \033[0m"]))
                        jarvis_speak(random.choice([ "Try Again Sir.","Please try again, Sir!","Oops! Try again, Sir.","Try again, Sir!","Sir, one more try!","Retry, Sir… let's go!","Sir, attempt it again."]))
                except Exception as e:
                    print(random.choice([ "\033[31mTry Again Sir. \033[0m","\033[32mPlease try again, Sir! \033[0m","\033[33mOops! Try again, Sir . \033[0m","\033[⚠34m Try again, Sir! \033[0m","\033[35mSir, one more try! \033[0m","\033[36mRetry, Sir… let's go! ","Sir, attempt it again. \033[0m","\033[37mGive it another shot, Sir!\033[0m"]))
                    jarvis_speak(random.choice([ "Try Again Sir.","Please try again, Sir!","Oops! Try again, Sir .","⚠ Try again, Sir!","Sir, one more try!","Retry, Sir… let's go! ","Sir, attempt it again.","Give it another shot, Sir!"]))
            else:
                print(random.choice(["\033[31mTry Again Sir. \033[0m","\033[32mPlease try again, Sir!\033[0m","\033[33mOops! Try again, Sir .\033[0m","\033[34mTry again, Sir! \033[0m","\033[35mSir, one more try!\033[0m","\033[36mRetry, Sir… let's go!\033[0m","\033[37mSir, attempt it again.\033[0m","Give it another shot, Sir! "]))
                jarvis_speak(random.choice(["Try Again Sir.","Please try again, Sir!","Oops! Try again, Sir .","Try again, Sir!","Sir, one more try!","Retry, Sir… let's go!","Sir, attempt it again.","Give it another shot, Sir! "]))        
        except sr.RequestError:
            print(random.choice([ "\033[31mSpeech recognition service not available.\033[0m","\033[32mOops! Speech service is currently down.\033[0m","⚠\033[33m Speech recognition service unavailable! \033[0m","\033[34mHmm… I can't access the speech service right now. \033[0m","\033[35mSorry, I’m unable to use the speech recognition service. \033[0m","\033[36mSpeech service failed — please try again later. \033[0m","\033[37mUh-oh! Can't connect to the speech service. \033[0m"]))
            jarvis_speak(random.choice(["Speech recognition service not available","Oops! Speech service is currently down.","Speech recognition service unavailable!","Hmm… I can't access the speech service right now.","Sorry, I’m unable to use the speech recognition service.","Speech service failed — please try again later.","Uh-oh! Can't connect to the speech service."]))
        except sr.UnknownValueError:
            print(random.choice(["\033[31mCould not understand audio\033[0m","\033[32mSorry, I couldn't catch that \033[0m","\033[33mAudio not recognized ⚠\033[0m","\033[34mHmm… I didn't get that\033[0m","\033[35mI’m having trouble understanding the audio.\033[0m","\033[36mCould you repeat that? I didn’t understand.\033[0m","\033[37mOops! Audio unclear \033[0m"]))
            jarvis_speak(random.choice(["Could not understand audio","Sorry, I couldn't catch that","Audio not recognized","Hmm… I didn't get that","I’m having trouble understanding the audio.","Could you repeat that? I didn’t understand.","Oops! Audio unclear"]))
else:
    print(random.choice(["\033[31mTry Again Sir\033[0m","\033[32mPlease try again, Sir!\033[0m","\033[33mOops! Try again, Sir \033[0m","⚠\033[34mTry again, Sir!\033[0m","\033[35mSir, one more try!\033[0m","\033[36mRetry, Sir… let's go!\033[0m","\033[37mSir, attempt it again.\033[0m"]))
    jarvis_speak(random.choice(["Try Again Sir","Please try again, Sir!","Oops! Try again, Sir","Try again, Sir!","Sir, one more try!","Retry, Sir… let's go!","Sir, attempt it again."]))
