import os

os.remove("file.extension")#that remove the file
os.rename("file_old_name", "file_new_name") #rename files
os.path.exists("path to file")
os.path.getsize("path to file")
os.path.getmtime("path to file") #last time was modify (Timestamp from 1 january 1970)
os.path.abspath("file")#look for the path of the file specified

print(os.getcwd())#give us the curren directory (if unix sistem we sould use pwd)
os.mkdir #same as unix
os.chdir("file path")#change the current directory
os.rmdir("path") #just will work if we have a empty directory
os.listdir("path") #return a list of subdirectories and files
os.path.isdir("path") #check if path is a directory 
os.path.join("paht")#It creates a string containing cross-platform concatenated directories.
