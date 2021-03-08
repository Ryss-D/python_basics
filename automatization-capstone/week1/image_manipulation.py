
from PIL import Image #library to manipulate images
im = Image.open("bride.jpg")
im.rotate(45).show

#other examples

new_im = im.resize((640,480))
new_im.save("example_resized.jpg")

## exercise
#!usr/bin/env python3
import os
from PIL import Image

place = "/home/student-01-ec18ffebbebc/images"

for filename in os.listdir(place):
    im = Image.open(os.path.join(place, filename))
    im.rotate(90).resize((128,128)).save(f"/home/student-01-ec18ffebbebc/opt/icons/{filename}.jpg")

