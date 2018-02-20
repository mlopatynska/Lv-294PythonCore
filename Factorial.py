def factorial(x):
    f = 1
    for j in range(1, x + 1):
        f = f * j
    return (f)

n = int(input("n="))
m = int(input("m="))
tot = 0
tot = (factorial(n) * factorial(m)) / factorial(n + m)
print(tot)
