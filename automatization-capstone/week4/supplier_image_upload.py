#!/usr/bin/env python3

import requests
import os

ip = '34.67.175.241'

url = f"https://{ip}/upload"

for image in os.listdir(f"~/supplier-data/images"):
    if image.endswith('.jpeg'):
        with open(f"~/supplier-data/images/{image}", 'rb') as opened:
            r = requests.post(url, files={'file' : opened})
