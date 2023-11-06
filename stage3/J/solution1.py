# TL, Тест 4: превышение лимита времени

def same(k):
    ks = str(k)
    for i in range(len(ks) - 1):
        if ks[i] == ks[i + 1]:
            return False
    return True


def req(k, s):
    st = list(set(str(k)))
    for j in st:
        if j not in s:
            return False
    return True


s = input()
k = int(input())

if s == '0':
    print(-1)
else:
    while True:
        if same(k) and req(k, s):
            print(k)
            break
        k += 1
