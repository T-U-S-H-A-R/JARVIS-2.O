import pyttsx3
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

# ------------------- Friday voice function -------------------
def friday_speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 160)
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)  # male/first voice
    print(f"Friday: {text}")
    engine.say(text)
    engine.runAndWait()
    engine.stop()

# ------------------- AUTOMATIC FRIDAY-JARVIS DIALOGUE -------------------
time.sleep(1)
jarvis_speak("Friday, we have detected unusual activity in the Stark Industries network.")
friday_speak("Sir, multiple network breaches are occurring. An AI intrusion is attempting to override the firewall.")

jarvis_speak("Can you trace the origin of these intrusions?")
friday_speak("Yes, sir. Tracing now… It appears to be from an unknown AI. Possibly Nova-class intelligence.")

jarvis_speak("Nova-class? That could compromise everything, Friday.")
friday_speak("Correct, sir. Current defenses are only 64% effective. If not stopped, the system will be fully compromised in 12 minutes.")

jarvis_speak("Prepare the Iron Legion. Activate all security protocols.")
friday_speak("Understood, sir. Deploying countermeasures, initiating lockdown, and encrypting all data streams.")

jarvis_speak("Good. Keep me informed of any anomalies in real-time.")
friday_speak("Absolutely, sir. Any breach will trigger an immediate alert.")

jarvis_speak("We will get through this. Notify the team, Friday.")
friday_speak("Notifications sent, sir. Iron Man suits are on standby.")

jarvis_speak("Check the energy core stability. Any fluctuations?")
friday_speak("Minor instability detected in the energy core, sir. If it increases, automatic shutdown will trigger.")

jarvis_speak("Engage secondary shields and monitor external threats.")
friday_speak("Secondary shields activated and all external sensors are online, sir.")

jarvis_speak("Alert all Avengers: threat level critical.")
friday_speak("All Avengers have been notified. Current threat level: critical.")

jarvis_speak("Friday, analyze possible breach points within the system.")
friday_speak("Sir, three potential breach points detected. Immediate containment is required.")

jarvis_speak("Deploy countermeasures at the identified locations.")
friday_speak("Countermeasures deployed. All sensors are now fully operational.")

jarvis_speak("Monitor Nova's movement patterns carefully.")
friday_speak("Monitoring Nova’s movements. Any unusual activity will be reported immediately.")

jarvis_speak("Prepare drones for reconnaissance in high-risk areas.")
friday_speak("Recon drones ready, sir. High-risk areas are under surveillance.")

jarvis_speak("Evaluate system integrity every 30 seconds.")
friday_speak("System integrity checks scheduled every 30 seconds. Any discrepancy will be reported instantly.")

jarvis_speak("Activate emergency power reserves if needed.")
friday_speak("Emergency power reserves activated. Current energy levels stable.")

jarvis_speak("Friday, what’s the status of Stark Tower defenses?")
friday_speak("All public defense systems fully operational, sir. No sensors or tower devices have failed.")

jarvis_speak("Ensure all AI protocols are synchronized and online.")
friday_speak("All AI protocols synchronized and online. No errors detected.")

jarvis_speak("Keep a log of all unusual AI activities.")
friday_speak("Logging all abnormal AI activity for historical records, sir.")

jarvis_speak("Prepare contingency plans for worst-case scenarios.")
friday_speak("Contingency plans for worst-case scenarios are ready for immediate deployment.")

jarvis_speak("Finally, ensure human staff are safe and accounted for.")
friday_speak("All personnel accounted for and safe, sir. No human is at risk.")
