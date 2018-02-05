number = input("Enter the 4-digit number:\n")
num = str(number)
product =( int(num[0]) * int(num[1]) * int(num[2]) * int(num[3]))
print("The product of number of enetered value is {}".format(product))
rev = num[::-1]
print("The reverse of your number will be {}".format(rev))
sort = (''.join(sorted(num)))
print("Sorted from A to Z your number will be following: {}".format(sort))