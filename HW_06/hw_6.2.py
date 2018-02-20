def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)

def f(i,j):
    var_f = factorial(i) * factorial(j)/float(factorial(i+j))
    return var_f

n = input("Enter number n:\n")
m = input("Enter number m:\n")

y = f (n,m)

print("Result = {}".format(y))