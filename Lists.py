lucky_numbers = [4,8,15,16,23,42]
friends = ["Kevin","Karen","Jim","Oscar","Tom","Oscar"]
##friends.extend(lucky_numbers)
friends.append("Creed")
friends.remove("Tom")
friends[1] = "Mike"

print(friends.index("Oscar"))
friends.sort() ## does not support both int and str
print(friends)
print(friends.count("Oscar"))