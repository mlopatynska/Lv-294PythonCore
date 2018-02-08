from math import sqrt
print("Input 3 hights.")
a = input("a= ")
b = input("b= ")
c = input("c= ")
if c <= a + b and b <= a + c and a <= b + c:
    P = a + b + c
    print("P = {}".format(P))
    P /= 2
    S = sqrt(P * (P - a) * (P - b) * (P - c))
    print("S = {}".format(S))
else:
    print("'a,b,c' not a triangle side")