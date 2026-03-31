# More on dictionaries

d = {'key': 'value'}

# Iterate over a dictionary 

d = {0:0, 1:1, 2:4, 3:9, 4:16}
print(d)                          # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

for i in d:
    print(i, d[i])          

# print(i) will print only the keys            # print(i, d[i]) will print 
    # 0                                                            # 0 0
    # 1                                                            # 1 1
    # 2                                                            # 2 4
    # 3                                                            # 3 9
    # 4                                                            # 4 16 
    

# Dictionary specific methods :

d = {0:0, 1:1, 2:4, 3:9, 4:16}





# Write a Python program to combine two dictionary by adding
# values for common keys.

d1 = {10:100, 20:200, 40:300}
d2 = {40:400, 50:500, 60:600}

for i in d2:
    if i in d1.keys():
        d1[i] += d2[i]
    else:
        d1[i] = d2[i]

print(d1)

print(d.keys())                  # dict_keys([0, 1, 2, 3, 4])         , in a list
print(d.values())                # dict_values([0, 1, 4, 9, 16])      , in a list 
print(d.items())                 # dict_items([(0, 0), (1, 1), (2, 4), (3, 9), (4, 16)]), This is another place where python internally use tuples

