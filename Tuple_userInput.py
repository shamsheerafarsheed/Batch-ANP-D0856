#to collect Students details and store them in atuple
num_Students=int(input("Enter the number of students?:"))
student_data=[]
for i in range(num_Students):
    name=input(f"Enter the name of the student{i+1}:")
    marks=float(input(f"Enter marks of{name}:"))
    student=(name,marks)
    student_data.append(student)
#Display the data
print("\n Student Details:")
for student in student_data:
    print(f"Name:{student[0]},Marks:{student[1]}")
#highest score
topper=max(student_data,key=lambda x:x[1])
print(f"Topper is:{topper[0]} with {topper[1]}marks.")

    
