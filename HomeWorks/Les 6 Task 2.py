n = int(input("Enter number \n"))
m = int(input("Enter number \n"))
def func(x):
    import math
    math.factorial(x)
    return x
f = func(n) * func(m) / float(func(n + m))
print ("F (n,m) = {}".format(f))