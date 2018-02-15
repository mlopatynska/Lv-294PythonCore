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

def all_amstrong_number():
    n = input("Enter the search boundary:")
    for i in xrange(0, n):
        i = str(i)
        x = len(i)
        z = 0
        for j in i:
            z += pow(int(j),x)
        if int(i) == z:
            print(z)

def amstrong_number():
    n = input("Enter the number for check:")
    x = str(n)
    summ_n = 0
    for i in x:
        summ_n += pow(int(i),len(x))
    if n == summ_n:
        print("It's Amstrong number!")
    else:
        print("Not Amstrong number!")

#all_amstrong_number()
#amstrong_number()
