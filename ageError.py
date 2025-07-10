#raise
try:
    age=int(input("Enter your age??"))
    if age<18:
            raise Exception("You are not eligible for vote")
    print("Yes,You are  eligible for vote")
except Exception as e:
    print("error",e)
