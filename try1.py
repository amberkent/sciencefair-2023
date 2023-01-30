import pyttsx3
engine = pyttsx3.init()
import time

def Speak(name):
    time.sleep(3)
    engine.say("{}".format(name))
    engine.runAndWait()

Speak("Save me I'm drowning.")

Speak("I'm scared of the dark.")

Speak("Were having a drout over here.")

Speak("It's a pristine day.")
