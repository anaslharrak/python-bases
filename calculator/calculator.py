"""
This is a simple calculator that can perform basic arithmetic operations.
"""

firstNumber = float(input("Enter the first number: "))
secondNumber = float(input("Enter the second number: "))

addition = firstNumber + secondNumber
subtraction = firstNumber - secondNumber
multiplication = firstNumber * secondNumber
division = firstNumber / secondNumber


mensaje = f"""
    The result of the operation is:
    Addition: {addition}
    Subtraction: {subtraction}
    Multiplication: {multiplication}
    Division: {division}
"""
print(mensaje)
