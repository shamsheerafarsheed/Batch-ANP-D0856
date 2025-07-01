def calculate_total(bill_amount,tax=0.05):
    return bill_amount+(bill_amount*tax)
print("Total amount:",calculate_total(1000))

def find_grade(marks):
    avg=sum(marks)/len(marks)
    if avg>=90:
        return "A"
    elif avg>=80:
        return "B"
    elif avg>=50:
        return "C"
    else:
        return "Fail"
print("Grade:",find_grade([60,70,90,75]))
        
    
    

    
    
