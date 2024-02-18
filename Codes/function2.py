def A():
    print("Hello I am A")
    B()
def B():
    print("Hello I am B")
def C():
    print("Hello I am C")
    A()
C()