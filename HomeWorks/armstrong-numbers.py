number=raw_input("Enter a number ")
su=0
import math
for i in number:
	
	su+=math.pow(int(i),len(number))
	

if int(number)==su:
	print"It is Armstrong's number"
else:
	print"It is not Armstrong's number"
		