def perestanovka(x,y):
	import random
	import math
	x=list(x)
	Y=[ ]
	F=[ ]
	i=0
	l=len(x)

	l=math.factorial(l)
	while i<l:
		random.shuffle(x)
		F=(" ".join(x))
		if F in Y:
			continue
		else:
			Y[len(Y):]=[F]
			#print F
			i+=1
	print Y
	if y in Y:
		print "Ok"
		#if y in F:
			#print "Ok"
		#else:
			#continue
			

print perestanovka("mama","mama")

#http://www.cyberforum.ru/python/thread44963.html
		
