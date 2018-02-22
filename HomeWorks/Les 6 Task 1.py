from random import randint
x = randint(1,1000)
y = randint(1,1000)
z = randint(1,1000)
a = [x for x in range(1,62,2)]
b = [i for i in xrange(2,63,2)]
c = [i for i in xrange(31)]

def event(f,g):
    k = 0
    eg = len(f)
    for i in range(eg):
        k = f[i] * pow(g,eg - i)
    return k

rezult = pow(event(a,x),2) - (event(b,y)) / event(c,(x+z))

print("a ={}\n b = {}\n c = {}\n x = {}\n y = {}\n z = {} \n Rezult = {}".format(a, b, c, x, y, z, rezult))
