#!/usr/bin/env python3

import os
from PIL import Image

source_path = "~/supplier-data/images"
destination_path = "~/supplier-data/images"

for image in os.listdir(source_path):
    image = Image.open(os.path.join(source_path, image))
    image.convert('RGB') \
    .resize(600, 400) \
    .save(f"{source_path}/{image}.jpeg")#instead put the \ we can just cover all opration into parentezis and tab after every dot
    
