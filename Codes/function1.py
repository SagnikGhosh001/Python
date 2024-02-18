def calculateGmean(a,b):
    mean=(a*b)/(a+b)
    print(mean)
def isGreater(a,b):
    if(a>b):
        print("first number is greater")
    else:
        print("Second number is greater or equal")
def isLesser(a,b):
    pass #write it on future
a=float(input("Enter the first number:-"))
b=float(input("Enter the second number:-"))
calculateGmean(a,b)
isGreater(a,b)
c=float(input("Enter the first number:-"))
d=float(input("Enter the second number:-"))
calculateGmean(c,d)
isGreater(c,d)

