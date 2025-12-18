# More on sets 

st = {1, 2, 3, 4, 5}

# Set doesn't allow duplicate values 

st = {1, 2, 2, 2, 3, 3, 4, 5, 3, 4, 5}

print(st)           # {1, 2, 3, 4, 5} 

# print(st[0])        # Error, cannot be used like list 

# With respect to mutability set is peculiar, set itself is mutable , but every value inside set has to be immutable and hashable,
# which means you can add values into a set but whatever values which we add, those values has to be immutable.
# Hence, we cannot add a list or a dictionary or a tuple containing a list or a dictionary to a set, because then it will not be 
# immutable as well as hashable.


# Set methods :

A = {1,3,5}
B = {1,2,3,4,5}

print(A.issubset(B))          # True
print(A.issuperset(B))        # False 

C1 = A.union(B)               # Using union method
C2 = A | B                    # Usin '|' operator 

print(C1, C2)                 # {1, 2, 3, 4, 5} {1, 2, 3, 4, 5}  ,  same output 

C3 = A.intersection(B)        # Using intersection method
C4 = A & B                    # Usin '&' operator 

print(C3, C4)                 # {1, 3, 5} {1, 3, 5}  , same output 


A = {1, 2, 3}
B = {3, 4, 5}

C5 = A.difference(B)          # Using difference method 
C6 = A - B                    # Usin '-' operator 

print(C5, C6)                 # {1, 2} {1, 2}  , same output 
