def raise_to_power(base_num, pow_num):
    counter = 0
    res = 1
    while counter < pow_num:
        res = res * base_num
        counter +=1
        print(res)

raise_to_power(2,4)
