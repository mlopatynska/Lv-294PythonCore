# Fibonacci numbers
fib1 = 1
fib2 = 1

k = input("Input N:\n")
k = int(k)
print("Fibonacci numbers:\n")
if k ==1:
    print("1")
elif k ==2:
    print("1\n1")
else:
    i = 2
    print("1\n1")
    while i < k:
        fib = fib1 + fib2
        fib1 = fib2
        fib2 = fib
        print (fib)
        i += 1
