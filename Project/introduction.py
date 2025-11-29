import google.generativeai as genai
import speech_recognition as sr
import pyttsx3

# ---------------- CONFIG ----------------
API_KEY = "." #_Google_AI_STUDIO_API_KEY
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")

# ---------------- TTS ENGINE (Jarvis Speak) ----------------

def jarvis_speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 170)
    voices=engine.getProperty("voices")
    engine.setProperty("voice",voices[0].id)
    print("Jarvis >", text)
    engine.say(text)
    engine.runAndWait()

# ---------------- LISTEN FUNCTION ----------------
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language="en-in")
        print("You >", query)
        return query
    except:
        print("Could not understand, say again...")
        return ""

# ---------------- MAIN LOOP ----------------
jarvis_speak("Hello, I am Jarvis. How can I help you?")

while True:
    user_input = listen()

    if user_input == "":
        continue

    if user_input.lower() in ["exit", "quit", "stop", "bye"]:
        jarvis_speak("Goodbye!")
        break

    try:
        response = model.generate_content(user_input)
        reply = response.text
        jarvis_speak(reply)

    except Exception as e:
        jarvis_speak("There was an error.")
        print(e)
