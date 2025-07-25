''' def function_name(parameter):
    function body
    return value
    '''
def show():
    print("Learning function")
show()#calling fn
print("------Function with parameter-----------")
def add(a,b):
    return a+b
result=add(11,13)
print(result)

print("------Function with Default parameter-----------")
#if parameters is not provided,the fn uses default value
def greet(name="Guest"):
    print(f"Hello,{name}!")
greet("Sahil")
greet()
print("------Function with retun value-----------")
print("------Variable length Argument(* args,** args) -----------")
#* args-->used to pass multiple arguments as tuple
#** args--->used to pass multiple key-value pair as dictionary
def sum_all(*numbers):
    return sum(numbers)
print(sum_all(11,25,30,4,5))#15

print("Keyword arguments")
def person_info(**details):
    for key,value in details.items():
        print(f"{key}:{value}")
person_info(name="Ananaya",age=21,city="Banglore")
print("------Lambda Function-----------")
#small one line function without name
#Syntax:lambda argument:expression
square=lambda s,t:s*t
print(square(25,5))
print("------Recursion Function-----------")
#Recursion function call itself until base condition met
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))
        





    

    
