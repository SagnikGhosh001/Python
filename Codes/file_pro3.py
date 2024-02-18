

# Getting the integer file descriptor 
f = open('file2.txt', 'r') 
#next() 
try: 
    while f.next(): 
        print(f.next()) 
except: 
    f.close()