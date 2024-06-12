numberToFind = 5

for number in range(10):
    if number == numberToFind:
        print("Number found")
        break
else:
    print("Number not found")
