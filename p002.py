def isEven(num):
  return num % 2 == 0

def nextFibonacci(prev1, prev2):
  return prev1 + prev2

def compute(upperLimit):
  total = 0
  prevN = 1
  nextN = 2

  while (nextN < upperLimit):
    if isEven(nextN):
      total += nextN
    
    temp = nextFibonacci(prevN, nextN)
    prevN = nextN
    nextN = temp

  return total


print(compute(4e6))

