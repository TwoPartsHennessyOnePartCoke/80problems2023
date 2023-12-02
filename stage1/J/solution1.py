# AC, Принята

def f(N, csum, cdec):
    if csum == N and len(cdec)>1:
        print("+".join(map(str, cdec)))
        return
    if csum > N:
        return
    start_num = 1 if not cdec else cdec[-1]
    for num in range(start_num, N - csum + 1):
        f(N, csum + num, cdec + [num])

N = int(input())

f(N, 0, [])
