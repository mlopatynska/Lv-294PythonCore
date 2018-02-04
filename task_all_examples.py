x= int(raw_input("Enter x "))
y= int(raw_input("Enter y "))
z= int(raw_input("Enter z "))

import math

a= (3+math.exp(y-1))/(1+(x*x)*math.fabs(y-math.tan(z)))

print a

b= 1+math.fabs(y-x)+ ((y-x)*(y-x))/2+math.pow(math.fabs(y-x),3)/3

print b

a=(1+y)*(((x+y)/(x*x+4))/((math.exp(-x-2))+1/(x*x+4)))

print a

b=(1+math.cos(y-2))/((math.pow(x,4)/2)+math.pow(math.sin(z),2))

print b

a=y+(x/(math.pow(y,2)+math.fabs(math.pow(x,2)/(y+(math.pow(x,3)/3)))))

print a

b=1+math.pow(z,2)/(3+math.pow(z,2)/5)

print b

a= (2*math.cos(x-math.pi/6))/(1/2+math.pow(math.sin(y),2))

print a

b=(1+math.pow(math.tan(z/2),2))

print b

a=(1+math.pow(math.sin(x+y),2))/(2+math.fabs((x-2*x)/(1+math.pow(x,2)*math.pow(y,2))))+x

print a

b=math.pow(math.cos(math.atan(1/z)),2)

print b

