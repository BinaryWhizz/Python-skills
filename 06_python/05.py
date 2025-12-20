# Scope of Variables 

def myFunction1(x):
    x = x * 2
    print("Value of x in function 1", x)

x = 5 

print("Value of x before function call", x)          # Value of x before function call 5
myFunction1(x)                                       # Value of x in function 1 10
print("Value of x after function call", x)           # Value of x after function call 5 

# myFunction1(x), Here we are calling this function ( myFunction1(x) ) along with an argument, we are not actually 
# passing this variable x to this function. But taking the value of that variable ( x = 5 ) to this function. 



# locals variable

# def myFunction1(x):                              # x here is local variable, can be used in this function definition only
#     x = x * 2
#     print("Value of x in function 1", x)


# Global variable

# x = 5                                            # x here is global variable, can be used in the entire code 
# print("Value of x before function call", x)         
# myFunction1(x)                                       
# print("Value of x after function call", x) 


# Is global a function? Ans : No, global is NOT a function, global is a keyword in Python. 

# A keyword:
# Has a special meaning in the language
# Is used to give instructions to Python
# Is not callable (you don’t use parentheses)


def myFunction1():
    global x
    x = x * 2                                         # 5 * 2
    print("Value of x in function 1", x)              # 10

def myFunction2():
    global x
    x = x * 3                                         # 10 * 3
    print("Value of x in function 2", x)              # 30 

x = 5 

print("Value of x before function call", x)           # 5  
myFunction1()
myFunction2()                                                                    
print("Value of x after function call", x)            # 30

# Whenever we say global x, computer realizes there is one variable name x somewhere in the global code which we have
# written, then it looks for that particular variable and finds its value which is 5, And in that particular function,
# it always refers to this particular variable x, because of that x*2 = 5*2 = 10 

# In 2nd function, x = 10, it uses existing global copy, x*3 = 10*3 = 30 


# Output

# Value of x before function call 5
# Value of x in function 1 10
# Value of x in function 2 30
# Value of x after function call 30 

