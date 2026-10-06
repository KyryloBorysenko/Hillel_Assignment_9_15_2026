list = [0, 1, 0, 12, 3]
zeros = 0

for i in range(len(list)):
    if list[i] == 0:
        zeros += 1
    else:
        list[i - zeros] = list[i]

for i in range(len(list) - zeros, len(list)):
    list[i] = 0

print(list)