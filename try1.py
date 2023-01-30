import pyttsx3
engine = pyttsx3.init()
import time

def Speak(name):
    time.sleep(3)
    engine.say("{}".format(name))
    engine.runAndWait()

Speak("Save me I'm drowning.")

Speak("I am scared of the dark.")
