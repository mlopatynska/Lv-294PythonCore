number = input("enter number \n")
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print number, "not a prime number"
            break
    else:
        print number, "prime number"
else:
    print number, "not a prime number"