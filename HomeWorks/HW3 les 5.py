a = int(raw_input("enter number \n"))
fib = [0, 1]
i = 1
while i < a:
    fib.append(fib[i] + fib[i-1])
    print fib
    i += 1