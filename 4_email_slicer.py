#Python Email Slicer
#Splits the email into two parts: username and domain name
#Example:
#username@domain.com ----> username + domain

Email_Input = input("What is your email?: ")
if "@" in Email_Input:
    Index = Email_Input.index("@")
    Username = Email_Input[:Index]
    Domain_Name = Email_Input[Index + 1:]
    print(f"Username: {Username}")
    print(f"Domain Name: {Domain_Name}")
else:
    print("Please enter a valid email address.")