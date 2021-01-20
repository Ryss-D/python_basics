#!/usr/bin/env python3
import re
import os
import csv
import glob
import operator

def system_errors_ranking(path):
    
    #All the error mensages and how many times each error was found
    #sorted by most common to least common

    log_info = process_log_files(path)
    errors = {}

    for pack in log_info:
        if pack["type"] == 'INFO':
            continue
        else:
            errors[pack["message"]] = errors.get(pack["message"], 0) + 1

    write_report(sorted(errors.items()), 'error_menssage', ['Error', 'Count'])

    return None

def user_usage_statics(path):
    
    #List of all usersthat have used the system and hjow many info mensagges and error they have generated
    #Sorted by user name

    log_info = process_log_files(path)
    users = {}
    
    for pack in log_info:
        if pack["type"] == 'INFO':
            users[pack["user"]]["info"] = users[pack["user"]].get("info", 0) + 1
        elif pack["type"] == 'ERROR':
            users[pack["user"]]["error"] = users[pack["user"]].get("info", 0) + 1




    write_report(sorted(users.items(), key=operator.itemgetter(0)), 'user_statistics',['Username', 'INFO', 'ERROR'])

    return None

def extract_data(input_data):
    
    extracted_data = {}
    
    regex = {"type" : r"ticky:\s([A-Z]*)",
        "message" : r"[A-Z]{4,5}\s([A-Za-z0-9\[\]#\s]*)",
        "user" : r"\(([\w]*)\)"}
    
    for key in regex.keys():
        data = re.search(regex[key], input_data)
        extracted_data[key] = data[1]
        if data[1] == 'INFO':
            break
        else:
            continue
    return extracted_data

def write_report(data, name, columns):
    
    if name == 'error_menssage':
        with open('{}.csv'.format(name), 'w') as report:
            writer = csv.DictWriter(report, fieldnames=columns)
            writer.writeheader()
            for k,v in data:
                writer.writerow({"Error" : k, "Count" : v})
                
    elif name == 'user_statistics':
        with open('{}.csv'.format(name), 'w') as report:
            writer = csv.DictWriter(report, fieldnames=columns)
            writer.writeheader()
            for k, v in data:
                writer.writerow({"Username" : k, "Error" : v["error"], "info" : v["info"]})
    return None

def process_log_files(path):

    # files_to_check = glob.glob('{}'.format(path))
    files_to_check = ['sys.log']
    file_content = []

    for log_file in files_to_check:

        with open(log_file, "r") as f:
            for row in f:
                row_content = extract_data(row)
                file_content.append(row_content)
            f.close()

    return file_content

# test_data = "May 27 11:45:40 ubuntu.local ticky: INFO Created ticket [#1234] (username)"
# test_output = extract_data(test_data)
# print(test_output)

# if __name__ == "__main__":
path = 'sys.log'
system_errors_ranking(path)
user_usage_statics(path)