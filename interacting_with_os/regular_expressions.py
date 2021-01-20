import re
log = "string"
regex = r"\[(\d+)\]" #r mean is a raw string and is a good idea alwas use it at regular expresons
result = re.search(regex, log)#return first match
print(result[1])
#grep print any line who match the regular expresion 
#grep re directory or file
re.search(regex, log, re.IGNORECASE)#ignore case
#regex = "cat|dog" will match car or dog
#? means zero or one cocurrence for the term
#^ ah start [^] not this character $at the end of string \ is a scape character to find especial characters
#example of check variable names

pattern = "^[a-zA-Z_][A-Za-z0-9]*$"

result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
#we can make matchs by groups
print(result)
print(result.groups())
print(result[0])# correspond to all match
print(result[1])# correspond to first group
print(result[2])#correspond to secon group
print(re.search(r"[a-zA-Z]{5}", "a ghost"))# thats a way to match exactly 5 repetitons
# we can split string using regular expresions with the command re.split
# we also can use create sub strings from others using the re.sub command, in example replacing
