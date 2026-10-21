number = int(input("Write down your number: "))

while number > 9:
    result = 1 # It's one because everything that is multiply by 1 doesn't changes

# Digit become a string of numbers from variable "number" and split the numbers
    for digit in str(number):
        result *= int(digit) # Multiply each number

    number = result # Change the variable "number" and if number > 9 then repeats

print(number)