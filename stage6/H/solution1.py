# WA, Тест 7: неверный ответ

p1 = list(map(int, input().split()))[1:]
p2 = list(map(int, input().split()))[1:]

q = []
while len(p1) >= len(p2):
    if p1[0] == 0:
        p1.pop(0)
        q.append(0.0)
        continue
    lc = p1[0] / p2[0]
    q.append(lc)
    p2t = [c * lc for c in p2] + [0] * (len(p1) - len(p2))
    p1 = [c1 - c2 for c1, c2 in zip(p1, p2t)]
    p1.pop(0)

if sum(p1) or q == []:
    print("ABS")
elif not all(num.is_integer() for num in q):
    print("REL")
else:
    print(len(q) - 1, *[int(i) for i in q], sep=' ')
