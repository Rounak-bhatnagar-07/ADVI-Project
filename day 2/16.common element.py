#display common elements in alist  

list=[10,20,30,40,50,60]
list2=[20,50,45,77,11,33,40]
list3=[]
for i in list:
        if i not in list2:
            list3.append(i)
print(list3)
