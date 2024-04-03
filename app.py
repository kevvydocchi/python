character_name = "Tom"
character_age = 50.1
Is_male = False
print("There once was a man name " + character_name + ", ")
print("he was " + str(character_age) + " years old.")

character_name = "Mike"
print("He really like the name " + character_name + ", ")
print("but didn't like being " + str(character_age) + ".")


for i in range(6):
    print(i)


sum = 0
for i in range(2, 22, 2):
    sum = sum + i
    print(f"sum =" , sum)

numbers = [1, 2, 3, 4, 5]
# iterate over each element in list num
for i in numbers:
    # ** exponent operator
    square = i ** 2
    print("Square of:", i, "is:", square)


numbers = [10, 20, 30, 40, 50]

# definite iteration
# run loop 5 times because list contains 5 items
sum = 0
for i in numbers:
    sum = sum + i
    print("sum=",sum)
list_size = len(numbers)
print("list_size=", list_size)
average = sum / list_size
print(average)

for i in range(1,11):
    if i % 2 ==0:
        print('Even number:', i)
    else:
        print('Odd number:',i)


