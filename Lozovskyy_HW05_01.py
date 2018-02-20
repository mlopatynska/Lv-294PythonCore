num = 0
while num > 36 or num < 1:
    num = int(input ("Enter number between 1 and 36: "))
else:
    print "Programm we'll find all 4-digits number with sum {}".format(num)

for i in range(1000,10000):   #Iterration of 4 digit numbers
    sum = int(str(i)[0]) + int(str(i)[1]) + int(str(i)[2]) + int(str(i)[3])
    if sum == num:
        print "print Sum of {} digits = {} and = entered {}".format(i, sum, num)
