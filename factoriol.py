def factorial(n):
  if n == 0:
      return 1
  else:
      return n * factorial(n - 1)
  
def binomial(n, k):
  return factorial(n) / (factorial(k) * factorial(n - k))
  
def binomial_coefficients(n):
  for i in range(n + 1):
    print(binomial(n, i), end=' ')
  print()
  
binomial_coefficients(5)