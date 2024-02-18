lst=[]
j=0
n=int(input("enter no of elements:"))
for i in range(0,n):
    element=int(input("enter the element:"))
    lst.append(element)
print("before sort",lst)
for i in range(0,n):
    for j in range(i+1,n):
        if(lst[i]<lst[j]):
            temp=lst[i]
            lst[i]=lst[j]
            lst[j]=temp
print("after sort",lst)



