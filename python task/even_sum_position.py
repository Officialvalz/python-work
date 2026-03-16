numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_sum = 0

for nums in range (len(numbers)):
	if nums % 2 == 0:
	
			even_sum = even_sum + numbers[nums]
			
print("Even Sum Positions " , even_sum)
