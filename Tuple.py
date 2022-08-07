mytuple = ("apple", "banana", "cherry")
print(mytuple)

# Since tuples are indexed, they can have items with the same valuse:
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(len(thistuple))  # how many items a tuple has

thistuple = ("apple",)
print(type(thistuple))


thistuple = ("apple")
print(type(thistuple))
print(thistuple)

# Tuple items can be of any data type:

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
print(type(tuple1))
print(type(tuple2))
print(type(tuple3))

# Tuple can contain different data types: strings, integers and boolean values
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)

# It is possible to use tuple() constructor to make a tuple

thistuple = tuple(["apple", "banana", "cherry"]) # note the double round-brackets
print(thistuple)
print(type(thistuple))
print(thistuple[1])
print(thistuple[-1])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5]) # the search will start at index 2 (included) and end at index 5 (not included)

print(thistuple[2:]) 

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])
if "apple" in thistuple:
    print("Yes, apple is in the fruits tuple")

# Once a tuple is created, you cannot change its values. Tuples are unchangeable, 
# or immutable as it also is called
# But there is a workaround. You can covert the tuple into a list, 
# and convert the list back into a tuple

x =  ("apple", "banana", "cherry") 
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# Since tuplare are immutable, they do not have a build-in append() method, but there are
# other ways to add items to a tuple
# Covert into a list

thistuple = ("apple", "banana", "cherry")
print(thistuple)
y = list(thistuple)
y.append("orange")
print(y)
thistuple = tuple(y)
print(thistuple)

# Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item,
# create a new tuple with the items, and add it to the existing tuple:
thistuple = ("apple", "banana", "cherry")
y = ('orange', 'watermelon')
thistuple = thistuple + y
print(thistuple)

# Tuples are unchangeable, so you can not remove items from it but you can use the same workaround 
# as we used for changing and adding tuple items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

# You can delete the tuple completely. The del keyword can delete the tuple completely.
thistuple = ("apple", "banana", "cherry")
del thistuple
# print(thistuple)

# When we create a tuple, we normally assign values to it. This is called "packing" a tuple.
fruits = ("apple", "banana", "cherry")
print(fruits)

# In Python, we are also allowed to extract the values back into variables. 
# This is called "unpakcing"
fruits = ("apple", "banana", "cherry")
(green, yellow, red ) = fruits
print(green)
print(yellow)
print(red)

# if the nmber of variables is less than the number of values, you can add an * to the variable name
# and the values will be assigned to the variable as a list:

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)

# you can loop through the tuple items by using a for loop
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)

# You can also loop through the tuple items by referring to their index number
# Use the rang() and len() funtions to create a suitable iterable.
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i])

# You can loop through the list items by using a while loop
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i += 1

# Join two or more tuples you can use the + operator
tuple1 = ("a", "b", "c")
tuple2 = (1,2,3)

tuple3 = tuple1 + tuple2
print(tuple3)

# If you want to multiply the content of a tuple a given number of times, you can use * operator
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple) 

# Python has two built-in methods that you can use on tuples
# count() : Returns the number of times a spefied value occurs in a tuple
# index() : Searches the tuples for a specifed value and returns the position of where it was found
print(mytuple.index("apple"))
print(mytuple.count("apple"))

    
