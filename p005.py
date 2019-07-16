# doesn't scale very well, takes too long for upper = 20


def isEvenDisible(num, base):
    return num % base == 0


def compute(lower, upper):
    i = 1
    completed = False
    while not completed:
        found = True
        for x in range(lower, upper + 1):
            if not isEvenDisible(i, x):
                found = False

        completed |= found
        i += 20

    return i - 1


def gcd(a, b):
    if (b == 0):
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    return (a*b)/gcd(a, b)

def findLCM(lower, upper):
    temp = lower
    for x in range(lower, upper):
        temp = lcm(temp, x)

    return round(temp)

print(findLCM(1, 20))