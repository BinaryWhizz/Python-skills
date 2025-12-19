# Functional programming part 1


fruits = ['mango', 'apple', 'banana', 'orange', 'pineapple', 'watermelon', 'guava', 'kiwi']

# for i in fruits:
#     print(i)


bascket = iter(fruits)

print(bascket)            # <list_iterator object at 0x000001E18AF505B0>, originally fruit was a list then it become iterator 
                          # collectively it become list iterator object 

print(next(bascket))      # mango
print(next(bascket))      # apple
print(next(bascket))
print(next(bascket))
print(next(bascket))
print(next(bascket))
print(next(bascket))
print(next(bascket))      # ... upto "kiwi"

# print(next(bascket))      # Shows error because there is no item next to kiwi 


# Generator 

# We can generate our own iterator 

def square(limit):
    x = 0
    while x < limit:
        yield x * x
        yield x * x * x
        x += 1  

a = square(5)
print(next(a), next(a))            # 0 0
print(next(a), next(a))            # 1 1
print(next(a), next(a))            # 4 8 
print(next(a), next(a))            # 9 27

# This is how combination of Generator and Iterator works together 

