#List with Duplicate Email list
email_list=["use1@gmail.com","use2@gmail.com","use3@gmail.com",
            "use4@gmail.com","use5@gmail.com","use6@gmail.com",
            "use1@gmail.com"#duplicate
            "use2@gmail.com"#duplicate
            "use7@gmail.com"
            "use1@gmail.com"]#duplicate
print(email_list)
#converting list to set for remove duplicates
unique_emails=set(email_list)
print("Unique Emails:")
print(unique_emails)
      
