try:
    pin=int(input("Enetr 4 digit ATM pin"))
    if len(str(pin))!=4:
        raise ValueError("PIN must be 4 digit")
    print("PIN Accepted")
except ValueError as e:
    print("Invalid input:",e)
