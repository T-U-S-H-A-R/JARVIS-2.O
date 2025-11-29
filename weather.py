import requests
import pyttsx3
import speech_recognition as sr

# -------- SPEAK FUNCTION --------
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# -------- VOICE INTERACTION & WEATHER --------
try:
    recognizer = sr.Recognizer()
    
    # Ask for city
    speak("Please say the city name.")
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening for city name...")
        audio = recognizer.listen(source)
    
    city = recognizer.recognize_google(audio)
    print(f"City recognized: {city}")
    
    # Fetch weather
    url = requests.get(f"https://wttr.in/{city}?format=j1")
    
    
    if url.status_code == 200:
        data = url.json()
        current = data['current_condition'][0]
        temp_C = current['temp_C']
        weather_desc = current['weatherDesc'][0]['value']
        humidity = current['humidity']
        wind_speed = current['windspeedKmph']
        wind_dir = current['winddir16Point']

        result = (f"Weather in {city}: Temperature {temp_C}°C, "
                  f"Condition: {weather_desc}, Humidity: {humidity}%, "
                  f"Wind: {wind_speed} km/h {wind_dir}")

        print(result)
        speak(result)
    else:
        speak("Could not get weather data.")
    
except sr.RequestError:
    print("Speech recognition service not available.")
except sr.UnknownValueError:
    print("Could not understand audio.")
except Exception as e:
    print("Some error occurred:", e)
