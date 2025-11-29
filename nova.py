import time
import pyttsx3
from gtts import gTTS
import os

# Jarvis voice function
def jarvis_speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 170)
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()
    engine.stop()

# Nova voice function
def nova_speak(texts):
    print("AI बोलेगी:", texts)
    filename = f"temp_voice_{int(time.time() * 5000)}.mp3"
    tts = gTTS(text=texts, lang='hi')
    tts.save(filename)
    os.system(f'start /min "" "{filename}"')
    time.sleep(5)
    os.remove(filename)

# ------------------- AUTOMATIC SCRIPTED DIALOGUE -------------------

print("🤖 Jarvis (English) vs Nova (Hindi) — Full Battle Story Started")
time.sleep(1)

# Battle Sequence
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

# ------------------- EXTENDED PART -------------------

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
