# Python has no command for declaring a variable
# A variable is created the moment you first assign a value to it
# Variables do not need to be delared with any particular type, and can even change type after they have been set
x = 4 # x is of type int
x = "Sally" # x is not of type str
print(x)

"""
Casting
"""
# If you want to specify the data type of a variable, this can be done with casting
x = str(3)
y = int(3)
z = float(3)
print(x)
print(y)
print(z)

# You can get the data type of a variable with the type() function
x = 5
y = "Jone"
print(type(x))
print(type(y))

# String variables can be declared either by using single or double quotes
x = "John"
x = 'John'

# Variable names are case-senstive
a = 4
A = "Sally"
# A will not overwrite a

"""
Variable Names
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores
# Variable names are case-sensitive
"""

# Camel Case
myVariableName = "John"

# Pascal Case
myVariableName = "John"

# Snake Case
my_variable_name = "John"

# Python allows you to assign values to multiple variables in one line:
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# You can assign the same value to multiiple variables in one line:
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a Collection
# If you have a collection of valuses in a list, tuple. Python allows you to extract the values into variables.
# This is called unpacking
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# In the print() function, you output multiple variables, seperated by a comma:
x = "Python"
y = "is"
z = "awesome"
print(x,y,z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
# Notice the space character after "Python " and "is ", 
# without them the result would be "Pythonisawesome".

# For numbers, the + character works as a mathematical operator
x = 5
y = 10
print(x + y)

"""
Global Variables
# Variables that are created outside of a fuction are known as global variables
# Global variables can be used by everyone, both inside of functions and outside
"""
x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()    

# If you create a variable with the same name inside a function, 
# this variable will be local, and can only be used inside the function. 
# The global variable with the same name will remain as it was, global and with the original value.

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

# To create a global variable inside a fuction, you can use the global keyword
def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)

# To change the value of a global variable inside a function, 
# refer to the variable by using the global keyword:
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)