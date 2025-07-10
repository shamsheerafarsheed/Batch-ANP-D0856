#Finally
try:
    print("Trying to open a file...")
    f=open("demo.txt","r")
    print(f.read())
except FileNotFoundError:
    print("File not Found")
finally:
    print("Closing file(if opened).")
