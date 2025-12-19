# Functional programming part 3

def add(x, y):
    return x + y

def sub(x ,y):
    return x - y

def mul(x ,y):
    return x * y

def div(x ,y):
    return x / y

print(add(10, 20))                   # 30
print(sub(10, 20))                   # -10
print(mul(10, 20))                   # 200
print(div(10, 20))                   # 0.5


# or


add = lambda x, y: x + y
sub = lambda x, y: x - y
mul = lambda x, y: x * y
div = lambda x, y: x / y

print(type(add))                     # <class 'function'>

print(add(80, 100))                  # 180
print(sub(100, 50))                  # 50
print(mul(2, 50))                    # 100
print(div(100, 5))                   # 20.0 



# Enumerate 

fruits = ['mango', 'apple', 'banana', 'orange', 'pineapple', 'watermelon', 'guava', 'kiwi']

for i in fruits:
    print(i) 

for i in range(len(fruits)):
    print(i, fruits[i])             # 0 mango
                                    # 1 apple
                                    # 2 banana
                                    # 3 orange
                                    # 4 pineapple
                                    # 5 watermelon
                                    # 6 guava
                                    # 7 kiwi


for i in enumerate(fruits):
    print(i)                        # (0, 'mango')
                                    # (1, 'apple')
                                    # (2, 'banana')
                                    # (3, 'orange')
                                    # (4, 'pineapple')
                                    # (5, 'watermelon')
                                    # (6, 'guava')
                                    # (7, 'kiwi')



fruits = ['mango', 'apple', 'banana', 'orange', 'pineapple', 'watermelon', 'guava', 'kiwi']

size = [5, 5, 6, 9, 10, 5, 4]       # Length of string values stored in the same order as these fruit names are stored 

print(zip(fruits, size))            # <zip object at 0x0000019FF4AEF4C0>
print(list(zip(fruits, size)))      # [('mango', 5), ('apple', 5), ('banana', 6), ('orange', 9), ('pineapple', 10), ('watermelon', 5), ('guava', 4)]

print(dict(zip(fruits, size)))      # {'mango': 5, 'apple': 5, 'banana': 6, 'orange': 9, 'pineapple': 10, 'watermelon': 5, 'guava': 4}


a = [10, 20, 30, 40, 50, 60]
b = [5, 10, 15, 20, 25, 30] 

# c = a - b 

# print(c)           # Error 

# only possible element in a or b - element in a or b

c  = a[0] - b[0] 

print(c)                  # 5 


def sub(x, y):
    return x - y 

c = map(sub, a, b)

print(c)                  # <map object at 0x0000017869F0EE80> 

print(list(c))            # [5, 10, 15, 20, 25, 30]

# map function takes 2 different types arguments, first is function name , a & b are iterators 
# map function will iterate over these two lists and at the same time it will execute this function for every single entry 
# inside these two lists a & b 



a = [10, 20, 30, 40, 50, 60]
b = [5, 10, 15, 20, 25, 30] 

def sub(x, y):
    return x - y 

def incr(x):
    return x + 1 

c = map(sub, a, b)
c = map(incr, a)                 # Here, c = a + 1 , Every element in c will be increased by + 1 

print(list(c))                   # [11, 21, 31, 41, 51, 61]  




# import math 

# a = [25, -16, 9, 81, -100]

# def square_root(n):
#     return math.sqrt(n)

# c = map(square_root, a)

# print(list(c))                      # Error because of these -16 and -100, negative numbers 


# Correct way 

import math 

a = [25, -16, 9, 81, -100]

def square_root(n):
    return math.sqrt(n)

def is_positive(n):
    if n >= 0:
        return n 

c = map(square_root, filter(is_positive, a))    # Skipping -16 and -100 
 
print(list(c))                                  # [5.0, 3.0, 9.0]
