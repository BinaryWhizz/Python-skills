# # 1) Write a program to check whether a person is eligible for voting or not. ( voting age >= 18)

x = int(input("Age of x : "))

if x >= 18 :
    print("Eligible for vote")
else: 
    print("Not eligible for vote")


# # 2) Write a program to find the lowest number out of two numbers expected from user.

a = int(input())
b = int(input())

if a > b :
    print("b is smaller")
else :
    print("a is smaller") 

# # 3) Write a program to check whether a number is even or odd.

x = int(input())

if x%2 == 0 :
    print("Even")
else:
    print("Odd")


# 4) Write a program to whether a number ( accepted from user ) is divisible by 2 and 3 both.

x = int(input())

if x%2 == 0 and x%3 == 0 :
    print("Divisible by 2 & 3 both")
else:
    print("Number isn't divisible by both")

# or

if x%2 == 0 :
    if x%3 == 0 :
        print("Divisible by 2 & 3 both")
else:
    print("Number isn't divisible by both")


# 5) Write a program to find the largest number out of three numbers expected from user.

# a) Correct way 

a = int(input())
b = int(input())
c = int(input())

if a >= b and a >= c:
    print("a is the largest")
elif b >= a and b >= c:
    print("b is the largest")
else:
    print("c is the largest")


# b) This is wrong: reason : Step-by-step execution for a=1, b=2, c=3:

# if a > b: → 1 > 2 ❌ → False, skip this block.

# elif b > a: → 2 > 1 ✅ → True, go inside it.
# → Inside this: if b > c: → 2 > 3 ❌ → False, so no print.

# Next elif c > a: → ⚠️ This will NOT be checked, because the previous elif was true (b > a was True).
# So Python skips this part entirely.

# ✅ Result: Nothing will be printed.

# 🧩 Why?

# Because once an elif condition (b > a) is True, Python won’t check the next elif, even if the inner condition (b > c) is False.
# That’s why your code does not print anything when a=1, b=2, c=3.

# a = int(input())
# b = int(input())
# c = int(input())

# if a>b :
#     if a>c :
#         print("a is greater")
# elif b>a :
#     if b>c :
#         print("b is grater")
# elif c>a:
#     if c>b:
#         print("c is greater")


# This is correct only when a!=b!=c not when a=b, b=c or c=a

a = int(input())
b = int(input())
c = int(input())

if a > b:
    if a > c:
        print("a is greater")
if b > a:
    if b > c:
        print("b is greater")
if c > a:
    if c > b:
        print("c is greater")


# 6) Write a program to check a character is vowel or not.

chr = input("Enter a character")

vowel = 'aeiouAEIOU'

if chr in vowel :
    print("chr is vowel")
else : 
    print('chr is not vowel')


# 7) Accept three positive integers as input and check if they form the
# sides of a right triangle. Print YES if they form one, and NO is they do
# not. The input will have three lines, with one integer on each line.
# The output should be a single line containing one of these two
# strings: YES or NO.

a = int(input())
b = int(input())
c = int(input())

if (a**2 + b**2 == c**2 ) or (c**2 + a**2 == b**2 ) or (c**2 + b**2 == a**2 ):
    print("YES")
else:
    print("NO")


# 8) EvenOdd is a tech startup. Each employee at the startup is given an employee id which is a unique
# positive integer. On one warm Sunday evening, five employees of the company come together for a meeting and sit at a circular table:
# The employees follow a strange convention. They will continue the meeting only if the following
# condition is satisfied.
# The sum of the employee-ids of every pair of adjacent employees at the table must be an even
# number.
# They are so lazy that they won’t move around to satisfy the above condition, If the current seating
# plan doesn’t satisfy the condition, the meeting will be cancelled. You are given the employee-id of all
# five employees. Your task is to decide if the meeting happened or not.
# The input will be five lined, each containing an integer. The ith line will have the employee-id of Ei.
# The output will be a single line containing one of these two strings: YES or NO.

E1 = int(input())
E2 = int(input())
E3 = int(input())
E4 = int(input())
E5 = int(input())

