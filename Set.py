"""
Set
"""
# Sets are used to store multiple items in a single variable
# Set is one of 4 build-in data types in Python used to store collection of data, the other 3 are
# List, Tuple and Dictionary, all with different qualities and usage.
# A set is a collection which is unordered, unchangeable*, and unindexed
# Set items do not allow duplicate values.
# Note : Set items are unchangeable, but you can remove items and add new items
# Sets are written with curly brackets.

thisset = {"apple", "banana", "cherry"}
print(thisset)

# Sets can not have two items with the same value.
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
print(len(thisset))

# Set items can be of any data type:
set1 = {"apple", "banana", "cherry"}
set2 = {1, 2, 3, 5, 7, 9, 3}
set3 = {True, False, False}
print(set1)
print(set2)
print(set3)

# A set with strings, integers and boolean valuses:
set1 = {"abc", 34, True, 40, "male"}
print(set1)

myset = {"apple", "banana", "cherry"}
print(type(myset))

# It is also possible to use the set() contructor to make a set.
thisset = set(("apple", "banana", "cherry"))
print(type(thisset))
print(thisset)

## As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

# You cannot access items in a set by referring to an index or a key
# But you can loop through the set items using a for loop, or ask if a specified value is present in a set,
# by using the in keyword.
thisset = {"apple", "banana", "cherry", "apple", "banana", "watermelon"}
for x in thisset:
    print(x)