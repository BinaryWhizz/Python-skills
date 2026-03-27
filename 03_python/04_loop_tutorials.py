# 1) Find the factorial of the given number 

n = int(input("Enter a number : "))

i = 1
m = 1

if n < 0 :
    print("Not defined")
else :
    for i in range(n, 1, -1):
        m = m*i
    print(m)


# 2) Find the number of digits in a given number 

n = abs(int(input("Enter a number : ")))

strn = str(n)
count = 0
for i in strn :
    count += 1
print(count)


# 3) Reverse the digits in the given number

n = int(input("Enter a number : "))
absStrn = str(abs(n))
rev = ''
for i in absStrn:
    rev = i + rev
if n >= 0 :
    print(rev)
else : 
    print('-' + rev)


# 4) Write a program to check if a number is palindrome or not.

n = int(input("Enter a number : "))
absStrn = str(abs(n))
rev = ''

for i in absStrn : 
    rev = i + rev
if n < 0 :
    rev = '-' + rev 
if n == int(rev) :
    print("Palindrome")
else:
    print("Not a Palindrome")


# 5) Find whether the number is a prime or not ?

num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")


# 6) Find the sum of all the digits in a given number 

num = int(input("Enter a number: "))
sum_of_digits = 0

for digit in str(num):
    sum_of_digits += int(digit)

print("Sum of digits =", sum_of_digits)


# 7) Find all factors of a given number 

num = int(input("Enter a number: "))

print("Factors of", num, "are:")

for i in range(1, num + 1):
    if num % i == 0:
        print(i)

# 8) Accept integers using input() function to find max until the input is -1

max_num = None                # To store the maximum number

for i in range(1000):         # arbitrary large range
    num = int(input("Enter a number (-1 to stop): "))
    
    if num == -1:
        break
    
    if (max_num is None) or (num > max_num):
        max_num = num

if max_num is not None:
    print("Maximum number entered is:", max_num)
else:
    print("No valid number entered.")


# Print the sum of all even & odd numbers in a range separately 

n = int(input())

even = 0
odd = 0

for i in range(1,n+1):

    if i%2==0:
        even = even+i
    if i%2!=0:
        odd = odd+i

print(even)
print(odd)


# Accept a number and check if it a perfect number or not. A number whose sum of factors is equal to the number itself

n = int(input())

sum = 0

flag = False

for i in range(1,n+1):
    if n%i==0:
        sum += i
        if sum == n:
            flag = True
        
if flag:
    print("Found")
else:
    print('Not this number')
    
