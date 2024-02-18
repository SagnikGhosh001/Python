import copy
a=[6,5,8,3,34,56,2,4,3,21,1]
b=copy.copy(a)
print('shallow copy:-',b)
c=copy.deepcopy(a)
print('deep copy:-',b)
