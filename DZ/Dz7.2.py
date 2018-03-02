data = range(100,10000,7)
hash = {'min':data[-1], 'max':data[0], 'avg':(sum(data)/len(data))}
x = 100000
for i in data:
    if hash['min']>i:
        hash['min']=i
    elif hash['max']<i:
        hash['max']=i
print 'Hash info: {}'.format(hash)
print 'Minimum value is: {}\nMaximum value is: {}\nAverage value is: {}'\
    .format(hash['min'],hash['max'],hash['avg'])