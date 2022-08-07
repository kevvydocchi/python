
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(3,4))


def raise_to_pow(base_num, pow_num):
    counter = 0
    res = 1
    while counter < pow_num:
        res = res * base_num
        counter +=1
    return  res

print(raise_to_pow(3,4))