#create new file using 'w' mode-->new file will creates,if already exists overites the content
file=open("Anudip.txt","w")
file.write("this is the new file created using 'w' mode")
file.close()

'''#create new file using 'X' mode-->new file will creates,if already exists raise file exist error
file=open("Anudip1.txt","x")
file.write("this is the new file created using 'x' mode")
file.close()
print("file already exist")
'''

#create new filewith open-->automatically close the file
with open("anudip2.txt","w")as file:
    file.write("this is the new file created using open context manager")


