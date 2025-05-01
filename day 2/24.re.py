import re
phone_no=input("enter a mobile number to validate:")
m=re.fullmatch("[0-9]{10}",phone_no)
if m!=None:
    print("valid mobile number")
else:
    print("invalid mobile number")