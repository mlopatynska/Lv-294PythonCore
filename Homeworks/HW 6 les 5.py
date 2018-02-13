a = raw_input(" Enter numbers")
a = str(a)
a = list(a)
min = a[0]
for el in a:
    if min > el:
        min = el
print min

