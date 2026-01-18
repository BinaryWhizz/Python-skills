# While loop


# Write a program to print numbers from 1 to 10 using a while loop.

i = 0
while i <= 10:
    print(i)
    i += 1


# Find the sum of numbers from 1 to N.

n = int(input("Enter N: "))
total = 0
i = 1

while i <= n:
    total += i
    i += 1

print("Sum =", total)


# Ask the user to enter 1947 until they get it right.

year = int(input("Enter a year: "))

while year != 1947:
    print("Wrong")
    year = int(input("Try again: "))

# print("Right!")


# Find factorial of a number

n = int(input("Enter a number : "))

i = 1
m = 1

while(i<=n):
    m = m*i    
    i += 1
print(m)

# # or

m = 1 

while( n>0):
    m *= i
    n -= i
print(m)


# Find the number of digits in a number

n = int(input())

count = 0

while(n>0) :
    n = n // 10
    count = count + 1
print(count)


# Take a number and print its reverse.

n = int(input("Enter a number: "))
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n //= 10

print("Reversed =", rev)


# Print the multiplication table of a given number.

n = int(input("Enter a number: "))
i = 1

while i <= 10:
    print(n, "x", i, "=", n * i)
    i += 1


# A number is palindrome if it reads the same backward (e.g. 121, 1331).
# Write a program to check if a number is palindrome.

n = int(input("Enter a number: "))
temp = n
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n //= 10

if temp == rev:
    print("Palindrome")
else:
    print("Not palindrome")


# Count how many even and odd digits a number has.

n = int(input("Enter a number: "))
even = 0
odd = 0

while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        even += 1
    else:
        odd += 1
    n //= 10

print("Even digits:", even)
print("Odd digits:", odd)


# Print each digit of a number on a new line (from last digit to first).

n = int(input("Enter a number: "))

while n > 0:
    digit = n % 10
    print(digit)
    n //= 10


# Keep asking the user to enter a number until they enter 0.

n = int(input())
while n>0:
    n = int(input())
    if n==0:
        print("Stop")  


# Ask the user to enter a password until the correct password is entered.

password = input()
while len(password)>0:
    password2nd = input()
    if password2nd==password:
        print("Matched")
