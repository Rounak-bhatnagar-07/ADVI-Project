import random
def generateRandomNumber():
    return random.randint(1,100)

for i in range(10):
    print(generateRandomNumber())
    
    #function without argument and no return type