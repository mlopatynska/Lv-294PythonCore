from random import randint


def bubble_sort(mas):
    length = len(mas) - 1
    while length >= 0:
        for i in range(length):
            if mas[i] > mas[i +1]:
                mas[i],mas[i+1] = mas[i+1],mas[i]
        length -= 1
    return mas


x = [randint(0,250) for x_i in xrange(5)]
print("Mas before sort.\n{}".format(x))

x = bubble_sort(x)
print("Mas before sort.\n{}".format(x))