files = dict()

import json 

with open('file.json', 'w') as file_json:
    json.dump(files, file_json, indent = 2)#dump fuction serialize objects into a JSON file
#Another option is to use the dumps() method, which also serializes Python objects, but returns a string instead of writing directly to a file.  

##YAML (Yet Another Markup Language) has a lot in common with JSON. They’re both formats that can be easily understood by a human when looking at the contents. In this example, we’re using the yaml.safe_dump() method to serialize our object into YAML:  

with open('files.jason', 'r') as file_json:
    files = json.load(file_json)

#The load() method does the inverse of the dump() method. It deserializes JSON from a file into basic Python objects. The loads() method also deserializes JSON into basic Python objects, but parses a string instead of a file

import yaml

with open('file.yaml', 'w') as file_yaml
    yaml.safe_dump(files, file_json)

# JSON ES COMMONLI USED TO SHARE DATA AND YAML TO STORE CONFIGURATION VALUES


