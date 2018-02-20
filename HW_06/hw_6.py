from random import randint


def my_sum(x):
    summ = 0
    for i in x:
        summ +=i
    return summ


def my_avg(x):
    avg = my_sum(x)
    avg /= len(x)
    return avg


def my_min(x):
    min = x[0]
    for i in x:
        if min > i:
            min = i
    return min


def my_max(x):
    max = x[0]
    for i in x:
        if max < i:
            max = i
    return max


def my_revers(x):
    x = x[::-1]
    return x


x = [randint(0,100) for i in xrange(10)]
print("Mass x: \n{}".format(x))



