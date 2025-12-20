# Types of Function Arguments 

def add(a, b, c):
    return (a + b - c)

print(add(20, 30, 40))        # 10 



def add(c, a, b):
    return (a + b - c)

print(add(20, 30, 40))        # 50 , because here c = 20, a = 30, b = 40 


# Positional arguments :

print(add(10, 15, 30))        # 30 


print(add( a = 20, b = 30, c = 40 ))       # Sequence of arguments here has nothing to do with he sequence parameters of 
                                           # add function the dependency between these two sequences has been eliminated     
                                           # completely. We mention the parameter name along with the argument over here  
                                           # in function definition itself. This type function arguments are referred as
                                           # keyword arguments 

# print(add(20))                # Error , add() missing 2 required positional arguments: 'a' and 'b'

# There is a way to solve this error

def add(c, a = 20, b = 30):
    return (a + b - c)

print(add(40))                # 10, since a & b are absent, it takes the default parameter value from add function

print(add(40, 10))            # 0 , here c = 40, a = 20, since b is absent, it takes the default parameter value from add function
print(add(40, 10, 50))        # 20, here c, a, b became 40, 10, 50 respectively 

print(add(40, b = 10, a = 50))  # c = 40 is positional argument, b & c are keyword arguments, also default arguments  

# -----------------------------------------------------------

def add(c, a = 20, b = 30):
    print(a + b - c)

print(add(40))               

print(add(40, 10))            
print(add(40, 10, 50))        

print(add(40, b = 10, a = 50)) 

# Output of the above programme : 

# 10  
# None
# 0
# None
# 20
# None
# 20
# None 

# This function prints a value
# But it does not return anything
# In Python, every function returns something.
# If you don’t write return, Python automatically returns None. 

# Step-by-step execution (very important)

# When Python sees:

# print(add(40))

# It works like this:

# Step 1

# Call the function:

# add(40)

# Step 2

# Inside the function:

# print(a + b - c)   # prints 10

# Step 3

# Function ends → Python automatically does:

# return None

# Step 4

# Now Python executes the outer print:

# print(None)

# So output becomes:

# 10

# None
