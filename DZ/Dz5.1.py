n = input("n= ")
lst = []
k = 0
for i in xrange(2, n+1):
    for j in xrange(2, i):
       if i % j == 0:
            k = k + 1
    if k == 0:
        lst.append(i)
    else:
        k = 0
print lst