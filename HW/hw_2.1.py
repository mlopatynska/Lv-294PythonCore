from math import cos, sin, tan, atan, sqrt, factorial, log1p, fabs, pi, e

        #Input x,y,z.
print ("Please, enter x , y , z:")
x = float(input("x = "))
y = float(input("y = "))
z = float(input("z = "))

#In all this task, use the same structur of creating variables.
#x_y - where x - task variables , y - task name.

        #Task - a
a_a = (sqrt(fabs(x-1)) - pow(fabs(y), 1/3.0)) / (1 + pow(x,2)/2 + pow(y,2)/2)
b_a = x * (atan(z) + pow(e, -(x+3)))

        #Task - b
a_b = (3 + pow(e, y-1))/(1 + pow(x,2) * fabs(y-tan(z)))
b_b = 1 + fabs(y-x) + pow(y-x, 2)/2 + fabs(pow(y-x, 3))/3

        #Task - c
a_c = (1+y) * (x+y/(pow(x,2)+4)) / (pow(e,-x-2) + 1/(pow(x,2)+4))
b_c = (1 + cos(y-2))/(pow(x,4)/2 + ((1 - cos(2*z))/2))

        #Task - d
a_d = y + x/((pow(y,2) + fabs(pow(x,2)/(y + pow(x,3)/3))))
b_d = 1 + (1-cos(z))/(1+cos(z))

        #Task - e
a_e = (2*cos(x - pi/6)) / (1/2 + (1-cos(2*y))/2)
b_e = 1 + (pow(z,2))/(3 + pow(z,2)/5)

        #Task - f
a_f = (1 + (1-cos(2*(x+y))/2)) / (2 + fabs(x - (2*x)/(1 + pow(x,2)*pow(y,2))))
b_f = (1 + cos(2 * (atan(1/z)))) / 2

        #Task - g
a_g = fabs((y - sqrt(fabs(x)) * (x - y/(z + pow(x,2)/4))))
b_g = x - pow(x,2)/factorial(3) + pow(x,5)/factorial(5)


#Output all variables!
print("\n\tAnswer of task A:\na = {:8f}\nb = {:8f}\n\n \
       Answer of task B:\na = {:8f}\nb = {:8f}\n\n \
       Answer of task C:\na = {:8f}\nb = {:8f}\n\n \
       Answer of task D:\na = {:8f}\nb = {:8f}\n\n \
       Answer of task E:\na = {:8f}\nb = {:8f}\n\n \
       Answer of task F:\na = {:8f}\nb = {:8f}\n\n \
       Answer of task G:\na = {:8f}\nb = {:8f}\n\n \
          ".format(a_b, b_a, a_b,
                   b_b, a_c, b_c,
                   a_d, b_d, a_e,
                   b_e, a_f, b_f,
                   a_g, b_g))







