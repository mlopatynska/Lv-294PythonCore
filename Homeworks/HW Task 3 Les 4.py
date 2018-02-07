a = int (raw_input ("Enter a \n"))
b = int (raw_input ("Enter b \n"))
c = int (raw_input ("Enter c \n"))

import math
D = math.pow(b,2) - 4*a*c
if D > 0:
    x1 = (-b + math.sqrt(D))/(2*a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print ("The equel has two roots:", x1, x2)
elif D == 0:
    x1= - (b/(2*a))
    print ("The equel has one root:", x1)
else:
    print ("The equel has not roots")
