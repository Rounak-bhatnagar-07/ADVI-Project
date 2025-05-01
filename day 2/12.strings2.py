s1=input("enter a string: ")

for i in range(len(s1)):
    for j in range(i+1):
        print(s1[j],end=" ")
    print()
    
    
    
s1=input("enter a string: ")
for i in range(len(s1)):
    for j in range(len(s1)-i):
        print(s1[j],end=" ")
    print()
    
s1=input("enter a string: ")
print(s1)

print(len(s1))
for i in range(-len(s1),0):
    print(s1[i])