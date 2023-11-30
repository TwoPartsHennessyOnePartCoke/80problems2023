# AC, Принята

n, s = map(int, input().split())
a = list(map(int, input().split()))

thing = {0: []}

for i in a:
    thing_copy = thing.copy()
    for j in thing_copy:
        if j + i not in thing:
            thing[j + i] = thing[j] + [i]

print(*thing[s])
