f = open("/Users/kevincho/test/test.txt", "r")
print(f.read())


a = open("/Users/kevincho/test/test.txt", "a")
a.write("this line has been appened")
a.close()


f = open("/Users/kevincho/test/test.txt", "r")
print(f.read())





