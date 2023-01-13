import pyttsx3
engine = pyttsx3.init()

def MoreWater():
    engine.say("Save me I'm drowning!")
    engine.runAndWait()

MoreWater()
