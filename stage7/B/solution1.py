# WA, Тест 2: неверный ответ

st = input()

def to_base7(n):
    convertString = "0123456"
    if n < 7:
        return convertString[n]
    else:
        return to_base7(n//7) + convertString[n%7]

def check_solved(st):
    return st in ['WWWWBBBB', 'BBBBWWWW' 'WBWBWBWB', 'BWBWBWBW', 'WWBBWWBB', 'BBWWBBWW'] 

def rotate(st, action):
    if action == 0:
        return st
    if action == 1:
        return st[1] + st[3] + st[0] + st[2] + st[5] + st[7] + st[4] + st[6]
    elif action == 2:
        return st[2] + st[0] + st[3] + st[1] + st[6] + st[4] + st[7] + st[5]
    elif action == 3:
        return st[4] + st[1] + st[0] + st[3] + st[6] + st[5] + st[2] + st[7]
    elif action == 4:
        return st[2] + st[1] + st[6] + st[3] + st[0] + st[5] + st[4] + st[7]
    elif action == 5:
        return st[0] + st[5] + st[2] + st[1] + st[4] + st[7] + st[6] + st[3]
    elif action == 6:
        return st[0] + st[3] + st[2] + st[7] + st[4] + st[1] + st[6] + st[5]

def solve(st):
    for i in range(0, 7**7):
        comb = to_base7(i).zfill(7)
        temp_st = st
        for action in comb:
            temp_st = rotate(temp_st, int(action))
            if check_solved(temp_st):
                return comb
    return -1

act = str(solve(st)).replace('0', '')
print(len(act))
for i in act:
    match i:
        case '1':
            print('CW')
        case '2':
            print('CCW')
        case '3':
            print('LU')
        case '4':
            print('LD')
        case '5':
            print('RU')
        case '6':
            print('RD')
