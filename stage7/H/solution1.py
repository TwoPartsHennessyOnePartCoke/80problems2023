# RT, Тест 2: ошибка времени исполнения

from sys import setrecursionlimit
setrecursionlimit(1000000)

n, k = map(int, input().split())
selected = list(map(int, input().split()))
seq = ''.join(map(str, selected))
available = [str(i) for i in range(1, n+1) if i not in selected]

def rec(seq, available, current):
    if seq == '':
        return current
    for i in range(len(str(n-1)), 0, -1):
        if seq[-i:] in available:
            available.remove(seq[-i:])
            temp = rec(seq[:-i], available, current + [seq[-i:]])
            if temp:
                return temp
        else:
            break
    else:
        return '-1'

answ = rec(seq, available, [])[::-1]
print(len(answ))
print(*answ, sep=' ')
