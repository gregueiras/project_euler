def isPalindrome(number):
  string = str(number)
  start = 0
  end = len(string) - 1

  while (start <= end):
    if (string[start] != string[end]):
      return False
    start += 1
    end -= 1

  return True

def compute():
    n1 = 999
    n2 = 999

    incN1 = True
    while not isPalindrome(n1 * n2):
      if incN1:
        n1 -= 1
      else:
        n2 -= 1

      if (abs(n1 - n2) > 100):
        incN1 = not incN1
        if n1 < n2:
          n1 += 100
        else:
          n2 += 100
    
    return [n1, n2, n1 * n2]


print(compute())