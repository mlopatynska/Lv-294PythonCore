checknum = int(input('Enter your number so I could find something for you:\n'))
number = 999
while number < 9999:
    number += 1
    num = str(number)
    sumnumber = (int(num[0]) + int(num[1]) + int(num[2]) + int(num[3]))
    if sumnumber == checknum:
        print number
else:
    print 'That\'s are all 4 digit numbers which sums are eqal to the number'
