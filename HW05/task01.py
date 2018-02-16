list = [22, 11, 6, 87, 34, 55, 74, 2, 109]
min, max = list[0], list[0]
for i in list:
  if i < min:
    min = i
for i in list:
  if i > max:
    max = i
dict = {'min': min, 'max': max}
print dict
