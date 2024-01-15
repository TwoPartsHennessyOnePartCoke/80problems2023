# TL, Тест 7: превышение лимита времени

def sieve_thing(n):
    primes = [True for _ in range(n+1)]
    p = 2
    while (p * p <= n):
        if (primes[p] == True):
            for i in range(p * p, n+1, p):
                primes[i] = False
        p += 1
    prime_numbers = [p for p in range(2, n) if primes[p]]
    return prime_numbers

def find_three_primes(c, primes):
    for i in reversed(primes):
        if i > c:
            continue
        for j in primes:
            if j > c - i:
                break
            if c - i - j in primes:
                print("{}={}+{}+{}".format(c, i, j, c-i-j))
                return
    print("Для числа {} гипотеза Гольдбаха неверна".format(c))

primes = list(sieve_thing(1000000))

while (c := int(input())) != 0:
    find_three_primes(c, primes)
