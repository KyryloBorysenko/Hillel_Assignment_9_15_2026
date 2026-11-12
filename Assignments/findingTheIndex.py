def second_index(text, some_str):
    first = text.find(some_str)

    if first == -1:
        return None

    second = text.find(some_str, first + len(some_str))

    if second == -1:
        return None

    return second

massage = input("your massage: ")
letter = input("What letter do you want to find: ")

print(second_index(massage, letter))