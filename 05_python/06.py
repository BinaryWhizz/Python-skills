# Dictionary

d = {}

d['A'] = 9854426803
d['B'] = 9577192318
d['C'] = 8472929467

print(d)

print(d['A'])
print(d['B'])
print(d['C'])


for i in d:
    d[i] = 0
print(d)               # {'A': 0, 'B': 0, 'C': 0} 




JsUser = {
    'name' : "Monugya",
    "full name" : "Monugya_Borchetia",
    "Hobby" : "coding_&_gaming",
    'age' : 28,
    'location' : "Assam",
    'email' : "monugya@gmail.com",
    'isLoggedIn' : False,
    # 'lastLoginDays' : ["Monday", "Saturday"]
}

# for i in JsUser:
    # print(i)
    # print(i,':', JsUser[i])

for i,j in JsUser.items():     # only in case of dictionary only
    print(i,':',j)


if "email" in JsUser:
    print("Present")
else:
    print("Absent")
    

print(len(JsUser))


JsUser["Gf"] = "No"    # adding 
print(JsUser)


JsUser.pop("Gf")       # Removes the key and returns its value. If the key does not exist, Python also raises KeyError (unless a default is provided).
print(JsUser)          # removing 


JsUser.popitem()       # removes the last item automatically 
print(JsUser)


del JsUser["age"]      # Removes the key without returning anything.If the key does not exist, Python raises KeyError.
print(JsUser)



# Dictionary and list inside dictionary

fbUser = {
    'email': "mbc@google.com",
    'fullName' : {
        'userFullName': {
            'firstlName' : "Monugya",
            'lastName' : "Borchetia"
        } 
    },
    'otherinfo': {
        'age' : 28,
        'location' : "Assam"
        },
    'lastLoginDays' : ["Monday", "Saturday"]
    
}



squared_num = { x:x**2 for x in range(6)}
print(squared_num)

squared_num.clear()              # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(squared_num)               # {}



keys = ['a','b','c','d']

default_value = 'Delicious'

new_dict = dict.fromkeys(keys, default_value)

print(new_dict)                  # {'a': 'Delicious', 'b': 'Delicious', 'c': 'Delicious', 'd': 'Delicious'}  


new_dict01 = dict.fromkeys(keys, keys)

print(new_dict01)       # {'a': ['a', 'b', 'c', 'd'], 'b': ['a', 'b', 'c', 'd'], 'c': ['a', 'b', 'c', 'd'], 'd': ['a', 'b', 'c', 'd']}