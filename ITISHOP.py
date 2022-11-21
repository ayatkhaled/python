import csv
print("welcome to our ITI Shop")
print("1-Are you owner?")
print("2-Are you coustomer?")
print("3-Exit")
print("=========================")
choise= int(input("Enter your choise "))
mydic = {}
my_dict = {'1-apple':70 , '2-banana':50,'3-orange':60}
dict = {'1-apple':15 , '2-banana':20,'3-orange':17}
employee={'ahmed':200,'ali':100}
fired=["tamer","ayat"]
thislist = ["ali", "amany", "yasser"]

if(choise==1):
	print("hello owner")
	userName= (input("Enter your user name "))
	password= int(input("Enter your password "))
	while True:
		
		if(userName=="ayat" and password==1234):
			print("welcome MISS ayat")
			print("Tell me how can I help you")
			print("=========================")
			print("1-Add New Product")
			print("2-Show Product")
			print("3-Change Cost")
			print("4-add new employee")
			print("5-add new one to fired")
			print("6-exit")
			print("=========================")
			select= int(input("Enter your choise "))
			
			if(select==1):
				print(my_dict)
				sel=(input("write the new item "))
				price=int(input("enter its price "))
				my_dict[sel]=price
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
				
				
				
			if (select==4):
					print(employee)
					new= input("Enter the name of the new one ")

					salary=int(input("enter his salary "))
					employee[new]=salary
					print(employee)
					my_dict = {"test": 1, "testing": 2}
					with open('names.csv', 'w') as f:  # You will need 'wb' mode in Python 2.x
						w = csv.DictWriter(f, employee.keys())
						w.writeheader()
						w.writerow(employee)
			if (select==5):
					print(fired)
					fired= input("Enter the name of fired one ")
					print (fired)
					thislist.append(fired)
					print(thislist)
					with open('fired.csv', 'w') as myfile:
						wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
						wr.writerow(thislist)
					

					
                    					
			if(select==6):
				print("Good Bye sir")
				exit()
			
			
			
		else:
			print("ivalid password or user name please try again")

if(choise==2):
	print("welcome sir")
	print("that what we have")
	print(dict)
	while True:
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
		if (ch==3):
			key='3-orange'
			amount= int(input("Enter the amount "))
			price=dict.get('3-orange')
			total=price*amount
			print(total)	
	
if(choise==3):
	print("Good Bye sir")
	exit()


