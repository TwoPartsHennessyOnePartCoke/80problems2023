# WA, Тест 5: неверный ответ	

A, D, H = map(int, input().split())

D = D - 0.001

N = D // A

numbers = 0
if N % 2 == 1:
    if (1+(A*N)**2)**0.5>D:
        print("---")
    numbers += N
    N -= 1
    while N > 0:
        numbers += N * 2
        N -= 2
else:
    if (2**2+(A*N)**2)**0.5>D:
        print("---")
    while N > 0:
        numbers += N * 2
        N -= 2

numbers *= H // A
print(int(numbers))
