#String Functions and methods
#1.upper-->convert all letter s to upper case
text="   anudip"

print(text.upper())
#try lower
#title
print(text.title())
#Capitalize
print(text.capitalize())

#strip-->remove whitespace
print(text.strip())
#replace->(old,new)
text1="I love Java"
print(text1.replace("Java","Python"))
#split-->split sentences into list

veg="Cucumber,Onion,Cabbage,Chiily"
print(veg.split(","))
#join--->join elements of a list into single string

veg1=['Cucumber','Onion','Cabbage','Chiily']
print("_".join(veg1))
#startwith/endwith
name="Anu anil"
print(name.startswith("Anu"))
#find-->return the index of the first occurance of a substring-return -1 if not found
print(name.find("anil"))
#count--how many times a substring appears
feedback="i have good students in my class,they are good in domain"
print(feedback.count("good"))
#len(),isdigit,isalpha()




