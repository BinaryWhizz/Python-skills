# More on tuples

# Lists are mutable and tuples are immutable , we cannot modify the values inside tuple once the tuple is created, Tuple may not allow us to modify its values
# but still we can perform various operations on tuples, we can access elements in the tuple using their index, Tuples also provides methods like list except methods 
# like append, remove, insert, pop for obvious reason which is correct, tuple is immutable.

# The most common application of tuple is packing and unpacking 


t = 1,2,3
print(t, type(t))         # (1, 2, 3) <class 'tuple'>

x,y,z = t 
print(x,y,z)              # 1 2 3 


x = 5 
y = 10
x,y = y,x                 # python is packing these two variables , y and x into a tuple and then unpacking it on the left-hand side 
print(x,y)                # 10 5


l = [10]
print(l, type(l))         # [10] <class 'list'> 

t = (10)
print(t, type(t))         # 10 <class 'int'> , Here python considers it as a single element, for tuple it should be more than one 


t = ([1,2], ['a','b'])
print(t)                  # ([1, 2], ['a', 'b'])  ---> list as a value inside it  


# t = ([1,2], ['a','b'])
# t[0] = [10,20]
# print(t)                  # TypeError: 'tuple' object does not support item assignment 


t = ([1,2], ['a','b'])
t[0][0] = 10 
print(t)                  # ([10, 2], ['a', 'b']) ---> If value inside a tuple is a list then we can modify the values inside that list  
                          # In python, this particular principle is referred as hashable 



t1 = (1,2,3)              # hashable
t2 = ([1,2,3])            # Non-hashable 

# If the values inside tuple are also immutable then the tuple is considered as hashable, 
# whereas, if values inside tuple are mutable then tuple is referred as non-hashable. 