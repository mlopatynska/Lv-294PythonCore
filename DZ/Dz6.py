a = [45, 17, 28, 34, 100]
i = 0
nmin = i
min = a[nmin]
nmax = i
max = a[nmax]
while (i < len(a)):
    if (a[i] < min):
        nmin = i
        min = a[nmin]
    if (a[i] > max):
        nmax = i
        max = a[nmax]
    i += 1
print "min = a[", nmin, "] = ", min
print "max = a[", nmax, "] = ", max