lst=[]
even=[]
odd=[]
n=int(input("enter no of elements:"))
for i in range(0,n):
    element=int(input("enter the element:"))
    lst.append(element)
for i in range(0,n):
    if(lst[i]%2==0):
        even.append(lst[i])
    else:
        odd.append(lst[i])
print("even=",even)
print("odd=",odd)



