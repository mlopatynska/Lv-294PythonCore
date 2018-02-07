a = int (raw_input ("Enter a \n"))
b = int (raw_input ("Enter b \n"))
c = int (raw_input ("Enter c \n"))
import math
if a < b + c and b < a + c and c < a + b:
    P = a + b + c
    S = int(math.ceil(math.sqrt (P * (P - a) * (P - b) * (P - c))))
    print "P = ", P, "S = ", S
else:
    print "it is impossible to build a triangle"
    