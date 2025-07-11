#File I/O-->we can read or write the file using python
''' use:storing data permanantly
   reading data from .txt,.csv etc
   writing o/p of a pgm
   common modes
   'r'-->read
   'w'-->write
   'a'-->Append
   'x'-->create
   'b'-->Binary mode
   't'-->text mode
   '+'--->read and write
'''
'''opening a file
#open(file_name,mode)
#read()--read entire content
file.read()
readline()-->read one line at atime
#readlines()-->read all lines into a list
#write()-->write a single string
writelines()-->write list of string
'''
import os
if os.path.exists("datas.txt"):
    print("File exists")
else:
    print("File not exists")
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
