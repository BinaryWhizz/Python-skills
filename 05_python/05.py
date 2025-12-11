x = [1,4,2,5,3,6,4,7,7,8]
y = {1,4,2,5,3,6,4,7,7,8} 

print(y)                     # {1, 2, 3, 4, 5, 6, 7, 8} , removes duplicates in set 


s = set(range(10))

print(s)

# Searching in list takes a lot of time if the list is big than searching in set , set is easy


import sys

x = list(range(100))
y = set(range(1000))

print(sys.getsizeof(x))    # size is not same as number of elements, it's basically the size of memory allocation 
print(sys.getsizeof(y))


z = {'A','B','C','D','E','F'}

z.add("Z")

print(z)