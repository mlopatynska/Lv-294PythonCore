from random import randint

def min_elem(mas):
    minn = mas[0][0]
    x = 0
    y = 0
    for i in xrange(len(mas)):
        for j in xrange(len(mas[i])):
            if minn > mas[i][j]:
                minn = mas[i][j]
                x = i
                y = j
    return x, y

def swap_min_elem(mas1,x_mas1,y_mas1,mas2,x_mas2,y_mas2):
    mas1[x_mas1][y_mas1],mas2[x_mas2][y_mas2] = mas2[x_mas2][y_mas2],mas1[x_mas1][y_mas1]
    return mas1, mas2

a = [[randint(10,150) for a_j in xrange(5)] for a_i in range(5)]
b = [[randint(10,150) for b_j in xrange(5)] for b_i in range(5)]
print('Mas A:\n{}\nMas B:\n{}'.format(a,b))


x_min_a, y_min_a = min_elem(a)
x_min_b, y_min_b = min_elem(b)


print("Min elem in A = {}\nx = {}\ty = {}".format(a[x_min_a][y_min_a],x_min_a,y_min_a))
print("Min elem in B = {}\nx = {}\ty = {}".format(b[x_min_b][y_min_b],x_min_b,y_min_b))

a, b = swap_min_elem(a,x_min_a,y_min_a,b,x_min_b,y_min_b)
print("Swap!\n'Mas A:\n{}\nMas B:\n{}".format(a,b))