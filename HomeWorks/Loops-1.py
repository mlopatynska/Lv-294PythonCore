a=int(raw_input("Enter a number "))
i=0
for i in range(1000,10000):
	k=i
	p1=k%10
	k=k//10
	p2=k%10
	k=k//10
	p3=k%10
	k=k//10
	p4=k%10
	s= p1+p2+p3+p4
	if a==s:
		print i
	i+=1
		
