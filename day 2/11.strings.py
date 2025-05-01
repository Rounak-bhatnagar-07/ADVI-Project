s1='good'                   #index value starts from 0
s2='morning'
s3=s1+s2
print(s3)

s1='sachin'
print(s1)
for i in s1:
    print(i)
    
print(len(s1)) 
for i  in range (len(s1)):
    print(s1[i])

#nested  loop of string
for i in s1:
    for j in s2:
        print(i,j)