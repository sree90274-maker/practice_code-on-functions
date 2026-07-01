#functions
def sum(a,b):
	c=a+b
	print("sum of two numbers is :",c)
sum(10,20)
print("______________________________")
def hello():
	print("hello World")
hello()
#print("______________________")
def name():
	name="abc"
	print("name")
name()
#print("____________________________")
def sum(a,b,c,d,e,):
	c=a+b+c+d+e,
	return c
sum(10,20,30,40,50,)
print(sum(10,20,30,40,50))
print("__________________________")
def fruits(apple,org):
	c=apple,org
	return c
f=fruits("apple","org")
print(f)
print("________________________")
def product(num1,num2):
	c=num1*num2
	return c
p=product(19,2)
print(p)
print("_______________________")
def numbers():
	for i in range(1,6):
		return i
n=numbers()
print(n)
print("_________________________")
a=int(input("enter a number:"))
if a>-10 and a<10:
	print("single digit")
elif a>-100 and a<100:
	print("double digit")
elif a>-1000 and a<1000:
	print("thrible digit")
else:
	print("no possible digits")
print("____________________________")
def num(n):
	if n%2==0:
		print("it is a even")
	else:
		print("not a even")
num(6)
print("________________________")
#Find square
def square(n):
	a=n**n
	return a
a=square(12)
print(a)


