def say_hi(name, age):
    return f"Hi. My name is {name} and I'm {age} years old"

name = input("What is your name: ")
age = int(input("How old are you: "))

print(say_hi("Kyrylo", 17))
print(say_hi(name, age))

print('ОК')