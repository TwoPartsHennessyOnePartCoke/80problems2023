# AC, Принята

L, K = map(int, input().split())
count = 0

while L > 1:
    L = (L + K - 1) // K  # Деление с округлением вверх
    if L>1:
        count += 1

print(count)
