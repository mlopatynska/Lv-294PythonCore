import math
#HW 07_02 fin production of two factorials with selfmade factorial's function

def factorial(x):
    res=1
    for i in range (1,x+1,1):
        res *= i
    else:
        return res
F = 1.00000
n = int(input("Enter number 1:\n"))
m = int(input("Enter number 2:\n"))


# F = x*y/z
F = (factorial(n)*factorial(m))+factorial(n+m)
print "n! is {}, m! is {}, (n+m)! is: {}".format\
    (factorial(n),factorial(m),factorial(n+m))
print "Result of function n!*m!/(n+m)! is: {0:.5f}".format(F)