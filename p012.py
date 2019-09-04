import math

def triangular(n):
  return int(n*(n+1)/2)

def divisors(n):
  limit = int(math.ceil(math.sqrt(n)))
  divisors = 0

  for i in range(1, limit):
    if (n % i == 0):
      divisors += 1
      if (i != n/i):
        divisors += 1

  #print(f'N: {n}\tD: {divisors}')
  return divisors

def iter():
  maxDivisors = 0
  n = 1

  while(maxDivisors < 500):
    maxDivisors = divisors(triangular(n))
    n += 1

  print(f'N: {triangular(n - 1)}\tD: {maxDivisors}')
  
iter()
