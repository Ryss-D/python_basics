#! /usr/bin/env python3

import os
import requests

ip = '34.123.188.150'
path = '/data/feedback'
mensagge = dict()

for feedback in os.listdir(path):
    with open(os.path.join(path, feedback)) as txt:
        lines = txt.readlines()
        mensagge["title"] = lines[0].rstrip()
        mensagge["name"] = lines[1].rstrip()
        mensagge["date"] = lines[2].rstrip()
        mensagge["feedback"] = lines[3].rstrip()
        requests.post("{}/feedback".format(ip), data=mensagge)