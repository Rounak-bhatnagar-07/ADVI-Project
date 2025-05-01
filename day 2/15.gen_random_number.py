#genereate 10 random no. without duplicates btw 1 to 50 
import random
a=[]
i=1
while i<=10:
    num=random.randint(1,50)
    print(i,"---",num)
    if num not in a:
        a.append(num)
        i+=1
print(a)