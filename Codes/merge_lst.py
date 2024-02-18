lst1=[]
lst2=[]
n1=int(input("enter no of elements of first list:"))
for i in range(0,n1):
    element=int(input("enter the element:"))
    lst1.append(element)
n2=int(input("enter no of elements of 2nd list:"))
for i in range(0,n2):
    element=int(input("enter the element:"))
    lst2.append(element)
print(lst1+lst2)

