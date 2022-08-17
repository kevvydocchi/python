# Boolean
# When you compare two values, the expression is evaluated and Python returns the Boolean answer
print(10>9)

# The bool() function allows you to evaluate any value, and give you True or Fales in return
print(bool("Hello"))

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

print(bool(0))

z = []
print(bool(z))

class myclass():
    def __len__(self):
        return 0
        
myobj = myclass()
print(bool(myobj))

# You can create functionis that returns a Boolean Value
def myFunction():
    return True

print(myFunction())

# Python also has many bilt-in functions that return a boolean value, like the isinstance() function
# which can be used to determine if an object is of a certain data type
x = 200
print(isinstance(x, int))

# Module
x = 5
y = 2
print(x % y)