import pyttsx3
engine = pyttsx3.init()

def Speak(name):
    sleep(1000)
    engine.say("{}".format(name))
    engine.runAndWait()

Speak("Save me I am drowning")
