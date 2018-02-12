
z = input("Enter a number for 1 to 36 \n")

for tr in range(1000,10000):

    suma = int(str(tr)[0]) + int(str(tr)[1]) + int(str(tr)[2]) + int(str(tr)[3])
    if suma == z:
        print "number {} the sum of numbers of which is equal to the given number {}".format(tr, z)