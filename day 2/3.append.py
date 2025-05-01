import random
sum=[]
def generateRandomNumber():
    return  random.randint(1,100)

for i in range (10):
    sum.append(generateRandomNumber())
print(sum,max(sum))
