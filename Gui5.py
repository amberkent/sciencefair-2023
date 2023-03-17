import io
import os 
import time
import PySimpleGUI as sg
from PIL import Image
import cv2
img = cv2.imread('/home/img/python.png', cv2.IMREAD_UNCHANGED)
# resize image

old_path = os.path.join(
                values["-FOLDER-"], values["-FILE LIST-"][0]
            )
            #  read image using old_path
im = cv2.imread(old_path)
            #  resize image to desired dimensions
im = cv2.resize(im,[1200,800])
            # save image to temporary folder (new_path) as png
new_path ='temp_storage/image_to_show.png'
cv2.imwrite(new_path,im)
            # update window with new resized image
window["-IMAGE-"].update(new_path)

 
# scale_percent = 150 # percent of original size
# width = int(img.shape[800] * scale_percent / 100)
# height = int(img.shape[480] * scale_percent / 100)
# dim = (width, height)
 
# print('Resized Dimensions : ',resized.shape)

def scuba():
    layout = [
        [sg.Image(key="-IMAGE-", background_color='black', pad=(0, 0))],

    ]
    window = sg.Window("Image Viewer", layout,)
    window.finalize()
    
    filename = "images/scuba.jpeg"
    
    if os.path.exists(filename):
        image = Image.open(filename)
        image.thumbnail((800,480))
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
