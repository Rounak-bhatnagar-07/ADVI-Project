#program to find frequecy of elements in a list
list1=[1,2,2,3,3,3,4,5,6,6]

for i in list1:
    if list1.count(i)>1:
        print(i,"occurs",list1.count(i),"times")
    else:
        print(i,"occurs",list1.count(i),"time")