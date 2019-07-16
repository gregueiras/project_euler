def brute_squareSum(limit):
  total = 0

  for x in range(1, limit+1):
    total += x

  return total * total


def brute_sumSquare(limit):
  total = 0

  for x in range(1, limit+1):
    total += x * x

  return total

def brute(limit):
  return abs(brute_squareSum(limit) - brute_sumSquare(limit))

print(brute(100))