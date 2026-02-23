word = "vocabulary"
count = 0
vowels = "aeiouAEIOU"
for char in word:
	if char in vowels:
		count += 1
		
print("vowels >> ", count)
