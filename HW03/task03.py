print("Please enter the values for each a,b,c in ax^2 + bx + c = 0:\n")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

discr = b ** 2 - 4 * a * c;
if discr > 0:
    x1 = (-b + discr ** 0.5) / (2 * a)
    x2 = (-b - discr ** 0.5) / (2 * a)
    print("x1 = {:.2f} \nx2 = {:.2f}".format(x1, x2))
elif discr == 0:
    x = -b / (2 * a)
    print("x = {:.2f}".format(x))
else:
    print("There are no solutions")
