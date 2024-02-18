lst=[2,8,3,5,7,4,1,2]
unit=2
r=7
sum=0
for i in range (0,8):
    sum=sum+lst[i]
    if(sum>=(unit*r)):
        break;
print(i+1)
