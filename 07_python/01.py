# Introduction to Recursion 

# Recursion is a programming technique where a function calls itself to solve a problem by breaking it into smaller
# versions of the same problem.

# Why recursion is used ?

# Problems that repeat in a self-similar way
# Cleaner code for mathematical and hierarchical problems


# n = 10
# ans = 0

# for i in range(n):
#     print(i+1)
#     ans += (i+1)

# print(ans)

# Let's use function 

def sum(n):
    ans = 0
    for i in range(n):
        ans += (i+1)
    return ans 


# Different way or better way to write the above function : Recursion 

def sum(n):
    if n == 1:
        return 1 
    else:
        return n + sum(n-1)

print(sum(10)) 

# Python lets you call the same function within the function 


# Compute compound interest by assuming the interest to be 10%

def comp(p, n):
    if n==1:
        return p*(1.1)
    else:
        return comp(p,n-1)*1.1

print(comp(2000, 3))



# Factorial using recursion 

def fact(n):
    if n==1:
        return 1
    else:
        return fact(n-1)*n 
    
print(fact(5))

