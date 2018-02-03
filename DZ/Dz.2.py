from math  import  pow
a = input("Input first number:\n")
b = input("Input second number:\n")
print ('a - b = ' + str(a - b) \
	   + '\na + b = ' + str(a + b) \
	   + '\na * b = ' + str(a * b))
try:
	print('a / b = ' + str(float(a) / b))
except ZeroDivisionError:
	print('You can not divide by zero!!!')
else:
	print('a // b = ' + str(a // b) \
		  + '\na % b = ' + str(a % b))
print('a ^ b = ' + str(pow(a,b)))