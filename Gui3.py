import io
import os
import time
import PySimpleGUI as sg
from PIL import Image

def scuba():
    layout = [
        [sg.Image(key="-IMAGE-", background_color='black', pad=(0, 0))],

    ]
    window = sg.Window("Image Viewer", layout,)
    window.finalize()
    
    filename = "images/scuba.jpeg"
    
    if os.path.exists(filename):
        image = Image.open(filename)
        image.thumbnail((800, 480))
        bio = io.BytesIO()
        image.save(bio, format="PNG")
        window["-IMAGE-"].update(data=bio.getvalue())
    else:
      raise Error("ERROR: NO FILE")
        
    
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

    window.close()
if __name__ == "__main__":
    scuba()
    time.sleep(3)
    
def perfect():
    layout = [
        [sg.Image(key="-IMAGE-", background_color='black', pad=(0, 0))],

    ]
    window = sg.Window("Image Viewer", layout,)
    window.finalize()
    
    filename = "images/perfect.jpeg"
    
    if os.path.exists(filename):
        image = Image.open(filename)
        image.thumbnail((800, 480))
        bio = io.BytesIO()
        image.save(bio, format="PNG")
        window["-IMAGE-"].update(data=bio.getvalue())
    else:
      raise Error("ERROR: NO FILE")
        
    
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

    window.close()
if __name__ == "__main__":
    time.sleep(3)
    
    perfect()
