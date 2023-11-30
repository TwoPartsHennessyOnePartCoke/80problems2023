# AC, Принята

from math import floor, ceil

align = list(input())

top = list(input().split('&'))
max_len = [len(i) for i in top]

rows = []

while True:
    row = list(input().split('&'))
    if '*' in row:
        break
    max_len = [max(max_len[i], len(row[i])) for i in range(len(row))]
    rows.append(row)

def print_aligned_cell(text: str, align, length):
    if align == '<':
        print(text + ' ' * (length - len(text)), end=' ')
    elif align == '>':
        print(' ' * (length - len(text)) + text, end=' ')
    elif align == '=':
        print(' ' * floor((length - len(text)) / 2) + text + ' ' * ceil((length - len(text)) / 2), end=' ')

tb = '@' + (sum(max_len) + len(max_len) * 3 - 1) * '-' + '@'

print(tb)

for i in range(len(top)):
    print('| ', end='')
    print_aligned_cell(top[i], align[i], max_len[i])
print('|')

print('|', end='')
print(*['-' * (i + 2) for i in max_len], sep='+', end='|\n')

for row in rows:
    for i in range(len(row)):
        print('| ', end='')
        print_aligned_cell(row[i], align[i], max_len[i])
    print('|')

print(tb)
