daynum = int(input('Enter the number between 1 and 365:\n'))
if 1 <= daynum <= 365:
  countday = (daynum % 7) - 1
  dayslist = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
  print('The corresponding day for entered number will be {}'.format(dayslist[countday]))
else:
  print('You\'ve entered wrong number!')
