class InsufficientFunds(Exception):
    pass
balance=5000
withdraw=int(input("Enter the amount to withdraw"))
try:
    if withdraw>balance:
        raise InsufficientFunds("not enough Balance")
    balance-=withdraw
    print("withdraw is successful:Remaining balance is:", balance)
except InsufficientFunds as e:
    print(e)
    
             
