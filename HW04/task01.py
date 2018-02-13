checknum = int(input('Enter your number so I could find something for you:\n'))
if 0 < checknum < 37:
  number = 999
  while number < 9999:
      number += 1
      num = str(number)
      sumnumber = (int(num[0]) + int(num[1]) + int(num[2]) + int(num[3]))
      if sumnumber == checknum:
          print number
else:
    print 'For this value there are no 4-digit numbers which sum of digits would be equal to enterd value'
