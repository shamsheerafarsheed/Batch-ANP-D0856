#else
try:
    num=int(input("Enter a number:"))
    result=100/num
except ZeroDivisionError:
    print("Cant divide by zero")
else:
    print("Result is:",result)
