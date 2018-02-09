from math import sqrt, pow
a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))
if a==0:
     print("construction is impossible")
elif b==0:
    print("construction is impossible")
elif c==0:
    print("construction is impossible")
else:
      P=(a+b+c)
      S=sqrt(P*(P-a)*(P-b)*(P-c))
      print("P={},S={:.2f}".format(P,S))
