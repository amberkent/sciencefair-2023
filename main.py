import io
import os
import time
import PySimpleGUI as sg
from PIL import Image
import pyttsx3
engine = pyttsx3.init()
import board
import adafruit_tsl2591
import datetime
i2c = board.I2C()  
sensor = adafruit_tsl2591.TSL2591(i2c)
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)
chan_water = AnalogIn(ads, ADS.P0)
chan_light = AnalogIn(ads, ADS.P2)


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
    
# def light_sensor():
  
#     lux = sensor.lux
#     print("Total light: {0}lux".format(lux))
#     infrared = sensor.infrared
#     print("Infrared light: {0}".format(infrared))
#     visible = sensor.visible
#     print("Visible light: {0}".format(visible))
#     full_spectrum = sensor.full_spectrum
#     print("Full spectrum (IR + visible) light: {0}".format(full_spectrum))
#     time.sleep(1.0)
  
def main():
   now = datetime.datetime.now()
   while True:
       if chan_water.value >= 22297 :
           set_image("images/dry.jpeg")
           Speak("I'm in a drout over here.")

       elif chan_water.value <= 20349:
           set_image("images/scuba.jpeg")
           Speak("Save me I'm drowning.")

       elif(now.hour => 8 and  now.hour <= 18)and chan_light.value > 17945:
           set_image("images/vampire.jpeg")
           Speak("I'm scared of the dark.")
    
       else:
           set_image("images/perfect.jpeg")
           Speak("It's a pristine day.")
    
    time.sleep(60)

  def main()
    
# def change_image():
#   while True:
#     time.sleep(3)
#     scuba()
#     time.sleep(3)
#     perfect()
#     time.sleep(3)
#     vampire()
#     time.sleep(3)
#     dry()
    
# if __name__ == "__main__":
#     perfect()

#     import threading
#     th = threading.Thread(target=change_image, args=())
#     th.start()
    
#     while True:
#         event, values = window.read()

#         if event == "Exit" or event == sg.WIN_CLOSED:
#             break

#     window.close()
