a=int(input("Enter the 1st number: "))
b=int(input("Enter the 2nd number: "))
c=int(input("Enter the 3rd number: "))
if(a>b and a>c):
    print("a is greater")
elif(b>c and b>a):
    print("b is greater")
else:
    print("c is greater")
