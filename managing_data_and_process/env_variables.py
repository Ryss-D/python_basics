#we can acces to variable enviroments usin os

import os

print("home" + os.environ.get("home", ''))#like a dictionary
#if we want to define a enviromen variable uy use export variable=value
import sys
print(sys.argv)#give us information about the parameters passed
#we can acces from script to arguments passed like on a list ieg sys.argv[1]
#Exit estatus is a value retornet from program to shell 0 means no erros and (Different of zero) 2 means erros
#$? in shell let us now the last command exit estus "echo $?"
#wc command let us now the number of lines, words and letters on a file
#we can select the exits status into the script with sys.exit(code) ieg sys.exit(1)
#we can call eval() on pytho to execute string as expresions

#we can excecutes system commands from python

import subprocess

#subprocess.run(["date"])

#result = subprocess.run("ls", "this file does not exists")
#print(result.returncode)#this is the way to acces return code

result = subprocess.run(["host", "8.8.8.8"], capture_output = True)
print(result.returncode)
print(result.stdout.decode().split())#we can call for stderr attribute too