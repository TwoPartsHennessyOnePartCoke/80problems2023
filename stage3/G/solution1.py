# AC, Принята

from math import floor, ceil

p, q = map(int, input().split())

def continued_fraction(p, q):
    while q != 0:
        yield p // q
        p, q = q, p % q

shit = list(continued_fraction(p, q))
shit[-1] -= 1
shit.append(1)

def get_reverse_lengths(cf):
    prev = 0
    for i in cf[::-1]:
        cur = len(str(i))
        yield prev + cur
        prev = prev + cur + 3

lengths = list(get_reverse_lengths(shit))[::-1]
lengths.append(0)

prev = 0
for i, j, k in zip(lengths, lengths[1:], shit):
    dif = i - j
    h = (j - 1) / 2
    l, r = floor(h), ceil(h)
    print('.' * (prev + dif + l) + '1' + '.' * r)
    if j == 0:
        break
    print('.' * prev + str(k) + '.+.' + '-' * j)
    prev += dif
