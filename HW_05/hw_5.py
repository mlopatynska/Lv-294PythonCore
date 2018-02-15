from random import randint

def min_max():
    d = {'min': min(randint(10,250) for i in xrange(10)),
         'max': max(randint(10,250) for i in xrange(10))}
    print(d)


#min_max()

length_edge = input('Enter length of the lower edge:\n')

def isosceles(n):
    for i in range(1,n + 1,2):
         x = (n-i)/2
         print('{0}{1}{0}'.format(' '*x,'*'*i))

def rectangular(n):
    for i in range(1,n+1):
        print('*' * i)

if length_edge % 2:
    isosceles(length_edge)
else:
    rectangular(length_edge)