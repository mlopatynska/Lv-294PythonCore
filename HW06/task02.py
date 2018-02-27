n = input('Enter n value:\n')
m = input('Enter m value:\n')
 
def factorial(x):
  prod = 1
  for i in range (1,x+1):
    prod *= i
  return prod
 
result = factorial(n) * factorial(m) / float(factorial(n+m))
print('F(m,n) = {:.10f}'.format(result))
