primenum = int(input('Enter your number to check if it\'s prime:\n'))
if primenum > 1:
  for i in range (2, primenum):
    if primenum % i == 0:
      print('Entered number is not prime, cause {} can be devided by {} to receive integer {}.'.format(primenum, primenum // i, i))
      break
  else:
    print('{} is a prime number!'.format(primenum))
else:
  print('Entered number is not prime.')
