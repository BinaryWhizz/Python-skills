# Introduction to Binary Search

# Key requirement
# The list must be sorted (ascending or descending).

# How binary search works (idea)
# Find the middle element.
# Compare it with the target:
# If equal → found.
# If target is smaller → search the left half.
# If target is larger → search the right half.
# Repeat until found or the range becomes empty.


# Check if a given element k is present in a list L or not 

def obvious_search(L,k):
    for i in L:
        if i == k:
            return 1
    return 0 

L = list(range(100))
print(L)
print(obvious_search(L,2)) 