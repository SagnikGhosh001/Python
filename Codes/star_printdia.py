for i in range(1,4):
    for j in range(1,6):
        if (j>=4-i and j<=2+i):
            print("*",end='')
        else:
            print(" ",end='')
    print("\n",end='')
for i in range(4,5):
    for j in range(1,6):
        if(j>=6-i and j<=i):
            print("*",end='')
        else:
            print(" ",end='')
    print("\n",end='')
for i in range(5,6):
    for j in range(1,6):
        if(j>=8-i and j<=8-i):
            print("*",end='')
        else:
            print(" ",end='')
    print("\n",end='')