if (E1+E2)%2 == 0 and (E2+E3)%2 == 0 and (E3+E4)%2 == 0 and (E4+E5)%2 == 0 : 
    print("YES")
else:
    ("NO")


# 9) Accept a string as input and print the vowels present in the string in
# alphabetical order. If the string doesn’t contain any vowels, then
# print the string none as output. Each vowel that appears in the input
# string – irrespective of its case should appear just once in lower case
# in the output.

x = input()
z = x.lower()
y = ""

if 'a' in z:
    y+='a'
if 'e' in z:
    y+='e'
if 'i' in z:
    y+='i'
if 'o' in z:
    y+='o'
if 'u' in z:
    y+='u'
if y in z == False:
    print("none")
else:
    print(y)



# 10) Accept a string as input. Your task is to determine if the input string is a valid password or not. For a
# string to be a valid password, it must satisfy all the conditions given below:
# (1) It should have at least 8 and at most 32 characters
# (2) It should start with an uppercase or lowercase letter
# (3) It should not have any of these characters: / \ = ' "
# (4) It should not have spaces
# It could have any character that is not mentioned in the list of characters to be avoided (points 3 and
# 4). Output True if the string forms a valid password and False otherwise.

n = input()

if 8<= len(n) <= 32 and n[0].isalpha() and '/' not in n and '=' not in n and '\'' not in n and "'" not in n and '"' not in n and ' ' not in n :
    print("True")
else: 
    print("False")


# 11) Accept a point in 2D space as input and find the region in space that this point belongs to. A
# point could belong to one of the four quadrants, or it could be on one of the two axes, or it
# could be the origin. The input is given in 2 lines: the first line is the x-coordinate of the point
# while the second line is its y-coordinate. The possible outputs
# are first, second, third, fourth, x-axis, y-axis, and origin. Any other output will not be
# accepted. Note that all outputs should be in lower case

x = float(input())
y = float(input())
if x>0:
  if y>0:
    print("first")
  elif y<0:
    print("fourth")
  elif(y==0):
    print("x-axis")
if x<0:
  if y>0:
    print("second")
  elif(y<0):
    print("third")
  elif(y==0):
    print("x-axis")
if x==0:
  if y==0:
    print("origin")
  else:
    print("y-axis")


# 12) Accept a string as input. If the input string is of odd length, then continue with it. If the input string is of even length, make the
# string of odd length as below:
# • If the last character is a period (.), then remove it
# • If the last character is not a period, then add a period (.) to the end of the string. Call this string of odd length 'word'. 
# Select a substring made up of three consecutive characters from 'word' such that there are an
# equal number of characters to the left and right of this substring. Print this substring as output. You can assume that all input
# strings will be in lower case and will have a length of at least four. 

s = input()
n = len(s)
if n%2 == 0:
    if s[n-1]=='.':
        s=s[:-1]
    else:
        s=s+'.'
n = int((len(s)-1)/2)
print(s[n-1: n+2])


# 13) You are given the date of birth of two persons, not necessarily from the same family. Your task is to find the younger of the two. If both
# of them share the same date of birth, then the younger of the two is assumed to be that person whose name comes first in alphabetical order.
# The input will have four lines. The first two lines correspond to the first person, while the last two lines correspond to the second person. 
# For each person, the first line corresponds to the name and the second line corresponds to the date of birth in “DD-MM-YYYY” format. 
# Your output should be the name of the younger of the two.

a = input()  
x = input()   # DOB
b = input()  
y = input()   # DOB

if x==y :
    if a<b :
        print("a is younger")
    else:
        print("b is younger")
elif x[-4:] != y[-4:]:
    if int(x[-4:]) < int(y[-4:]):
        print("b is younger")
    else:
        print("a is younger")
elif x[3:5] != y[3:5]:
    if int(x[3:5]) < int(y[3:5]):
        print("b is younger")
    else:
        print("a is younger")
else:
    if int(x[0:2]) < int(y[0:2]):
        print("b is younger")
    else:
        print("a is younger")


