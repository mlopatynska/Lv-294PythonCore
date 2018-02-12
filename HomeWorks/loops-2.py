a=input("Enter a number  ")
for n in range(2,a):
	if a%n:
		print("Your number is simple")
		break
	else:
		print("Your number is complicated")
		break
