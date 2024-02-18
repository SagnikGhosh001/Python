#check a given no is prime or composite
count=0;
n=int(input("Enter the number"))
for i in range (1,n+1):
    if(n%i==0):
        count=count+1
if(count==2):
    print("it is prime number")
else:
    print("it is composiyte number")
