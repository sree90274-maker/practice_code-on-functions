#functions with no arguments
def Hello():
	print("HelloWorld")
Hello()
print("____________________")
def durgasree():
	print("durgasree")
durgasree()
print("__________________")#print 1 to 10 numbers
def numbers():
	for i in range(1,11):
		print(i)
numbers()
print("_________________")#print 10 to 11 numbers
def numbers():
	for x in range(10,0,-1):
		print(x)
numbers()
print("_________________")#print even_numbers 1 to 100
def even_numbers():
	for num in range(1,101):
		if num%2==0:
			print(num)
even_numbers()

print("_____________")#print odd_numbers 1 to 100
def odd_numbers():
	for i in range(1,101):
		if i%2!=0:
			print(i)
odd_numbers()
print("__________________________")
def table():
	for i in range(1,11):
		print("5 x",i,"=",5*i)
table()
