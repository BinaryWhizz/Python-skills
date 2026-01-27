# PPA

# Accept a positive integer n as input and print the list of first n positive integers as output.

n = int(input())

l=[]

for i in range(n+1):
    l.append(i)
print(l) 


# Accept a sequence of words as input, append all these words to a list in the order in which 
# they are entered, and print this list as output. The first line in the input is a positive
# integer n that denotes the number of words in the sequence. The next n lines will have one
# word on each line. 

n = int(input())
l=[]
for i in range(n):
    x = input()
    l.append(x)
print(l) 


# Accept a sequence of comma-separated integers as input and print the maximum value in the
# sequence as output.
# Hint:
# When in doubt, always print the variables and examine the output.

num = '1,2,3,4,5'
L = num.split

num = input().split(',')
max = -1
for i in range(len(num)):
    if(int(num[i])>max):
        max = int(num[i])
print(max)


# This question introduces you to the idea of prefix codes. Prefix code is a block of visible code that is
# already provided to you. You have to type your code below the prefix code. Note that the contents of
# the prefix cannot be modified.
# A list L of words is already given to you as a part of the prefix code. Print the longest word in the list.
# If there are multiple words with the same maximum length, print the one which appears at the
# rightmost end of the list.
# You do not have to accept input from the console as it has already been provided to you

L = input().split(',')
max=0
m=''
for i in range(len(L)):
   if len(L[i])>=max:
    max=len(L[i])
    m=''
    m+=L[i]
print(m)

# or 

L = input().split(',')
max_word = L[0]

for word in L:
    if len(word) >= len(max_word):
        max_word = word

print(max_word)


# Accept a space-separated sequence of positive real numbers as input. Convert each
# element of the sequence into the greatest integer less than or equal to it. Print this sequence
# of integers as output, with a comma between consecutive integers.

x=input()
r=x.split(' ')
i = 0
s=''
while i<( len(r)-1) :
    n = int(float(r[i]))
    s += str(n)+','
    i += 1
n= int(float(r[i]))
s += str(n)
print(s)


# Accept a sequence of comma-separated words as input. Reverse the sequence and print it as output.
# Hint:
# 1 print([1] + [2])
# 2 print([2] + [1]) 

l=input().split(',')
for i in range(len(l)-1,0,-1):
    print(l[i],end=',')
print(l[0])


# This question introduces you to the idea of suffix codes. Suffix code is a block of visible code that
# will be executed after whatever code you type. You have to type your code above the suffix code.
# Note that the contents of the suffix code cannot be modified.
# Accept a square matrix as input and store it in a variable named matrix. The first line of input will
# be, n, the number of rows in the matrix. Each of the next n lines will have a sequence of n spaceseparated integers.
# You do not have to print the output to the console as the suffix code already does that for you.

n = int(input())
matrix = []

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row) 

