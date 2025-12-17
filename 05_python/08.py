# More on Lists 

l1 = [1,2,3]
l2 = [4,5,6]

l12 = l1 + l2
l21 = l2 + l1

print(l12, l21)         # [1, 2, 3, 4, 5, 6] [4, 5, 6, 1, 2, 3] 


# l3 = [0,0,0,0,0,0,0,0,0,0] 

l3 = [0] * 10 
print(l3)

print(l1 * 5)           # [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3] 


l1 = [1,2,3]
l2 = [1,2,3]
l3 = [1,3,2] 

print(l1 == l2)         # True  
print(l2 == l3)         # False   
print(l2 > l3)          # False  

print([1,2] < [2,1])    # True 
print([1] < [1,2,3])    # True 
print([2,3] < [3])      # True 
print([] < [1])         # True 


l = [1,2,4]
print(l)                # [1, 2, 4]
l[2] = 3
print(l)                # [1, 2, 3] 



# It cannot change value of a specific character 

# s = 'abcde'
# print(s[3]) 
# s[3] = 'd'
# print(s)            # Error 


x = 5
y = x
x = 10
print(x,y)


l1 = [1,2,3]
l2 = l1
l1[0] = 100 
print(l1, l2)         # [100, 2, 3] [100, 2, 3] , reason : Internal impementaion of integers and lists in python language 



l4 = [1,2,3]
l5 = list(l4)
l6 = l4[:]
l7 = l4.copy()        # Different object → same values 

l5[0] = 100
l6[1] = 200
l7[2] = 300 

print(l4, l5, l6, l7) 


l8 = l4

# is checks whether two variables refer to the same object in memory,
# NOT whether the lists have the same values

print(l4 is l5)        # False  , because of different memory location , l7 = l4.copy(), Different object → same values  
print(l4 is l6)        # False  ,            ""
print(l4 is l7)        # False  ,            ""
print(l4 is l8)        # Ture   , This does NOT create a new list. It simply points l8 to the same list object as l4 



# def add(x):
#     x = x+1
#     return x

# x = 5
# print(add(x))        # 6
# print(x)             # 5 


def add(x):
    x.append(1)
    return x

x = [5]
print(add(x))          # [5,1]
print(x)               # [5,1] 



l = [1,2,3] 
print(l)               # [1, 2, 3]

l.append(4)
print(l)               # [1, 2, 3, 4]

l.remove(2)
print(l)               # [1, 3, 4] 

# new
l.insert(2,9)          # ----> (2,9) means 9 will be placed at 2nd index
print(l)               # [1, 3, 9, 4] 

l.pop(0)               # (0) ---> index 0, here index 0 == 1 will me removed 
print(l)               # [3, 9, 4] 


l = [2,6,1,50,3,7,5]
l.sort() 
print(l)               # [1, 2, 3, 5, 6, 7, 50]

l.reverse()
print(l)               # [50, 7, 6, 5, 3, 2, 1] 

