balance = 0
transactions = [ ]

def show_menu():
		print("\n=====  MENU  ======")

		print("1:    Deposit Money")
		print("2:    Withdraw Money")
		print("3:    View History")
		print("4:    Check Balance")
		print("5:    Exit ")

		print("========================")

def deposit_money():
		global balance

		print("\n----------    Add Money   ---------")
		
		amount = float(input("How Much Money Do You Want To Add To Your Account?  $"))

		if amount <= 0:
			print("You Cannot Add A Negative Amount!  $0")
			return


		balance = balance + amount
		transaction = "Deposited $"+ str(amount) + "|  New  balance:  $" +   str(balance)
		transactions .append(transaction)

		print("You Have Successfully Added Funds To Your Account: $"    +    str(amount))
		print("Your New Balance is: $"    +    str(balance))

def withdraw_money():
		global balance


		print("\n----------------  Withdraw Money ------------------------")
		
		amount = float(input("How Much Money Do You Want Withdraw? $"))

		if amount <= 0:
						print("you cant take out $0 nagetive money! ")
						return
				
		if amount > balance:
				print("Not Enough Money! You Only Have $" + str(balance))
				return

		balance = balance - amount

		transaction = "Withdrew $" + str(amount) + "  |  New  balance:  $"   + str(balance)
		transactions .append(transaction)
					
		print("Withdrawal Successful $" + str(amount))
		print("Your New Balance Is: $" + str(balance))

def view_history():
		print("\n=======  TRANSACTION HISTORY  ===========")
		
		if len(transactions) == 0:
				print("No Transaction Yet")
		else:
				counter = 1
				for transaction in transactions:
						print(f"{counter}.{transaction}")
						counter += 1
		
		print("===============================")
		
		
def check_balance():
		print("\n-----    YOUR BALANCE    ---------")
		
		print("Your Account Balance Is:    $"  + str(balance))
		
		
print("Welcome To The Transaction Log App")
print("This App Helps You Track Your Money. ")

running = True


while running:
		show_menu()
		
		choice  = input("What Would You Like To Do?  Please Select A Number From 1, 2, 3, 4, 5:")
		
		if choice == "1":
				deposit_money()
			
		elif choice == "2":
				withdraw_money()
				
		elif choice == "3":
				view_history()
				
		elif choice == "4":
				check_balance()
				
		elif choice == "5":
				print("Thank You For Using The App")
				print("Goodbye")
				running = False
				
		else:
				print("That is not a valid choice.  please enter  1, 2,  3,  4; or 5 to exit. ")
				
print("End of program. ")
			
	
