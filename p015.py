import math

def binomialCoefficient(x, y):
  n = x + y
  k = x
  return int(math.factorial(n) / (math.factorial(k)*math.factorial(n - k)))

print(binomialCoefficient(20, 20))