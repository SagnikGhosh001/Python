a=input("enter the value of a: ")
if(a>='0' and a<='9'):
    print("this is a number")
elif ((a>='a' and a<='z') or (a>='A' and a<='Z')):
    print("this is a alphabet")
else:
    print("this is a special character")
