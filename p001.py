def isMul(number, base):
  return number % base == 0

def mySum(start, end, listMultiples):
  total = 0
  for num in range(start, end):
    isMult = False
    for mult in listMultiples:
      if isMul(num, mult):
        isMult = True
    if (isMult):
      total += num

  return total

print(mySum(1, 1000, [3, 5]))