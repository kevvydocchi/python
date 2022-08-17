# Like may other popular programming lanuguages, strings in python are arrays of bytes representing 
# unicode charaters.
# However, Python does nothave a charater data type, a single charater is simply a string with a length
# of i

from posixpath import split


a = "Hellow World!"
print(a[1])
print(len(a))

for x in "banana":
    print(x)

txt = "The best things in life are free!"
print("free" in txt)

if "free" in txt:
    print("Yes, 'free' is present")

txt = "The best things in life are free!"
print("expensive" not in txt)

b = "Hellow World!"
print(b[2:5])
print(b[:5])
print(b[-5:-2])
print(b.upper())
print(b.lower())

# The strip() method removes an whitespace from the beginning or the end
s = " Hellow World! "
print(s.strip())

# The replace() method replaces a string with another string
s = " Hellow World! "
print(s.replace("H","J"))


# The split() method returns a list where the text between the specified separator becomes the list items
a = "Hello, World!"
print(a.split(","))

# String Concatenation
a = "Hello"
b = "World"
c = a + " " + b
print(c)

# We can combine strings and numbers by using format() method
# The format() method takes the passed arguments, formats them, and places them in the string where
# the placeholders {} are
age = 36
txt = "My name is John, I am {}"
print(txt.format(age))

# The format() method takes umlimited number of arguments, and are placed into the respective placeholders
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars"
print(myorder.format(quantity, itemno, price))

# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# Escape
# To insert charaters that are illegal in a string, use an escape character
# An escape character is a backlash \ followed by the character you want to insert
# To fix this problem, use the escapre character \"

txt = "We are the so-called \"Vikings\" from the north."
print (txt)

