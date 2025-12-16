# tuples

# A tuple is immutable, meaning once it is created, its elements cannot be changed.

t = (1, 2, 3)

print(t[1])      # Can be accessed like lists methods, but cannot append or remove  


# Single-element tuple:

t = (5,)   # comma is mandatory

# A tuple is unchangeable
# A list can be changed 

l = list(range(10))
print(l)

t = tuple(range(10))
print(t)


import string

print(string.ascii_letters)      # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 

print(string.ascii_uppercase)    # ABCDEFGHIJKLMNOPQRSTUVWXYZ 
print(string.ascii_lowercase)    # abcdefghijklmnopqrstuvwxyz 


p = tuple(string.ascii_letters)
print(p)

q = set(p)                       # Converting tuple into set 
print(q)


print(p.__sizeof__())            # 440 
print(q.__sizeof__())            # 2248


# Here in tuple less memory needed than set 

# When we are sure of the list that we are handling and we are also sure that it never changes, then use a tuple 

