#!/usr/bin/env python3

import os
import requests

def fix_format(string):
    x = string.split(' ')
    real = x[0]
    real = real.strip()
    real = int(real)
    return real

ip = '34.67.175.241'
path = 'supplier-data/descriptions'
messagge = dict()

for feedback in os.listdir(path):
    with open(os.path.join(path, feedback)) as txt:
        lines = txt.readlines()
        messagge["name"] = lines[0].rstrip()
        messagge["weight"] = fix_format(lines[1].rstrip())
        messagge["description"] = lines[2].rstrip()
        messagge["image_name"] = lines[3].rstrip()
        requests.post(f"{ip}/fruits", data = messagge)