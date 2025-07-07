# input registers
registered = set()
attended = set()

n = int(input("Enter the number of registered users: "))
print("Enter names of registered users:")
for _ in range(n):
    registered.add(input().strip())

m = int(input("Enter the number of users who will attend the event: "))
print("Enter names of attendees:")
for _ in range(m):
    attended.add(input().strip())

# Find who registered but didn't attend
absentees = registered - attended

print("\nList of users who registered but didn't attend:")
for name in absentees:
    print(name)
      
      
      
      
