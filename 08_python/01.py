# class : A class is a blue print for creating objects in Python. It defines properties (attributes) and actions (methods)
# that objects created from the class can have.

# Example : 

class Car:
    # Class attributes
    brand = 'Toyota'
    wheels = 4

    # Mothod 
    def start_engine(self):
        return "The engine has satrted."

# Key points :
# - Car is the name of the class
# - Attributes : Brand and wheels describe the properties of a car 
# - Method : start_engine() is an action the car can perform 


# Object : An object is an instance of a class. It inherits all the attributes and methods of the class from which is created

# Create an object of the Car class
my_car = Car()

# Access object properties
print(my_car.brand)            # Toyota 

# Call object method 
print(my_car.start_engine())   # The engine has started 


# Developing Class and Object

# step-1 : 

# class ClassName:
    # # Class attributes
    # attribute1 = value1
    # attribute2 = value2


# step-2 :

# Consttructor (Optional)

# def __init__(self, parameter1, parameter2):        # __init__ : This method is called automatically whenever a new object of the class is created 
    # self.parameter1 = parameter1
    # self.parameter2 = parameter2 


# step-3 :

# Method

# def method_name(self):
#     return "Action performed"


# step-4 :

# Create an object 

# object_name = ClassName(argument1, argument2)


class Calculator:
    # Contructor
    def __init__(self, num1, num2):
        self.num1 = num1              # Object specific attribute 
        self.num2 = num2 

    # Method to add numbers 
    def add(self):
        return self.num1 + self.num2
    
# Key points : 
# - Class : Calculator is the class name.
# - Constructor : __init__(self, num1, num2) initializes two numbers. 
# - Attributes : self.num1 and self.num2 store numbers for the object.
# - Method: add() defines the action of adding two numbers. 

# Usage:

# Create an object 
calc = Calculator(5, 3)

# Call the add method
print(calc.add())           # 8  