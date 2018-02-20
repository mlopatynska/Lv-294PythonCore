from random import randint


def my_multiplication(mas,var):
    summ = 0
    length = len(mas)
    for i in range(length):
        summ = mas[i] * pow(var,length - i)
    return summ


a = [i for i in xrange(1,62,2)]
b = [i for i in xrange(2,63,2)]
c = [i for i in xrange(31)]
x = randint(1,100)
y = randint(1,100)
z = randint(1,100)

ans = pow(my_multiplication(a,x),2) - (my_multiplication(b,y)) / \
      my_multiplication(c,(x+z))

print("a:\n{}\nb:\n{}\nc:\n{}\nx = {}\ny = {}\nz = {}".format(a, b, c, x, y, z))
print("Ansver = {}".format(ans))