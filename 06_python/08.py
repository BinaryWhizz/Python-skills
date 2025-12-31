# Tutorial on functions 


# Write a python code using functions which calculates the number of upper case letters, lower case letters. total number of characters
# and number of words 

def upper(s):
    upper = 0
    for c in s:
        if (c.isupper()):
            upper += 1
    return upper


def lower(s):
    lower = 0
    for c in s:
        if (c.islower()):
            lower += 1
    return lower


def characters(s):
    chars = 0
    for c in s:
        chars += 1
    return chars


def words(s):
    words = 1
    for c in s:
        if (c == ' '):
            words += 1
    return words


sentence = input('Enter the sentence: ')

uLetters = upper(sentence)
print(f'\nTotal number of upper case characters: {uLetters}')

lLetters = lower(sentence)
print(f'\nTotal number of lower case characters: {lLetters}')

chars = characters(sentence)
print(f'\nTotal number of characters: {chars}')

words = words(sentence)
print(f'\nTotal number of words: {words}')




# Write a Python code using functions to calculate area and perimeter of circle and rectangle
# Test Cases

import math

# PI = 22 / 7
PI = math.pi

def circle_area(r):
    return (PI * r * r)

def circle_perimeter(r):
    return (2 * PI * r)

def rectangle_area(l, b):
    return (l * b)

def rectangle_perimeter(l, b):
    return (2 * (l + b))

polygon = ''
while polygon != 'exit':
    print('\nPOLYGONS\ncircle\nrectangle\nexit')
    polygon = input('\nChoose the polygon type or exit: ')
    property = ''
    
    if polygon == 'circle':
        r = float(input('\nEnter the radius of the circle: '))
        while property != '':
            print('\nCIRCLE PROPERTIES\narea\nperimeter\nback')
            property = input('\nChoose the circle property or go back: ')
            
            if property == 'area':
                cArea = circle_area(r)
                print(f'Area of circle with radius {r} = {cArea} sq. units')
                property = ''
            
            elif property == 'perimeter':
                cPerimeter = circle_perimeter(r)
                print(f'Perimeter of circle with radius {r} = {cPerimeter} units')
                property = ''
            
            elif property == 'back':
                break
            
            else:
                print('Please select the correct polygon property')
                property = ''
    
    elif polygon == 'rectangle':
        l = float(input('\nEnter the length of the rectangle: '))
        b = float(input('\nEnter the breadth of the rectangle: '))
        while property != '':
            print('\nRECTANGLE PROPERTIES\narea\nperimeter\nback')
            property = input('\nChoose the rectangle property or go back: ')
            
            if property == 'area':
                rArea = rectangle_area(l, b)
                print(f'Area of rectangle = {rArea} sq. units')
                property = ''
            
            elif property == 'perimeter':
                rPerimeter = rectangle_perimeter(l, b)
                print(f'Perimeter of rectangle = {rPerimeter} units')
                property = ''
            
            elif property == 'back':
                break
            
            else:
                print('Please select the correct polygon property')
                property = ''
    
    elif polygon == 'exit':
        break
    
    else:
        print('Please select the correct polygon type or exit')



# Write a Python code using functions which checks whether the input coordinates form a triangle or not 
# 1)	(0, 0), (0, 1), (1, 0)	Triangle
# 2)	(-3, -5), (-7, 10), (0, 0)	Triangle
# 3)	(1, 2), (1, 10), (5, 2)	Triangle
# 4)	(1, 1), (2, 2), (3, 3)	Not a triangle
# 5)	(2, 3), (3, 2), (2, 3)	Not a triangle
# 6)	(0, 0), (10, 0), (0, 0.0001)	Triangle 


def distance(xi, yi, xj, yj):
    return (((xj - xi) ** 2) + ((yj - yi) ** 2)) ** 0.5

def isTriangle(max, a, b):
    if (a + b) > max:
        print('\nTriangle')
    else:
        print('\nNot a triangle')

x1 = float(input('Enter x coordinate of 1st point: '))
y1 = float(input('Enter y coordinate of 1st point: '))
x2 = float(input('\nEnter x coordinate of 2nd point: '))
y2 = float(input('Enter y coordinate of 2nd point: '))
x3 = float(input('\nEnter x coordinate of 3rd point: '))
y3 = float(input('Enter y coordinate of 3rd point: '))

d1 = distance(x1, y1, x2, y2)
print(f'\nDistance between points ({x1}, {y1}) and ({x2}, {y2}) = {d1}')

d2 = distance(x2, y2, x3, y3)
print(f'\nDistance between points ({x2}, {y2}) and ({x3}, {y3}) = {d2}')

d3 = distance(x3, y3, x1, y1)
print(f'\nDistance between points ({x3}, {y3}) and ({x1}, {y1}) = {d3}')

if d1 > d2:
    if d1 > d3:
        isTriangle(d1, d2, d3)
    else:
        isTriangle(d3, d1, d2)

elif d2 > d3:
    isTriangle(d2, d1, d3)

else:
    isTriangle(d3, d1, d2) 


# Or 


'''Approach 2: Using slope of lines connecting two points'''

import math

def slope(xi, yi, xj, yj):
    if (xi == xj):
        return (math.inf)
    else:
        return ((yj - yi) / (xj - xi))

x1 = float(input('Enter x coordinate of 1st point: '))
y1 = float(input('Enter y coordinate of 1st point: '))
x2 = float(input('\nEnter x coordinate of 2nd point: '))
y2 = float(input('Enter y coordinate of 2nd point: '))
x3 = float(input('\nEnter x coordinate of 3rd point: '))
y3 = float(input('Enter y coordinate of 3rd point: '))

s1 = slope(x1, y1, x2, y2)
print(f'\nSlope of the line connecting points ({x1}, {y1}) and ({x2}, {y2}) = {s1}')

s2 = slope(x2, y2, x3, y3)
print(f'\nSlope of the line connecting points ({x2}, {y2}) and ({x3}, {y3}) = {s2}')

if (s1 != s2):
    print('\nTriangle')
else:
    print('\nNot a triangle')
