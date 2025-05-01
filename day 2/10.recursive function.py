#recursive function

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)
n = int(input("enter a number:"))
res = fact(n)
print("factorial of", n ,"is",res)


#sum of two numbers using recursion
def sum(a,b):
    if b==0:
        return a
    else:
        return sum(a+1,b-1)
a=int(input("enter first number:"))
b=int(input("enter second number:"))
res=sum(a,b)
print("sum of",a,"and",b,"is",res)

def sum(a,b):
    if b==0:
        return a
    else:
        return sum(a+1,b-1)
print(sum(10,20))
#fibonacci
#gcd