first_number = int(input("Enter first number: "))

second_number = int(input("Enter second number: "))

result = first_number // second_number

if second_number != 0:
    print(result)

if second_number == 0:
    print("cannot divide by zero")
