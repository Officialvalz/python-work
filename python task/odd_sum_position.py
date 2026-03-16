numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_sum = 0

for nums in range (len(numbers)):
	if nums % 2 != 0:
	
			odd_sum = odd_sum + numbers[nums]
			
print("Odd Sum Positions " , odd_sum)
