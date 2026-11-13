def add_one(some_list):
    number = int("".join(map(str, some_list))) # перетворюємо рядок у повне число
    number += 1 # додаємо один до числа

    return [int(digit) for digit in str(number)] # переиворюємо усе у список

listik = input("Write numbers: ")
print(add_one(listik))