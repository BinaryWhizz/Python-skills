s = "VIBGYOR"
t = "MONUGYA"

c = 0
for i in range(7):
    for j in range(7):
        c = c + 1 
        print(s[i],s[j])
        
print(c)


# Find all the prime numbers less than the entered number 

n = int(input("Enter a number : "))

if n >=2 :
    print(2, end=' ')
for i in range(3, n):
    flag = False
    for j in range(2, i):
        if i % j == 0 : 
            flag = False
            break
        else:
            flag = True
    if flag : 
        print(i, end = ' ') 


# Find the total profit/loss of each trader working in a trading firm. Information regarding number of traders and number of transactions in unknows.

empID = input("Enter employee ID : ")
while empID != '-1' :
    trade = int(input("Enter the trade amount: "))
    profit_loss = 0
    while trade != 0 :
        profit = profit_loss + trade 
        trade = int(input("Enter the trade amount : "))
    print((f'Profit/loss for employee (empID) is (profit_loss)'))
    empID = input('\nEnter employee ID : ')


# Find the day wise total rainfall for the entered duration of time e.g. week, month, ect.

days = int(input("Enter the number of days : "))
for i in range(1, days+1):
    total = 0
    rainfall = int(input("Enter the rainfall : "))
    while rainfall != -1 :
        total = total + rainfall
        rainfall = int(input("Enter the rainfall"))
    print("Total rainfall for day {0} is {1}".format(i, total))


# Find the length of longest word from set of words entered by the user 

word = input("Enter a word : ")

maxLen = 0 
while(word != '-1'):
    count = 0
    for letter in word:
        count += 1
        if count > maxLen :
            maxLen = count
        word = input("Enter a word : ")
print("The length of longest word is %s" %maxLen)


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
