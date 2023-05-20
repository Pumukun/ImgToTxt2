from PIL import Image
import pytesseract

import tkinter
import customtkinter

import app.py

filetypes = ['.ras', '.xwd', '.bmp', '.jpe', '.jpg', '.jpeg',
             '.xpm', '.ief', '.pbm', '.tif', '.gif', '.ppm',
             '.xbm', '.tiff', '.rgb', '.pgm', '.png', '.pnm']

def check_filetype(file_path: str) -> bool:
    if file_path[file_path.find('.')::] in filetypes:
        return True
    return False



file_p = '/home/pumukun/Downloads/Telegram Desktop/tg_image_1217954506.jpeg'

img = Image.open(file_p)

text = pytesseract.image_to_string(img, lang=app.option_menu)

print(text)

