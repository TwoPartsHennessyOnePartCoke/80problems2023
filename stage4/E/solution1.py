# AC, Принята

x, k = map(int, input().split())

i = -1
while x < 10**9: # с логарифмами был неправильный ответ :(
    x *= k
    i += 1

print(i)
