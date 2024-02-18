n=int(input("Enter the value"))
count=0
i1=n
i=i1
amst=0
while(n!=0):
    n=n//10
    count=count+1
while(i!=0):
    rem=i%10
    amst=amst+pow(rem, count)
    i=i//10
if(amst==i1):
    print("it's an Armstrong number")
else:
    print("it's not an Armstrong number")
