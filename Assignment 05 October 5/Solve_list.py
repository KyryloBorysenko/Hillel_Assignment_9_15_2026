list = [1, 5, 6, 2, 0, 2, 2, 1]

if list:
    result = sum(list[:-1:2]) * list[-1]
else:
    result = 0

print(result)