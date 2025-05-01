#slicing [start:end:step]

s1="keyboard"
print(s1)
print(s1[2:4])
print(s1[:5])
print(s1[2:])
print(s1[0:len(s1):2])

#-ve indexing
print(s1[-6:-1])
print(s1[-6:-2])
print(s1[::-1])


s1="computer"
for i in range(len(s1)):
    print(s1[:i+1])
for i in range(len(s1),0,-1):
    print(s1[:i])