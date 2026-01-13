def checkNumberLength( number): 
	status = "invalid"
	if 13 <= len(number) <= 16: 
			status = "valid Card"
	return status


def checkIfValid( number):
	status = "invalid Card"
	sum = getSumOfEvenAndOdd(number)
	if sum % 10 == 0:
		status = "valid Card"    
	return status


def getSumOfEvenAndOdd( number) :
	odd = 0
	even = 0
	
	for index in range(len(number) -1, -1, -2):
		character = number[index]
		odd += int(character)

	for index in range(len(number) - 2, -1 ,-2):
		character = number[index]
		temp = int(character)
		temp4 = temp * 2
		
		
		if (temp4 > 9):
			temp4 = (temp4 - 9)
			even += temp4
        	
		else:
			even += temp4
		
	return even + odd


def getCardType( number) :
	cardType = ""
	if number.startswith("4"):
		cardType = "Visa Card"

	elif number.startswith("5"):
		cardType = "Master Card"

	elif number.startswith("37"):
		cardType = "American Express Card"

	elif number.startswith("6"):
		cardType = "Discover Card"

	else :
		cardType = "Invalid Card Type"

	return cardType
    
    
number = input("Enter a number: ")
    
print("Credit card digit length: " + str(len(number)))
        
print("Credit Card Number: " + number)
        
print("Credit Card Type: "  + str(getCardType(number)))
        
print("Credit Card Validity Status: " + str(checkIfValid(number)))
                              
