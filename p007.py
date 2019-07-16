def isPrime(n):
    """Returns True if n is prime."""
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0 or n == 1:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True

def compute(limit):
  found = 0
  lastFound = 0
  i = 0

  while found < limit:
    i += 1
    if isPrime(i):
      lastFound = i
      found += 1
  

  return lastFound


print(compute(10001))
