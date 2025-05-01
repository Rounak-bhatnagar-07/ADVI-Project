def sum(a,b):
    print("a=",a)
    print("b=",b)
    sum=a+b
    print("sum=",sum)
sum(10,20)


def sum(a,b,c=1):
    print("a=",a)
    print("b=",b)
    print("c=",c)
    sum=a+b+c
    print("sum=",sum)
sum(10,20,30)
sum(10,20)

def sum(a=1,b=1,c=1):    #right most variable should be assigned 
    print("a=",a)
    print("b=",b)
    print("c=",c)
    sum=a+b+c
    print("sum=",sum)
sum(10,20,30)
sum(10,20)
sum()