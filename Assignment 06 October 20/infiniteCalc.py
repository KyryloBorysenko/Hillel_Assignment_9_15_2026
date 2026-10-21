while True:
    firstNum = int(input("First number: "))
    operator = input("What operator: ")
    secondNum = int(input("Second number: "))

    if operator == "+":
        print(firstNum + secondNum)
    elif operator == "-":
        print(firstNum - secondNum)
    elif operator == "*":
        print(firstNum * secondNum)
    elif operator == "/":
        print(firstNum / secondNum)
    else:
        print("Invalid operator")

    answer = input("Do you want to continue? yes/no: ")

    if answer.lower() not in ("yes", "y"):
        break

print("Calculator stopped")