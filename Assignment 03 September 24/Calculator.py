operation = input("What do you want +, -, *, /: ")

firstNum = int(input("First number: "))
secondNum = int(input("Second number: "))

if operation == "+":
    result = firstNum + secondNum
    print("result: " + str(result))
elif operation == "-":
    result = firstNum - secondNum
    print("result: " + str(result))
elif operation == "*":
    result = firstNum * secondNum
    print("result: " + str(result))
elif operation == "/":
    if secondNum == 0:
        print("You can't divide by 0")
    else:
        result = firstNum / secondNum
        print("result: " + str(result))