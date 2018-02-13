value = int(input('Enter your value:\n'))
val = str(value)
sum = 0
for i in range(len(val)):
  d = int(val[i])
  d3 = d*d*d
  sum = sum + d3
print('The sum of numbers\' cubes of your value is {}.'.format(sum))
