n=raw_input("Enter some list ")

def bubbles(x):
	x=str(x)
	x=list(x)
	j=0
	while j < (len(x)-1):
		
		if x[j] > x[j+1]:
			x[j],x[j+1]=x[j+1],x[j]
			#return x
		j+=1
	print x

bubbles(n)




