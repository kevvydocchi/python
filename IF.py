is_male = True
is_tall = False

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a mail but not tall")
elif not(is_male) and is_tall:
    print("You are not a mail and not tall")
else:
    print("You are not a male and not tall")

def max_num(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num3 and num2>=num1:
        return num2
    else:
        return num3

result = max(4,100,6)
print(result)
