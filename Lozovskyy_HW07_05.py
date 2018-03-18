def mysort(x):
    for a in range (len(x)-1):
        for i in range (len(x)-1):
            if x[i]>x[i+1]:
                x[i],x[i+1]=x[i+1],x[i]
            # print x
    return x

a = [10,9,8,7,6,5,4,3,2,1,0]

print "input data: {}".format(a)

y = mysort(a)
print "result of bubble sort: {}".format(y)

