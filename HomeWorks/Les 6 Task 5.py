x = raw_input("enter number")
x = list (x)
def sort(el):
    p = len(el) - 1
    while p >= 0:
        for i in range(p):
            if el[i] > el[i +1]:
                el[i],el[i+1] = el[i+1],el[i]
        p -= 1
    return el

x = sort(x)

print("Sorted list from min to max\n{}".format(x))