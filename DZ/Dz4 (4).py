year = input('Put a year\n')
if (not year%4 and year%100) or not year%400:
    print ('Leap year!')
else:
    print('Not a leap year!')
