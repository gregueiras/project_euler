import math

def isPrime(n):
    if n <= 3:
        return n > 1
    elif n % 2 == 0 | n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 | n % (i + 2) == 0:
            return False
        i = i + 6

    return True


def isFactor(num, base):
    return num % base == 0


def highestPrimeFactor(num):
    for x in (range(num // 2 - 1, 1, -2)):
        print(x)
        if isFactor(num, x) & isPrime(x):
            return x

    return None

def smallestPrimeFactor(num):
    for x in (range(1, num // 2 - 1)):
        if isFactor(num, x) & isPrime(x):
            return x

    return num

def compute():
    n = 600851475143
    while True:
        p = smallestPrimeFactor(n)
        if (p < n):
            n //= p
        else:
            return n

print(compute())
