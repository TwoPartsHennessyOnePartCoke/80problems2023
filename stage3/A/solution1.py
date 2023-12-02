# AC, Принята

def find_numbers(s, p):
    for a in range(1001):
        b = s - a
        if a * b == p:
            return a, b
s, p = map(int, input().split())
result = find_numbers(s, p)
print(*sorted(result))
