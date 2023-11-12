# TL, Тест 7: превышение лимита времени

from math import sqrt, ceil

a, b = map(int, input().split())

squares = [i ** 2 for i in range(2, ceil(sqrt(b)) + 1)]

def is_multiple_of_perfect_square(n):
    for square in squares:
        if square > n:
            break
        if n % square == 0:
            return True
    return False

simples = 0
for i in range(a, b + 1):
    if not is_multiple_of_perfect_square(i):
        simples += 1

print(simples)
