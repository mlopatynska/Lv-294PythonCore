number = int(input('Enter your number below:\n'))
if number > 0:
  f1 = 0
  f2 = 1
  count = 0
  print ('Fibonacci numbers for entered number of times will be:\n')
  while count < number:
    print f1
    count += 1
    fn = f1 + f2
    f1 = f2
    f2 = fn
else:
  print('You\'ve entered wrong number!')
