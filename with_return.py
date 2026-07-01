#functions with return
def sum(a,b):
	c=a+b
	return c
d=sum(30,40)
print(d)
#factorial of a number
def factorial(n):
	fact=1
	for i in range(1,n+1):
		fact=fact*i
	return fact
print(factorial(9))
print("________________")
def total(numbers):
    return sum(numbers)
nums = [2, 3, 4, 5]
result = total(nums)
print("Sum of elements:", result)