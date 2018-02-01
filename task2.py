a = int(raw_input("Enter some number from 1000 to 9999:  \n"))
b=list(str(a))
b.sort()

p1=a%10
a=a//10
p2=a%10
a=a//10
p3=a%10
a=a//10
p4=a%10


print "The sum of number is", p1+p2+p3+p4
print "Reverse is", p1,p2,p3,p4
print "Values from the smalest to the largest "," ".join(b)
