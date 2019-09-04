def nextCollatz(n):
  if (n % 2 == 0):
    return int(n/2)
  else:
    return int(3 * n + 1)

def collatzSize(n):
  collatzNumber = n
  size = 1

  while(collatzNumber != 1):
    collatzNumber = nextCollatz(collatzNumber)
    size += 1

  return size

def iter():
  maxSize = 0
  startingNumber = 1

  for n in range(1, 1000000):
    newSize = collatzSize(n)
    if (newSize > maxSize):
      maxSize = newSize
      startingNumber = n

  print(f'N: {startingNumber}\tS: {maxSize}')



iter()