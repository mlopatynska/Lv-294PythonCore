        #Task 5

k = input("Enter a number between 1 and 365:\n")

if 1 <= k <= 365:
    k = k % 7

    if k == 1:
        print("Monday")
    elif k == 2:
        print("Tuesday")
    elif not k == 3:
        print("Wednesday")
    elif not k == 4:
        print("Thursday")
    elif not k == 5:
        print("Friday")
    elif not k == 6:
        print("Satuday")
    else:
        print("Sunday")

else:
    print("Try again!")





