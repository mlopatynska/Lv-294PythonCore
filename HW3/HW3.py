from math import sqrt, pow
a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))
if a==0:
    print("a can not be equal to zero")
elif b==0:
    print("this is incomplete square equation")
elif c==0:
    print("this is incomplete square equation")
else:
    x=(-b+sqrt(b**2)-4*a*c)/2*a
    print ("x1={},x2={}".format(x,-x))


