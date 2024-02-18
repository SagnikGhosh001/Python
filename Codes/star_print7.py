for i in range(1,5):
    for j in range(1,8):
        if j>=5-i and j<=8-i:
            print("*",end='')
        else:
            print(" ",end='')
    print("\n",end='')
