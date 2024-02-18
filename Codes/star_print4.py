for i in range(1,5):
    for j in range(1,9):
        if j>=i and j<=4+i:
            print("*",end='')
        else:
            print(" ",end='')
    print("\n",end='')
