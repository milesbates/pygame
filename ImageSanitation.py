import os
from PIL import Image
import shutil


dir_path = "images\GUI"
image = Image.open(os.path.join(dir_path,'MainMenu.png'))
image = image.convert('RGBA')
dat = image.getdata()
newDat = []

for item in dat:
    if item[0] in list(range(255,256)):
        newDat.append((255,255,255,0))
    else:
        newDat.append(item)
image.putdata(newDat)
image.save(os.path.join(dir_path,'MainMenu.png'),"PNG")