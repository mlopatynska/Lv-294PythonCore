#Real numbers will be counted with step 1, only first number is requested.
a = input('Enter your a0 number:\n')
b = input('Enter your b0 number:\n')
c = input('Enter your c0 number:\n')
x = input('Enter x number:\n')
y = input('Enter y number:\n')
z = input('Enter z number:\n')

def sumproduct (abc,xyz):
    sum = 0
    i = 30
    for q in range (0,30):
        i = i - q
        abc = abc + q
        sum += abc * (xyz ** i)
    return sum

result = ((sumproduct(a,x) ** 2) - sumproduct(b,y)) / sumproduct (c,(x + z))
print('Your result for that crazy calculations will be following: {}'.format(result))
