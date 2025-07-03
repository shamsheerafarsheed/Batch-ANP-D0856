#collection of ordered ,mutable(change) and hetrogenious elements
#store integers,Strings,float or even other list or object i list
#Lst name=["aisha",20,5.5,True]
#insertion order
#duplicates
empty_list=[]
numbers=[1,2,3,4]
names=["Sahil","Prachi","Joshva","kiran","joshva","joshva"]
mixed=["aisha",20,5.5,True]
#Accessing list elements
print(names[1])
print(names[1:3])
#looping
for name in names:
    print(name)
#append(add at the end)
print("-----------append(add at the end)--------")
print(names)
names.append("Venkat")
print("After appending:",names)
print("-----------Insert(add at the position)--------")
names.insert(2,"Suresh")

print("After insertion:",names)
print("-----------Remove(by value)--------")
names.remove('Sahil')
print("After remove name('sahil'):",names)
#print("-----------pop(by index)--------")
removed_items=names.pop(3)
print(removed_items)

print("-----------Index(find the position ofvalue)--------")
position=names.index("joshva")
print(position)
print("-----------Count(no of occurance)--------")
names_Count=names.count('joshva')
print("Count :",names_Count)
print("-----------Sort(ascending order)--------")
numbers.sort()
names.sort()
print(names)
print(numbers)
print("-----------reverse--------")
names.reverse()
print(names)
print("-----------Length--------")
print("Length of the list:",len(mixed))
print("-----------Concatenation--------")
list1=[11,22,56]
list2=[10,34,55]
result=list1+list2
print(result)
print("-----------Repetation--------")
result1=list1*3
print(result1)
print("-----------membership(in,not in)--------")
print("-----------List Comprehension(special usage)--------")
#creating new list from existing one
square=[x*x for x in list1]
print(square)
#realtime usage

students=["Sahil","Prachi","Joshva","kiran","joshva","joshva"]
name="pooja"
if name in students:
    print(f"{name} is present")
else:
    print(f"{name} is Absent")
print("-----------List inside list--------")
employee=[["Amith",21],["Anu",31]]
for employees in employee:
    print(f"{employee[0][0]}age{employee[0][1]}")






 


