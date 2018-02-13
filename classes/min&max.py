list = [3, 5, 2]
min = list[0]
for i in list:
    if min > i:
        min = i
print('Min value is {}.'.format(min))
max = list[0]
for i in list:
    if max < i:
        max = i
print('Max value is {}.'.format(max))

sum = 0
for i in range(len(list)):
    sum += list[i]
print sum

prod = 1
i = 0
while i < len(list):
    prod *= list[i]
    i += 1
print prod