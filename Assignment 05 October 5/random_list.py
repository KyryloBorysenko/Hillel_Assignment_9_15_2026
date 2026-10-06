import random

list = []

for i in range(random.randint(3, 10)):
    list.append(random.randint(1, 10))

listResult = [list[0], list[2], list[-2]]

print(listResult)