#write a program to generate vehicle number 
import re
vehicle_number=input("enter a vehicle number to validate:")
#telangana state vehicle number format is TS00AB1234
m=re.fullmatch("[A-Z]{2}[0-9]{2}[A-Z]{2}[0-9]{4}",vehicle_number)

if m!=None:
    print("valid vehicle number")
else:
    print("invalid vehicle number")