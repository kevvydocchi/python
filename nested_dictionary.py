child1 = {
    "name" : "Nelly",
    "year" : 2004
}

child2 = {
    "name" : "Tobias",
    "year" : 2007
}

child3 = {
    "name" : "Kevin",
    "year" : 2009
}

print(child1.values())
print(child2)
print(child3)

mychild = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
}

print(mychild)

print(child1.get("name"))
print(mychild.get("child1"))

child1.update({"year":1999})
print(child1)
child1.update({"school": "killara high school"})
print(child1)