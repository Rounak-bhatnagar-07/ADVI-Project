#more than one datatype (different data types)
a=[10,78,45,23,56,78,90]
print(a)
print(type(a))

a.append(99)         #list can store duplicate value but set won't
a.append(10)
print(a)
print(len(a))
for i in range (len(a)):
    print(a[i])
    
#sum of even  and odd elements in alist
a=[10,78,45,23,56,78,90]
even_sum=0
odd_sum=0
for i in range (len(a)):
    if a[i]%2==0:
        even_sum=even_sum+a[i]
    else:
        odd_sum=odd_sum+a[i]
print("even_sum=",even_sum)
print("odd_sum=",odd_sum)