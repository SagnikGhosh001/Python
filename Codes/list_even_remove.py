lst=[]
n=int(input('Enter the elements no:-'))
for i in range(0,n):
    element=int(input('Enter the element:-'))
    lst.append(element)
    if(element%2==0):
        lst.remove(element)
print("only odd:-",lst)
    
