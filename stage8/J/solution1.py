# TL, Тест 5: превышение лимита времени

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def find_three_primes(c):
    for i in range(2, c):
        if is_prime(i):
            for j in range(2, c-i):
                if is_prime(j) and is_prime(c-i-j):
                    print("{}={}+{}+{}".format(c, i, j, c-i-j))
                    return
    print("Для числа {} гипотеза Гольдбаха неверна".format(c))

while (c := int(input())) != 0:
    find_three_primes(c)
