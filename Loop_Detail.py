
correct_pin="1234"
attempts=0
entered_pin=""
while entered_pin!=correct_pin and attempts<3:
    entered_pin=input("Enter your ATM PIN:")
    attempts+=1
if entered_pin==correct_pin:
    print("Access Grnated")
else:
    print("Try later..Too many Wrong attemps.")
    
    
