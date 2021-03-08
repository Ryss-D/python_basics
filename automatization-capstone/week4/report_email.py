#!/usr/bin/env python3

import os
from datetime import datetime
import reports
import emails

if __name__ == "__main__":

    path = 'supplier-data/description'
    info = list()
    attachment = "/tmp/processed.pdf"
    current_date = datetime.today().strftime('%Y-%m-%d')
    title = f"Precessed Update on {current_date}"

    for sheet in os.listdir(path):
        with open(os.path.join(path, sheet)) as txt:
            lines = txt.readlines()
            data = dict()
            data["name"] = lines[0].rstrip()
            data["weight"] = lines[1].rstrip()
            info.append(data)

    data = ''

    for item in info:
        data += "\n"
        name = item["name"]
        weight = item["weight"]
        data += f"name:{name}\n"
        data += f"weight:{weight}\n"

    reports.generate_report(attachment, title, data)
    
    message = emails.generate_email("student-04-7d2328391f41")

    emails.send_email('student-04-7d2328391f41', '2fYVCD56sB', message)
