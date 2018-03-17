from random import randint
def my_vector(mas,var):
    sum = 0
    length = len(mas)
    for j in range(length):
        sum = mas[j] * pow(var,length - j)
    return sum


a = [j for j in range(1,62,2)]
b = [j for j in range(2,63,2)]
c = [j for j in range(31)]
x = randint(1,100)
y = randint(1,100)
z = randint(1,100)

result = pow(my_vector(a,x),2) - (my_vector(b,y)) / \
         my_vector(c,(x+z))

print("a:\n{}\nb:\n{}\nc:\n{}\nx = {}\ny = {}\nz = {}".format(a, b, c, x, y, z))
x=(round(result,2))
print('Result={}'.format(x))
