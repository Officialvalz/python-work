word = ("apple")

inverse = ' '

for letter in word:
         print(letter,  end="\t")
         inverse = letter + inverse
         
print()

print(inverse)


