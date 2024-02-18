file=open("file1.txt",'r')
for each in file:
    file1=open("file2.txt",'a')
    file1.write(each)
    print(each)
file1=open("file2.txt",'a')
file1.write(each)
file.close()
