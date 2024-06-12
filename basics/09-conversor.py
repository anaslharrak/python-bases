temp = float( input("Enter temperature to convert: "))


method = input("Enter C to convert to Celsius, F to convert to Fahrenheit: ").upper()

if method == 'C':
    print((temp - 32) * 5/9)
elif method == 'F':
    print((temp * 9 / 5) + 32)
else:
    print("Invalid method")