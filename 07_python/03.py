# Sorting Recursively

def mini(L):                          # finds the minimum element in the list L
    mini = L[0]
    for x in L:
        if x<mini:
            mini = x 
    return mini 

# def sort(L):                          # recursively sort the list L 
#     m = mini(L)                       # m now contains the minimum most element in L 
#     L.remove(m)                       # We remove that element from L 
#     return [m]+sort(L)                # We recursively sort the smaller list


# What if the list is empty 

def sort(L):                          # recursively sort the list L 

    if L==[]:                         # if the list is empty, there is nothing to sort 
        return L 
    
    m = mini(L)                       # m now contains the minimum most element in L 
    L.remove(m)                       # We remove that element from L 
    return [m]+sort(L)                # We recursively sort the smaller list 

L = [5,6,59,19,2,1,3] 
print(sort(L))                        # [1, 2, 3, 5, 6, 19, 59] 

