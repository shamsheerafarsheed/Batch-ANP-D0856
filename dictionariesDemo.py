'''
Key value pair seperted by colon
create using curly braces'''
#creating Dictionary
student={
    "name":"Mukesh",
    "Afid":"af101",
    "age":20,
    "Course":"WEPP"
    }
print(student)
#empty Dictionary
empty_dict={}
print(type(student))
print(type(empty_dict))
#using dic() constructor
person=dict(name="anusha",city="bnglr")
print(person)
#accessing dictionary valuesusing keys(if key is not exist,it wil raise an error
print(student["name"])
#get()-->avoid error
print(student.get("gender","not found"))
#dict.keys(),dict.values(),dic.del(),dic.items(),dict.pop(),dic.popitem(),dict.clear(),dict.copy()

#modifying a dictionary
print("----------add new key----------")
student["city"]="mumbai"
print(student)
print("----------update an existing key----------")
student["age"]=25
print(student)
print("----------update key----------")
student.update({"city":"banglore","age":30})
print(student)
for key,value in student.items():
    print(f"{key}:{value}")
print("----------dictionary comprehension----------")
squares={x:x**2 for x in range(1,6)}


print(squares)
print("----------nested ----------")
students={
    "stdnt1":{"name":"Mukesh","Afid":"af101","age":20},
    "stdnt2":{"name":"eswari","Afid":"af102","age":21}
    
    
    }
print(students)
print(students["stdnt1"]["name"])

          



      





