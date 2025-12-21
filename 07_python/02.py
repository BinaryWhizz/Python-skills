# Recursion: Find 0 in a list

# This is piece of code to check if a given list has 0 in it or not. If it has "zero" in it, we return True(1), otherwise
# we retuen False(0)

def check0(L):
    if (len(L)==0):
        return 0           # If the list is empty return False 
    if L[0]==0:
        return 1           # If the first element is zero return True 
    else:
        return check0(L[1:len(L)])
    
ans = check0([1,2,0,4,5,10,8,7,3])

print(ans)                 # 1 

