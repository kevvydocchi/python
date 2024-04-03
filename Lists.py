stack = []
stack.append(1)
stack.append(2)

##print(stack)

pop_elem = stack.pop()

print(stack, pop_elem)


queue = []
queue.append(1)
queue.append(2)

pop2_elem = queue.pop(0)

print(queue, pop2_elem)

list = [1,0,2,0,4,6]

for item in list:

    if item == 0:
        list.remove(item)
        list.append(item)

print(list)

