# roman to integer

def roman_to_integer(roman):
    value = {
        "i": 1,
        "v": 5,
        "x": 10,
        "l": 50,
        "c": 100,
        "d": 500,
        "m": 1000
    }

    # initialise previous chara and answer
    p = 0
    ans = 0
    roman_lower = roman.lower()

    n = len(roman_lower)
    for i in range(n - 1, -1, -1):

        # If greater than equal to previous
        # add to answer
        if p <= value[roman_lower[i]]:
            ans += value[roman_lower[i]]

        # If small than previous
        # substract from ans
        else:
            ans -= value[roman_lower[i]]

        p = value[roman_lower[i]]
    print("Integer is " + str(ans))


roman_to_integer(input("Please Enter a roman numerals "))
