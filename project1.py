# Program make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

	

def hexa(m):
    return hex(m) 
def octa(l):
    return oct(l)    	

print("Select calculator mode.")
print("1.scintific")
print("2.programing")
print("================================")

while True:
    # take input from the user
	choice = input("chose 1 or 2: \n")
   
    
    # check if choice is one of the four options
	if choice == '1':
		print("Select operation.")
		print("================================")
		print("1.Add")
		print("2.Subtract")
		print("3.Multiply")
		print("4.Divide")
		print("================================")
		choice = input("Enter choice(1/2/3/4): ")
		if choice in ('1', '2', '3', '4'):
			num1 = float(input("Enter first number: "))
			num2 = float(input("Enter second number: "))

			if choice == '1':
				print(num1, "+", num2, "=", add(num1, num2))

			elif choice == '2':
				print(num1, "-", num2, "=", subtract(num1, num2))

			elif choice == '3':
				print(num1, "*", num2, "=", multiply(num1, num2))

			elif choice == '4':
				print(num1, "/", num2, "=", divide(num1, num2))
	if choice == '2':
		print("Select operation.")
		print("1.hex")
		print("2.oct")
		print("3.bin")
		print("4.Divide")
		choice = input("Enter choice(1/2/3/4): ")
		if choice =='1':
			num3 = int(input("Enter a number to covert to hexa \n"))
			print("HEX is "+ hexa(num3))
		if choice =='2':
			num3 = int(input("Enter a number  to convert to octa\n"))
			print("octa is "+ octa(num3))
			
			
        
        # check if user wants another calculation
        # break the while loop if answer is no
	next_calculation = input("Let's do next calculation? (yes/no): ")
	if next_calculation == "no":
		break
    
else:
	print("Invalid Input")