# AC, Принята

r, g, b = map(int, input().split())
if abs(r - g) <= 25 and abs(r - b) <= 25 and abs(g - b) <= 25:
    result = "ALLOWED"
else:
    result = "FORBIDDEN"
print(result)
