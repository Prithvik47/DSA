def maxDivide(x, k):
    while x % k == 0:
        x = x // k
    return x


def isUgly(n):
    n = maxDivide(n, 2)
    n = maxDivide(n, 3)
    n = maxDivide(n, 5)
    if n == 1:
        return True
    else:
        return False


def getUgly(a):
    count = 1
    i = 1
    while count < a:
        i += 1
        if isUgly(i):
            count += 1
    return i