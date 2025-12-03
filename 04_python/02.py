# import random 

# l = []

# l.append(random.random())
# print(l)
# l.append(random.random())
# print(l)
# l.append(random.random())
# print(l)
# l.append(random.random())
# print(l)
# l.append(random.random())
# print(l)

# for i in range(10):
#     l.append(random.random())
# print(l)

# for i in range(100):
#     l.append(random.randint(1,10))
# print(l)



# Birthday paradox

import random 

l = []
 
for i in range(30):                    # 30 days in a month
    l.append(random.randint(1,365))    # 365 in a year 
print(l)                               

# [47, 322, 192, 113, 253, 257, 260, 168, 58, 55, 350, 154, 307, 238, 365, 178, 358, 96, 282, 183, 150, 246, 164, 73, 333, 19, 360, 74, 245, 134]
# o check repetition in the terminal ----> sort() , arrange in ascending order 

l.sort() 
print(l)

# checking if there is any repetition
i = 0
flag = 0          # denotes that there is no repetition 

while i<len(l)-1 :
    if l[i] == l[i+1]:
        print("Repeats")
        flag = 1
        break
    i += 1
    # else: 
    #     print("None")
if flag == 0 :
    print("There is no repetition")



# Find the duplicates in the list 

# l = [2, 3, 4, 2, 3, 5]

# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]==l[j]:
#             print(l[i])

# or

l = [2, 3, 2, 2, 3, 5]
duplicates = []

for i in range(len(l)):
    for j in range(i+1, len(l)):
        if l[i] == l[j] and l[i] not in duplicates:
            duplicates.append(l[i])

print(duplicates)
