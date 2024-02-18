#add two number and check the sum is even or odd
def add(a,b):
    return(a+b)
def oddeven(x):
    if x%2==0:
        print("EVEN")
    else:
        print("ODD")
# p=int(input("Enter the first number:-"))
# q=int(input("Enter the second number:-"))
print("Enter two numbers:-")
p,q=[int(x) for x in input().split()]
oddeven(add(p,q))