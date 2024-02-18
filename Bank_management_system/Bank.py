details={}
while(1):
    acc=int(input("enter your account number:-"))
    name=input("enter your name:-")
    deposit=int(input("enter your amount:-"))
    details[acc]=name,deposit
    add=int(input("for add more customer press 0:-"))
    if(add!=0):
        break
length=len(details)
list1=list(details.values())
print(list1)
lst=[]
for i in list1:
    element=list(i)
    lst.append(element)
print(lst)
while(1):
    print("ATM MANU")
    print("1.deposit\n 2.withdraw\n 3.exit")
    menu=int(input("enter your choice:-"))
    if(menu==1):
        acc_check=int(input("enter your account number:-"))
        count=0
        for i in details.keys():
            count=count+1
            if(i==acc_check):
                print("welcome",lst[count-1][0])
                deposit1=int(input("Enter ammount to deposit:-"))
                main_balance=deposit1+lst[count-1][1]
                lst[count-1][1]=main_balance
                print("Final balance is:-",main_balance)
                break
            elif(length==count):
                print("Wrong information")
    elif(menu==2):
        acc_check=int(input("enter your account number:-"))
        count=0
        for i in details.keys():
            count=count+1
            if(i==acc_check):
                print("welcome",lst[count-1][0])
                withdraw=int(input("Enter ammount to withdraw:-"))
                if(lst[count-1][1]<withdraw):
                    print("Insuffient ammount")
                    break
                else:
                    main_balance=lst[count-1][1]-withdraw
                    lst[count-1][1]=main_balance
                    print("Final balance is:-",main_balance)
                    break
            elif(length==count):
                print("wrong information")
    elif(menu==3):
        exit()
    else:
        print("Wrong input")