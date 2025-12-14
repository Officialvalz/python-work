drive_distance = float(input("Enter the driving distance: "))

miles_per_gallon = float(input("Enter miles per gallon: "))

price_per_gallon = float(input("Enter price per gallon: "))

cost  =  (drive_distance / miles_per_gallon) * price_per_gallon

print(f"{cost:.2f}")
