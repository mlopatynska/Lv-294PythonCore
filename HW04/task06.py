n = int(input('How many number should be in the list?\n'))
list = []
for i in range(0,n):
  list.append(int(input('Enter the value:\n')))
min = list[0]
for i in list:
  if min > i:
    min = i
print('The smallest value from whole entered values is {}.'.format(min))
