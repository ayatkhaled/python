import os
import time


n=5

print('\t\t\t\t\t\t\t\t\t\t\t\t')

print('*')

for i in range(0,7):

	for j in range (0,i+1):
		print('*',end=" ")
	print()
for i in range(7,1,-1):
	for j in range (1,i):
		print('*',end=" ")
	print()
time.sleep(2)
os.system('cls')
# Number of rows
n=6


print('\t      *')
print('\t      *')
print('\t      *')
print('\t      *')
print('\t      *')
print('\t      *')	
print('\t      *')
n=7
for i in range(n):
	for j in range (i+1):
		print(' ',end=' ')
	for j in range (i,n):
		print('*',end=' ')

	for j in range (i,n):
		print('*',end=' ')
	print()	

time.sleep(2)
os.system('cls')	
n=7
for i in range(n):
	for j in range (i,n):
		print(' ',end=' ')
	for j in range (i+1):
		print('*',end=' ')

	for j in range (i+1):
		print('*',end=' ')
	print()	
print('\t      *')
print('\t      *')
print('\t      *')
print('\t      *')
print('\t      *')
print('\t      *')	
print('\t      *')
time.sleep(2)
os.system('cls')	
n=7

	
for i in range(n-1):
	for j in range (i+1):
		print('*',end=' ')
	print()	
for i in range(n):
	for j in range (i,n):
		print('*',end=' ')
	print()
time.sleep(2)
os.system('cls')		
