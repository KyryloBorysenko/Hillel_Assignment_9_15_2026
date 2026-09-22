#1
square = int(input("Write your number: "))
print(square ** 2)
print()

#2
num1 = int(input("First number: "))
num2 = int(input("Second number: "))
num3 = int(input("Third number: "))
print((num1 + num2 + num3) / 3)
print()

#3
minutes = int(input("How much minutes: "))
hours = minutes // 60
hoursMinutes = minutes % 60
print("it's", hours ,"hours", hoursMinutes, "minutes")
print()

#4
price = int(input("Price: "))
discount = int(input("What is a discount: "))
totalDiscount = discount / 100
totalPrice = price - (price * totalDiscount)
print("Price: " + str(price))
print("Discount: " + str(discount))
print("Price with discount: " + str(totalPrice))
print()

#5
findNumber = int(input("Write down your number: "))
lastDigit = findNumber % 10
print(lastDigit)
print()

#6
length = int(input("Length: "))
width = int(input("Width: "))
totalPerimeter = (length + width) * 2
print("Perimeter of a triangle is", totalPerimeter)
print()

#7
rowNumbers = int(input("Write a numbers (1234): "))
result1 = rowNumbers // 1000
result2 = (rowNumbers // 100) % 10
result3 = (rowNumbers // 10) % 10
result4 = rowNumbers % 10

print(result1)
print(result2)
print(result3)
print(result4)