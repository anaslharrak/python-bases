
userInput = ""

while userInput != "exit":
    print("Hello! I'm a simple calculator. I can add, subtract, multiply and divide.")
    print("To exit type \"exit\"")
    userInput = input("Enter the first number: ")

    if userInput.lower() == "exit":
        break
    else:
        firstNumber = float(userInput)
    userInput = input("Enter the second number: ")
    secondNumber = float(userInput)

    print("Choose an operation:")
    print("1 - Add")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - Divide")
    userInput = input("Enter the operation number: ")

    if userInput == "1":
        result = firstNumber + secondNumber
    elif userInput == "2":
        result = firstNumber - secondNumber
    elif userInput == "3":
        result = firstNumber * secondNumber
    elif userInput == "4":
        result = firstNumber / secondNumber
    else:
        print("Invalid operation")
        continue
    print("The result is: " + str(result))
