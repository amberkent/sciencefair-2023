import io
import os
import PySimpleGUI as sg
from PIL import Image

def main():
    layout = [
        [sg.Image(key="-IMAGE-", background_color='black', pad=(0, 0))],

    ]
    window = sg.Window("Image Viewer", layout,)
    window.finalize()
    
    filename = "images/vampire.jpeg"
    
    if os.path.exists(filename):
        image = Image.open(filename)
        image.thumbnail((400, 400))
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
    main()
