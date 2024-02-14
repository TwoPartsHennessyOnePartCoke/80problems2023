# AC, Принята

N, K = map(int, input().split())
count=0
while N>K:
    N-=K
    count+=1
print(count)