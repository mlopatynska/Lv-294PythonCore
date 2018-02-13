def fib(n):
    res=[1,2]
    a,b=1,2
    for x in range(2,n):
        a,b=b,a+b
        res.append(b)
    return res
print(fib (10))