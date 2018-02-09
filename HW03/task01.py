year = input('Enter the year to check it:\n')
print('It\'s a leap year' if (not year % 4 and year % 100) or not year % 400 else 'This is not a leap year')