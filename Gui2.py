import io
import os
import PySimpleGUI as sg
from PIL import Image
# file_types = [("JPEG (*.jpg)", "*.jpg"),
#               ("All files (*.*)", "*.*")]
def main():
    img = sg.Image(key="-IMAGE-")
    layout = [
        [img],
#         [
#             sg.Text("Image File"),
#             sg.Input(size=(25, 1), key="-FILE-"),
#             sg.FileBrowse(file_types=file_types),
#             sg.Button("Load Image"),
#         ],
    ]
    window = sg.Window("Image Viewer", layout)
    
    filename = "Dog.jpg"
    
    if os.path.exists(filename):
        image = Image.open(filename)
        image.thumbnail((400, 400))
        bio = io.BytesIO()
        image.save(bio, format="PNG")
#         window["-IMAGE-"].update(data=bio.getvalue())
        img.update(data=bio.getvalue())
    else:
      raise Error("ERROR: NO FILE")
        
    
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
#         if event == "Load Image":
#             filename = values["-FILE-"]
#             if os.path.exists(filename):
#                 image = Image.open(values["-FILE-"])
#                 image.thumbnail((400, 400))
#                 bio = io.BytesIO()
#                 image.save(bio, format="PNG")
#                 window["-IMAGE-"].update(data=bio.getvalue())
    window.close()
if __name__ == "__main__":
    main()
