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

import this


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

 # add() method to add one item
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

# update() to add items from another set into the current set
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

# The object in the update() method does not have to be a set, it can be of any iterable object 
# tuples, lists, distionaries etc
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

# remove() or discard() method to remove an item in a set
thisset = {"apple", "banana", "cherry"}
thisset.remove("apple")
thisset.remove("banana")
print(thisset)

# You can also use the pop() method to remove an item, but this method will remove the last item
# Remember that sets are unordered, you will not know what item that gets removed.
thisset = {"apple", "banana", "cherry", "orange", "watermelon"}
x = thisset.pop()
print(x)

# clear() method to empty the set
thisset = {"apple", "banana", "cherry", "orange", "watermelon"}
thisset.clear()
print(thisset)

# The del keyword will delete the set completely
thisset = {"apple", "banana", "cherry", "orange", "watermelon"}
#del thisset
print(thisset)

# You can loop through the set items by using a for loop:
thisset = {"apple", "banana", "cherry", "orange", "watermelon"}
for x in thisset:
    print(x)

# Join two sets
# There are serveral ways to join two or more sets in Python
# You can use the union() method that returns a new set containing all items from both sets,
# or the update() method that inserts all the items from one set into another
set1 = {"a", "b", "c", "d"}
set2 = {1,2,3,4}
set3 = set1.union(set2)
print(set3)

# The intersection_update() method will keep only the items that are present in both sets
# Keep the items that exist in both set x, and set y
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

# The intersection() method will retrun a new set, that only contains the items that are present in
# both sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)

# The symmetic_difference_update() method will keep only the elements that are not present in both sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

# The symmetric_difference() will return a new set, that contains only the elements that are not present in both sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)

# add()	Adds an element to the set
# clear()	Removes all the elements from the set
# copy()	Returns a copy of the set
# difference()	Returns a set containing the difference between two or more sets
# difference_update()	Removes the items in this set that are also included in another, specified set
# discard()	Remove the specified item
# intersection()	Returns a set, that is the intersection of two other sets
# intersection_update()	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	Returns whether two sets have a intersection or not
# issubset()	Returns whether another set contains this set or not
# issuperset()	Returns whether this set contains another set or not
# pop()	Removes an element from the set
# remove()	Removes the specified element
# symmetric_difference()	Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	inserts the symmetric differences from this set and another
# union()	Return a set containing the union of sets
# update()	Update the set with the union of this set and others