import random
def generateRandomNumber():
    return  random.randint(1,100)
sum=0
for i in range (10):
    sum=sum+generateRandomNumber()
print("sum=",sum)


import random
def generateRandomNumber():
    return  random.randint(1,100)
sum=0
for i in range (10):
    x=generateRandomNumber()
    print(x)
print("sum=",sum)