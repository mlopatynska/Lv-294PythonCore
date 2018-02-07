a = raw_input ("Enter some number from 1000 to 9999: \n")
a = int(a)

b = list(str(a))
b.sort()

d1 = a % 10
a = a // 10
d2 = a % 10
a = a // 10
d3 = a % 10
a = a // 10
d4 = a % 10
a = a // 10


print "Summ of numbers:", d1 + d2 + d3 + d4

print "Reverse from number is:",  d1, d2, d3, d4

print "The value from the smallest to the largest: ", " ".join(b)