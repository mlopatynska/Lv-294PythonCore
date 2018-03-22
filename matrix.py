from random import randint

def max_elem(mas):
    maxx = mas[0][0]
    x = 0
    y = 0
    for i in range(len(mas)):
        for j in range(len(mas[i])):
            if maxx < mas[i][j]:
                maxx = mas[i][j]
                x = i
                y = j
    return x, y

def matrx_max_elem(mas1,x_mas1,y_mas1,mas2,x_mas2,y_mas2):
    mas1[x_mas1][y_mas1],mas2[x_mas2][y_mas2] = mas2[x_mas2][y_mas2],mas1[x_mas1][y_mas1]
    return mas1, mas2

M1 = [[randint(10,150) for M1_j in range(5)] for M1_i in range(5)]
M2 = [[randint(10,150) for M2_j in range(5)] for M2_i in range(5)]
print('Mas Matrix1:\n{}\nMas Matrix2:\n{}'.format(M1,M2))


x_max_M1, y_max_M1 = max_elem(M1)
x_max_M2, y_max_M2 = max_elem(M2)


print("Max elem in Matrix1 = {}\nx = {}\ty = {}".format(M1[x_max_M1][y_max_M1],x_max_M1,y_max_M1))
print("Max elem in Matrix2 = {}\nx = {}\ty = {}".format(M2[x_max_M2][y_max_M2],x_max_M2,y_max_M2))

M1, M2 = matrx_max_elem(M1,x_max_M1,y_max_M1,M2,x_max_M2,y_max_M2)
print("Matrix1:\n{}\nMatrix2:\n{}".format(M1,M2))