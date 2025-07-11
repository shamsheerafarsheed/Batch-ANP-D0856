#Readlines from file
with open("data.txt","r")as file:
    line=file.readline()
    print(line)
print("---Readlines()---")
#Readlines from file
with open("data.txt","r")as file:
    lines=file.readlines()
    for line1 in lines:
        print(line1.strip())

