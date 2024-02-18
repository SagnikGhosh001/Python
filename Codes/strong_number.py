num=int(input("enter the number:-"))
num1=num
sum1=0
while(num!=0):
    rem=num%10
    fact=1
    i=1
    while(i<=rem):
        fact=fact*i
        i=i+1
    sum1=sum1+fact
    num=num//10
if(sum1==num1):
    print("this is a strong number")
else:
    print("this is not a strong number")
