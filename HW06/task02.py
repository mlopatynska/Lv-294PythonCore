n = input('Enter n value:\n')
m = input('Enter m value:\n')
 
def fucktorial(x):
  prod = 1
  for i in range (1,x+1):
    prod *= i
  return prod
 
result = fucktorial(n) * fucktorial(m) / fucktorial(n+m)
print('F(m,n) = {:.10f}'.format(result))
