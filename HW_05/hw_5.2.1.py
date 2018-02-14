from random import randint

num = [randint(0,100) for i in xrange(10)]
print(num)


#for - elemm
def for_elem(num):
    min = num[0]
    for i in num:
        if min > i:
            min = i
    print("Min element (for - element) = {}\n".format(min))

#for - index
def for_index(num):
    min = num[0]
    for i in range(1,len(num)):
        if min > num[i]:
            min = num[i]
    print("Min element (for - index) = {}\n".format(min))

#while


def while_index(num):
    min = num[0]
    i = 1
    while i < len(num):
        if min > num[i]:
            min = num[i]
        i += 1
    print("Min element (while) = {}\n".format(min))


for_elem(num)
for_index(num)
while_index(num)