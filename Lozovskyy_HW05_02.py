num = 0
# Enter number and check is that number more than 0
while num < 1:
    num = int(input ("Enter number more than Zero "))
else:
    print "Programm we'll check is the {} simple number".format(num)
# Check is an entered number Prime.
for i in range(2,num):     #to iterate on the factors of the number
    if num%i == 0:            #to determine the first factor
         print "Entered number {} is NOT prime".format(num)
         break
    else:                                # else part of the loop
        print "{} is a prime number!".format(num)
        break