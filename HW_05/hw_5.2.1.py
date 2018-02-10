from random import randint

num = []
for i in range(8):
    num.append(randint(0,100))

print(num)

#for - elemm
min = num[0]
for i in num:
    if min > i:
        min = i

print("Min element (for - element) = {}\n".format(min))

#for - index
min = num[0]
for i in range(1,len(num)):
    if min > num[i]:
        min = num[i]

print("Min element (for - index) = {}\n".format(min))

#while
min = num[0]
i = 1
while i < len(num):
    if min > num[i]:
        min = num[i]
    i += 1

print("Min element (while) = {}\n".format(min))


