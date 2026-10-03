list = [15, 20, 30]

if len(list) >= 1:
    c = list.pop()
    list.insert(0, c)
    print(list)
else:
    print(list)