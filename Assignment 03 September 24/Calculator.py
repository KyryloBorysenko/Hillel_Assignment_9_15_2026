operation = input("What do you want +, -, *, /: ")

if operation == "+":
    firstNum = int(input("First number: "))
    secondNum = int(input("Second number: "))
    result = firstNum + secondNum
    print("result: " + str(result))
elif operation == "-":
    firstNum = int(input("First number: "))
    secondNum = int(input("Second number: "))
    result = firstNum - secondNum
    print("result: " + str(result))
elif operation == "*":
    firstNum = int(input("First number: "))
    secondNum = int(input("Second number: "))
    result = firstNum * secondNum
    print("result: " + str(result))
elif operation == "/":
    try:
        firstNum = int(input("First number: "))
        secondNum = int(input("Second number: "))
        result = firstNum / secondNum
    except ZeroDivisionError:
        print("You can't divide by 0")
    else:
        print("result: " + str(result))