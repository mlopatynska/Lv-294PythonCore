# Prime number
x = input("Input number\n")

if x == 1:
    print("Not prime")
else:
    i = 2
    while i*i <= x:
        if x == 1:
            print("Not prime")
            break
        if not x % i:
            print(i)
            print("Not prime")
            break
        i+=1
    else:
        print("Yes, is prime!")
