lst = []
even = 0
odd = 0
n = int(input("enter no of elements:"))
for i in range(0, n):
    element = int(input("enter the element:"))
    lst.append(element)
print("before sort", lst)
for i in range(0, n):
    if lst[i] % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
print("even =", even)
print("odd =", odd)
