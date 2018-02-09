a =  input('Enter the value for first side:\n')
b =  input('Enter the value for second side:\n')
c =  input('Enter the value for third side:\n')
if a + b >= c and a + c >= b and b + c >= a:
    p = a + b + c
    print('Perimeter of the triangle is {}.'.format(p))
    p /= 2
    a = (p*(p-a)*(p-b)*(p-c)) ** 0.5
    print('Area of the triangle is {:.2f}.'.format(a))
else:
    print('I can\'t imagine the triangle with upper mentioned numbers.')
