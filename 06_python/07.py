# Exception handling 

a = int(input())
b = int(input())

c = a/b

print(c)                 # No error, if b != 0 

# if a = 20, b = 0 ---> ZeroDivisionError: division by

# An exception is an error that occurs while the program is running, in the above code the syntax c = a/b is correct
# but the problem is in the input.


a = int(input())
b = int(input())

c = a/b

print(d)                 # Error, There is nothing wrong in this code but d is not defined 



f = open('abc.txt', 'r')   # FileNotFoundError: [Errno 2] No such file or directory: 'abc.txt', problem is not in the python
                           # code, the problem is the file is not available in the directory 

f = open('06.py', 'r')     # No error here 


# 20/0 , It will throw an error because computer doesn't divide anything by 0, which isn't possoble, we can not force. 
# But the error shown in the terminal can be fixed, The motive is our programme should not throw an error like this 



# ZeroDivisionError 

a = int(input())
b = int(input())

try:
    c = a/b
    print(c) 

except ZeroDivisionError:
    # pass
    print("Invalid input, divisor can not be zero") 

# The purpose behind this whole concept of exception handling is to indicate user, is to help user to avoid such mistakes. 
# That's why instead of using 'pass', better to use print statement like this -> print("Invalid input, divisor can not be zero") 



# Let's discuss --- > 

# NameError: 

a = int(input())
b = int(input())

try:
    c = a/b
    print(d) 

except NameError:
    print("Variable not defined") 



# FileNotFoundError

a = int(input())
b = int(input())

f = open('abc.txt', 'r') 

try:
    c = a/b
    print(c) 

except FileNotFoundError:
    print("Invalid file, Please check again") 



# Common exception handling block : It's not possible to remember every Error name 

except:
    print("Something went wrong")



# finally block : A special block which executes irrespective of whether we get exception or we donot get exception 

finally:
    f.close()
    print("From finally block") 



# Exception created by my own and with some condition which i want, unknown to python 

a = int(input())

if a < 18:
    # print("You are under age, can not vote") 
    raise Exception("You are under age, can not vote")     # Error, because we wanted Exception 


