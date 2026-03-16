numbers = [20, 30, 40, 80, 1200, 200, 50, 90]
value = 1

for index in range (len(numbers)):
		if index % 3 == 0:
				value = value * numbers[index]
					
print("Value at every 3rd positions: " , value)
