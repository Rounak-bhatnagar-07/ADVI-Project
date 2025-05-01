#maximum of two number using lambda
f=lambda a,b :a if a>b else b
x=int(input("Enter first number:"))
y=int(input("Enter second number:"))
print("max=",f(x,y))