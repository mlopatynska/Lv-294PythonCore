                     #Task #3
from math import sqrt

a = input("Input a = ")
b = input("Input b = ")
c = input("Input c = ")

D = pow(b,2) - 4*a*c #Discriminator

if not D:
    x = (-b) / 2*a
    print("X = {}".format(x))
elif D > 0:
    x1 = (-b + sqrt(D)) / 2 * a
    x2 = (-b - sqrt(D)) / 2 * a
    print("X1 = {}\nX2 = {}".format(x1,x2))
else:
    print("There are no real roots.")
