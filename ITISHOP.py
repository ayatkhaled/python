print("welcome to our ITI Shop")
print("1-Are you owner?")
print("2-Are you coustomer?")
print("3-Exit")
print("=========================")
choise= int(input("Enter your choise "))
mydic = {}
my_dict = {'1-apple':70 , '2-banana':50,'3-orange':60}
dict = {'1-apple':15 , '2-banana':20,'3-orange':17}

if(choise==1):
	print("hello owner")
	while True:
		userName= (input("Enter your user name "))
		password= int(input("Enter your password "))
		if(userName=="ahmed" and password==1234):
			print("welcome MR ahmed")
			print("Tell me how can I help you")
			print("=========================")
			print("1-Add New Product")
			print("2-Show Product")
			print("3-Change Cost")
			print("4-Exit")
			print("=========================")
			select= int(input("Enter your choise "))
			
			if(select==1):
				print(my_dict)
			
			if(select==2):
				
				print(my_dict)
			if(select==3):
				
				print(dict)
				sel=int(input("select the item you want to change its price "))
				if (sel==1):
					key='1-apple'
					change= int(input("Enter the new price "))
					dict[key] = change
					print(dict)
				if (sel==2):
					key='2-banana'
					change= int(input("Enter the new price "))
					dict[key] = change
					print(dict)
				if (sel==3):
					key='3-orange'
					change= int(input("Enter the new price "))
					dict[key] = change
					print(dict)
				
				
				
			if(select==4):
				print("Good Bye sir")
				exit()
			
			
			
		else:
			print("ivalid password or user name please try again")
	
if(choise==2):
	print("welcome sir")
	print("that what we have")
	print(dict)
	ch= int(input("chose the item "))
	if (ch==1):
		key='1-apple'
		amount= int(input("Enter the amount "))
		price=dict.get('1-apple')
		total=price*amount
		print(total)
	
	if (ch==2):
		key='2-banana'
		amount= int(input("Enter the amount "))
		price=dict.get('2-banana')
		total=price*amount
		print(total)
	if (ch==2):
		key='3-orange'
		amount= int(input("Enter the amount "))
		price=dict.get('3-orange')
		total=price*amount
		print(total)	
	
if(choise==3):
	print("Good Bye sir")
	exit()


