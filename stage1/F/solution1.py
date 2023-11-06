# AC, Принята

n = int(input())

count = 0
while n != 1:
    if n % 2 == 0:
        count += n // 2
        n //= 2
        continue
    else:
        count += 1
        n -= 1

print(count)
