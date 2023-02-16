import io
import os
import time
import PySimpleGUI as sg
from PIL import Image
import pyttsx3
engine = pyttsx3.init()
import time
import time
import board
import adafruit_tsl2591
i2c = board.I2C()  
sensor = adafruit_tsl2591.TSL2591(i2c)


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
    
def light_sensor():
  
    lux = sensor.lux
    print("Total light: {0}lux".format(lux))
    infrared = sensor.infrared
    print("Infrared light: {0}".format(infrared))
    visible = sensor.visible
    print("Visible light: {0}".format(visible))
    full_spectrum = sensor.full_spectrum
    print("Full spectrum (IR + visible) light: {0}".format(full_spectrum))
    time.sleep(1.0)

def scuba():
  set_image("images/scuba.jpeg")
  Speak("Save me I'm drowning.")

def perfect():
  set_image("images/perfect.jpeg")
  Speak("It's a pristine day.")
    
def dry():
  set_image("images/dry.jpeg")
  Speak("I'm in a drout over here.")

def vampire():
  set_image("images/vampire.jpeg")
  Speak("I'm scared of the dark.")
    
def change_image():
  while True:
    time.sleep(3)
    scuba()
    time.sleep(3)
    perfect()
    time.sleep(3)
    vampire()
    time.sleep(3)
    dry()
    
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
