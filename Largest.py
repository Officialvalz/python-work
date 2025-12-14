first_nunber = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
third_number = int(input("Enter third numbr: "))

largest= first_number

if second_number > largest:
       largest= second_number

if third_number > largest:
       largest= third_number

print(largest)
