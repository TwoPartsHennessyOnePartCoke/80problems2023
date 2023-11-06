# TL, Тест 77: превышение лимита времени

from sys import setrecursionlimit
setrecursionlimit(1000000) # да, это плохо

n, k = map(int, input().split())


def l(n):
    if n == 1:
        return 1
    return len(str(n)) + 2 * l(n - 1)


def dig(n, k):
    if k > l(n):
        return -1
    elif k <= len(str(n)):
        return int(str(n)[k - 1])
    elif k > l(n - 1) + len(str(n)):
        return dig(n - 1, k - l(n - 1) - len(str(n)))
    else:
        return dig(n - 1, k - len(str(n)))


print(dig(n, k))
