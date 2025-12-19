# Functional programming part 2 

# Inline statements 

a = 10 
b = 20

if a < b:
    small = a 
else:
    small = b

print(small)         # 10

# This entire code from line 8 to 13 can be replaced by a single line of code 

a = 10 
b = 20

small = a if a < b else b 

print(small) 


# loops

# while :

a = 5 
while a > 0:
    print(a)
    a-=1

# or

a = 5 
while a > 0: print(a); a-=1


# for 

fruits = ['mango', 'apple', 'banana', 'orange', 'pineapple', 'watermelon', 'guava', 'kiwi']

newl = []

for i in fruits:
    if 'n' in i:
        newl.append(i.capitalize())
print(newl)                             # ['Mango', 'Banana', 'Orange', 'Pineapple', 'Watermelon'] 

# or 

fruits = ['mango', 'apple', 'banana', 'orange', 'pineapple', 'watermelon', 'guava', 'kiwi']

newl = [i.capitalize() for i in fruits if 'n' in i] 

print(newl)                             # ['Mango', 'Banana', 'Orange', 'Pineapple', 'Watermelon'] 



