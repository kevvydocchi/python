"""
List
"""

thislist = ["apple", "banana", "cherry"]
print(thislist)
print(thislist[0])
print(thislist[-1])  # -1 is the last value of the items in the list
print(thislist[-2])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
print(thislist[:5])
print(thislist[2:])
print(thislist[-4:-1])

mylist = ["apple", "banana", "cherry"]
if "apple" in mylist:
    print("Yes, apple is in my list")
else:
    print("No, apple is not in mylist")


mylist[1] = "strawberry"
print(mylist)   

thislist = ["apple", "banana", "cherry"]
# thislist[1:3] = ["strawberry", "watermelon"]
print(thislist)
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

# Insert function without replacing any of the existing values
thislist = ["apple", "banana", "cherry"]
thislist.insert(2,"watermelon") # insert from index 2
print(thislist)

thislist.append("orange") # append to the end of the listHI 

print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange") # insert from index 1
print(thislist) 

thislist2 = ["mango", "pineapple", "papaya"]
thislist.extend(thislist2) # append another list to the current list
print(thislist)
thistuple = ("watermelon","peach")
thislist.extend(thistuple) # extend can append tuple, set and dictionary
print(thislist)
thisdict = {"name" : "Tobias",
            "year" : 2004
}
thislist.extend(thisdict) # extend function can add dictionary key values
print(thislist)

thislist.remove("mango") # remove the specific item
print(thislist)

thislist.pop(1) # remove the specific index
print(thislist)

thislist.pop() # remove the last item
print(thislist)

del thislist[0] # remove the specific index
print(thislist)

thislist = ["apple", "banana", "cherry"]
print(thislist)

thislist = ["apple", "banana", "cherry"]

thislist.clear()
print(thislist)

thislist = ["apple", "banana", "cherry"]

for x in thislist:
    print(x)

print(len(thislist))    

for i in range(len(thislist)):
    print(thislist[i])

print("\n")
print("Using while loop")

i = 0
while i < len(thislist):
    print(thislist[i])
    i += 1   

[print(x) for x in thislist]

fruits = ["apple", "bannana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

newlist = []

newlist = [x for x in fruits if "n" in x]
print(newlist)

newlist = []
newlist = [x for x in fruits if x != "apple"]
print(newlist)

newlist = []
newlist = [x for x in fruits]
print(newlist)

newlist = []
newlist = [x for x in range(10) if x < 5]
print(newlist)

newlist = []
newlist = [x.upper() for x in fruits]
print(newlist)

newlist = []
newlist = ["hello" for x in fruits]
print(newlist)

newlist = []

for x in fruits:
    if x == "bannana":
        newlist.append("orange")
    else:
        newlist.append(x)

print(newlist)

newlist = []
newlist = [x if x != "bannana" else "orange" for x in fruits]
print(newlist)

"""
Sort function
"""

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print(thislist)

def myfunc(n):
    return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort() # case senstive, resulting in all capital letter being sorted before lower case letters
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower) # case insenstive sort
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

"""
Copy list
.copy()
list()
"""

thislist = ["banana", "Orange", "Kiwi", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(thislist)

# there are several ways to join, or concatenate, two or more lists in Pythong.
# One of the easiest waok

list1 = [1,2,3]
list2 = ["a", "b", "c"]
list3 = list1 + list2
print(list3)

list1 = [1,2,3]
list2 = ["a", "b", "c"]
for x in list2:
    list1.append(x)

print(list1)

list1 = [1,2,3]
list2 = ["a", "b", "c"]
list1.extend(list2)
print(list1)
