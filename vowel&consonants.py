string_input = input ("Enter A Name: ") . lower()
print(string_input)

numbers_of_vowel = 0
numbers_of_consonants = 0

for letter in string_input:
    if letter == "a" or letter == "i" or letter == "e" or letter == "o" or letter == "u":
	       numbers_of_vowel += 1
	       
    else:
        numbers_of_consonants += 1

print("Consonant no: ", numbers_of_consonants)
print("Vowel no: ", numbers_of_vowel)
