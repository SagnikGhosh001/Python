#1
a=int(input("Enter a number:-"))
print("The multipication table is:-")
for i in range(0,11):
   print(a,"X",i,"=",a*i)
#2
for i in range(-11,0):
   print(i,end=' ')
3
n=int(input("Enter the range:-"))
for i in range(2,n+1):
   c=0
   for j in range(1,i+1):
       if(i%j==0):
           c=c+1
   if (c==2):
       print(i,end=' ')
4
n=int(input("Enter a number:-"))
fact=1
for i in range(1,n+1):
   fact=fact*i
print("The factorial is",fact)
5
n=int(input("Enter the range:-"))
even=odd=0
for i in range (1,n+1):
   num=int(input("Please enter a number:-"))
   if(num%2==0):
       even=even+1
   else:
       odd=odd+1
print("The number of even number is",even,"The number of add number is",odd)
6
lst=[1,2,3,24,5,16,7,8]
temp=lst[0]
for i in lst:
   if(i>temp):
       temp=i
print(temp)
7
lst1=[3,6,1,8,1,2,7,4,78,13,90]
lst2=[1,8,13,34,12,78,54,67,76]
for i in lst1:
   for j in lst2:
       if(i==j):
           print(i,end=" ")
8(i)
c=1
for i in range (1,5):
   for j in range  (1,5):
       if(j<=i):
           print(c,end=" ")
           c=c+1
       else:
           print(" ",end=" ")
   print("\n",end=" ")
8(ii)
for i in range (1,5):
   for j in range  (1,i+1):
       if((i+j)%2==0):
           print("0",end=" ")
       else:
           print("1",end=" ")
   print("\n",end=" ")
8(iii)
for i in range (1,5):
   for j in range  (1,5):
       if(i<=j):
           print("*",end=" ")
       else:
           print(" ",end=" ")
   print("\n",end=" ")
