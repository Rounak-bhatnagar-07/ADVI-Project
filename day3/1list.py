#program to display the elements of the list using functions
def display(list1):
    for i in list1:
        print(i)
list1=[10,20,30,40]
display(list1)

#find the maximum element of the list using functions
def find_max(list1):
    max1=list1[0]
    for i in list1:
        if i>max1:
            max1=i
    return max1
list1=[11,22,33,44,55,66,77,88,99]
max1=find_max(list1)
print("maximum element of the list is:",max1)

#write a code to find second largest element of the list using functions dont use predefined function 
def find_second_largest(list1):
    max1=list1[0]
    second_max1=list1[0]
    for i in list1:
        if i>max1:
            second_max1=max1
            max1=i
        elif i>second_max1 and i!=max1:
            second_max1=i
    return second_max1
list1=[11,22,33,44,55,66,77,88,99]
second_max1=find_second_largest(list1)
print("second largest element of the list is:",second_max1)

#call by value & call by reference
def modify(x):
    x=x+10
x=10
print("before modify x:",x)
modify(x)
print("after modify x:",x)

def modify(a):
    for i in range(len(a)):
        a[i]=a[i]+10
listt1=[10,20,30,40,50]
print("before modify listt1:",listt1)
modify(list1)
print("after modify listt1:",listt1)
modify(list1)
