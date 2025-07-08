# Dictionary to store student data
students = {
    "101": {"name": "Alice", "course": "BCA", "marks": 85},
    "102": {"name": "Bob", "course": "BBA", "marks": 78},
    "103": {"name": "Charlie", "course": "BCom", "marks": 92}
}

# Function to display student data by roll number
roll_no = input("Enter student roll number: ")

if roll_no in students:
    print("Student Details:")
    print(f"Name: {students[roll_no]['name']}")
    print(f"Course: {students[roll_no]['course']}")
    print(f"Marks: {students[roll_no]['marks']}")
else:
    print("Student not found!")
