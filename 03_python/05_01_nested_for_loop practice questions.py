# Nested for loop


# Level 1

# Example : Print a rectangle of stars

for i in range(3):          
    for j in range(5):      
        print("*", end="")
    print()



# Example : Print numbers in a grid 

for i in range(1,4):
    for j in range(1,4):
        print(i, end=" ")
    print()



# Example : Multiply two numbers (Multiplication Table)

for i in range(1,11):
    for j in range(1,11):
        print(i," x ",j,' = ', i*j, end='\n')
    print()



# Print these pattern

# ****
# ****
# ****

for i in range(1,4):
    for j in range(1,5):
        print("*", end="")
    print()



# ****
# ****
# ****
# ****

for i in range(1,5):
    for j in range(1,5):
        print("*", end=" ")
    print()



# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5

for i in range(1,4):
    for j in range(1,6):
        print(j, end=" ")
    print()



# AAA
# AAA
# AAA

for i in range(1,4):
    for j in range(1,4):
        print("A", end=" ")
    print()



# *
# **
# ***
# ****
# *****

for i in range(1,7):
    for j in range(1,i):
        print("*", end=" ")
    print()



# *****
# ****
# ***
# **
# *

for i in range(1,7):
    for j in range(1,7-i):
        print("*", end=" ")
    print()



# 1
# 12
# 123
# 1234
# 12345

for i in range(1,6):
    for j in range(1,i+1):
        print(j, end="")
    print()



# 1
# 22
# 333
# 4444
# 55555

for i in range(1,6):
    for j in range(1,i+1):
        print(i, end="")
    print() 



# 10101
# 01010
# 10101
# 01010

for i in range(1,6):
    for j in range(1,6):
        if (i+j)%2 == 0:
            print(1,end='')
        else:
            print(0,end='')
    print()

# Or

rows = 4
cols = 5

for i in range(rows):
    for j in range(cols):
        print((i + j) % 2, end="")
    print()



# Level 2 nested loops

# *****
# *   *
# *   *
# *   *
# *****

rows = 5
cols = 5

for i in range(rows):
    for j in range(cols):
        if i == 0 or i == rows-1 or j == 0 or j == cols - 1:
            print("*", end = "")
        else:
            print(" ", end="")
    print()


#     *
#    **
#   ***
#  ****
# *****

for i in range(1, 6):
    for j in range(1,6-i):
        print(" ", end="")
    for k in range(1,i+1):
        print("*", end="")
    print()


# 12345
# 1234
# 123
# 12
# 1

for i in range(1,6):
    for j in range(1,6-i+1):
        print(j, end="")
    print()


# *****
#  ****
#   ***
#    **
#     *

for i in range(1,6):
    for j in range(1,i+1):
        print(" ", end='')
    for k in range(1,6-i+1):
        print("*", end="")
    print()


#     *
#    ***
#   *****
#  *******
# *********

n = int(input())

for i in range(1, n + 1):
    for j in range(1, n-i+1):
        print(" ", end="")
    for k in range(2*i - 1):
        print("*", end="")

    print()



# 1
# 01
# 101
# 0101
# 10101

for i in range(1,6):
    for j in range(1, i+1):
        if (i+j)%2==0:
            print(1, end="")
        else:
            print(0, end="")
    print()


# Pascal's triangle

# 1
# 11
# 121
# 1331
# 14641

n = 5

for i in range(n):
    num = 1
    for j in range(i + 1):
        print(num, end="")
        num = num * (i - j) // (j + 1)    # Pascal's formula
    print()


# Floyd’s Triangle

# 1
# 2 3
# 4 5 6
# 7 8 9 10

n = 4
num = 1

for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()


# A
# AB
# ABC
# ABCD
# ABCDE

for i in range(1, 6):
    for j in range(i):
        print(chr(65 + j), end="")
    print()



# Hollow Triangle

# *
# **
# * *
# *  *
# *****

n = 5

for i in range(1, n+1):
    for j in range(1, i+1):
        if i == 1 or j == 1 or j == i or i == n:             # First row OR first column OR last column OR last row
            print("*", end="")
        else:
            print(" ", end="")
    print()



# Level 3


# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *

n = 5
for i in range(1, n+1):
    print("*"*i + " "*(2*(n-i)) + "*"*i)

for i in range(n-1, 0, -1):
    print("*"*i + " "*(2*(n-i)) + "*"*i)



#     A     
#    ABA    
#   ABCBA   
#  ABCDCBA  
# ABCDEDCBA 

n = 5
for i in range(1, n+1):
    print(" "*(n-i), end="")
    for j in range(1, i+1):
        print(chr(64+j), end="")
    for j in range(i-1, 0, -1):
        print(chr(64+j), end="")
    print()



#    *      
#   * *     
#  *   *    
# *     *   
#  *   *    
#   * *     
#    *
 
n = 4

for i in range(1, n+1):
    print(" "*(n-i), end="")
    if i == 1:
        print("*")
    else:
        print("*" + " "*(2*i-3) + "*")

for i in range(n-1, 0, -1):
    print(" "*(n-i), end="")
    if i == 1:
        print("*")
    else:
        print("*" + " "*(2*i-3) + "*")



# 1
# 232
# 34534
# 4567456


n = 4
start = 1

for i in range(1, n+1):
    x = i
    for j in range(i):
        print(x, end="")
        x += 1
    for j in range(i-2, -1, -1):
        print(x-2-j, end="")
    print()



# nested loops ( for + while )

# Print a rectangle using while → for

i = 1
while i <= 5:          
    for j in range(5): 
        print("*", end="")
    print()
    i += 1



# while loop inside for loop (for → while)

for i in range(1, 6):   
    j = 1
    while j <= i:      
        print("*", end="")
        j += 1
    print()



# 1111
# 2222
# 3333
# 4444

i = 1
while i <= 4:
    for j in range(4):
        print(i, end="")
    print()
    i += 1



# *****
# ****
# ***
# **
# *

i = 5
while i >= 1:
    for j in range(i):
        print("*", end="")
    print()
    i -= 1



# 1
# 12
# 123
# 1234

for i in range(1, 5):
    j = 1
    while j <= i:
        print(j, end="")
        j += 1
    print()



# 1
# 1 3
# 1 3 5
# 1 3 5 7

for i in range(1, 5):
    j = 1
    count = 1
    while count <= i:
        print(j, end=" ")
        j += 2
        count += 1
    print()


