def sayhi(name, age):
    print("Hello World " +name )
    print("This is " +name +". I am " + str(age)  )
print("Start")
sayhi("Kevin",45)
print("End")

def cube(num):
    return num*num*num

result = cube(4)
print(result)

def raise_to_power(base_num, pow_num):
    counter = 0
    res = 1
    while counter < pow_num:
        res = res * base_num
        counter +=1
        print(res)

raise_to_power(2,3)


