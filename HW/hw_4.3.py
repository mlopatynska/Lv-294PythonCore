                     #Task #3
a = input("Input a = ")
b = input("Input b = ")
c = input("Input c = ")

D =  pow(b,2) - 4*a*c #Discriminator

if not D:
       x = (-b) / 2*a
       print("X = {}".format(x))
else:
       print("D not 0!")
