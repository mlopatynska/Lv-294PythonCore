                     # Task #4
from math import sqrt

print("Input 3 random numbers.")
a = input("a =\n")
b = input("b =\n")
c = input("c =\n")


if c <= a + b and b <= a + c and a <= b + c:
    P = a + b + c
    print("P = {}".format(P))
    P /= 2
    S = sqrt(P * (P - a) * (P - b) * (P - c))
    print("S = {}".format(S))
else:
    print("'a' , 'b' and 'c' not a triangle side")