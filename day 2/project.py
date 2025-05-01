#phonenumbers from website
import re,urllib
import urllib.request #extract data
text=urllib.request.urlopen("https://www.sphoorthengg.ac.in/")
data = text.read()
numbers=re.findall("[0-9][6-9]{10}",str(data))

for number in numbers:
    print(number)
    
    

