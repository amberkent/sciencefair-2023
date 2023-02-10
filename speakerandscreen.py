import io
import os
import time
import PySimpleGUI as sg
from PIL import Image
import pyttsx3
engine = pyttsx3.init()
import time

def Speak(name):
    time.sleep(3)
    engine.say("{}".format(name))
    engine.runAndWait()
    
layout = [
    [sg.Image(key="-IMAGE-", background_color='black', pad=(0, 0))],
]
window = sg.Window("Image Viewer", layout,)
window.finalize()

def set_image(filename):
    if os.path.exists(filename):
        image = Image.open(filename)
        image.thumbnail((400, 400))
        bio = io.BytesIO()
        image.save(bio, format="PNG")
        window["-IMAGE-"].update(data=bio.getvalue())
    else:
      raise Error("ERROR: NO FILE")

def scuba():
  set_image("images/scuba.jpeg")
  Speak("Save me I'm drowning.")

def perfect():
  set_image("images/perfect.jpeg")
  Speak("It's a pristine day.")
    
 def dry():
  set_image("")
  Speak("I'm in a drout over here.")


    
def change_image():
  while True:
    time.sleep(3)
    scuba()
    time.sleep(3)
    perfect()
    
if __name__ == "__main__":
    perfect()

    import threading
    th = threading.Thread(target=change_image, args=())
    th.start()
    
    while True:
        event, values = window.read()

        if event == "Exit" or event == sg.WIN_CLOSED:
            break

    window.close()
