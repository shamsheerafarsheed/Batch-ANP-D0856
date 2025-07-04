#Tuple is ordered,immutable(we cant change),hetrogenious  colection of elements
#creating tuple using-->()
my_tuple=(10,"python",3.14,True)
print(my_tuple)
#tuple without paranthesis
tpl1=1,2,3,4,5
print(tpl1)
print(type(tpl1))
#Accessing tuple elements(0 based index)
print(my_tuple[1])
#slicing
num=(10,20,30,40,50)
print(num[1:4])
print(num[:4])#start from 0
print(num[1:])#print till end
#tuple is immutable
#num[1]=25
#print(num)#it will raise an error
#concatenation
num1=(11,23,34,56)
result=num+num1
print(result)
repeat_tuple=("Pthon",)*4

print(repeat_tuple)
#tuple unpacking
person=("Govardhan",21,"Student")
name,age,profession=person
print(name)
#count,index

#convert tuple to list
num_list=list(num1)
print(num_list)
print(type(num_list))


