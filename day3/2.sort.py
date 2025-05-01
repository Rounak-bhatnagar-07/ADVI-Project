#program to sort the elements of the list using functions
def sort_list(list1):
    for i in range(len(list1)-1):
        for j in range(i+1,len(list1)):
            if list1[i]>list1[j]:
                list1[i],list1[j]=list1[j],list1[i]
    return list1
list1=[15,89,23,45,67,12,34,56,78]  
sorted_list=sort_list(list1)
print("sorted list is:",sorted_list)
