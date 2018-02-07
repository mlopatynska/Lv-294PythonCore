# example a

x = int(raw_input("Enter Value x \n"))
y = int(raw_input("Enter Value y \n"))
z = int(raw_input("Enter Value z \n"))

import math
a = (math.sqrt(math.fabs(x-1)) - math.sqrt(math.sqrt(math.fabs(y)))) / (1 + ((x*x)/2) + ((y*y)/4))
b = x * (math.atan(z) - math.exp (-(x+3)))
print a, b


