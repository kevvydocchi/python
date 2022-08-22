
s = '*_*'
s = 2 * s + s * 2
print(s)

def foo(x, y, z):
    return x(y(z))
    
print(foo(lambda x: 2*x, lambda x:x//2, 2))


s = ['a','b']
for i in s:
    print(i)
    

    