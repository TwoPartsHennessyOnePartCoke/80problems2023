# AC, Принята

sym_count = {
'A': 0, 'a': 0, '0': 0,
 'B': 0, 'b': 0, '1': 0,
 'C': 0, 'c': 0, '2': 0,
 'D': 0, 'd': 0, '3': 0,
 'E': 0, 'e': 0, '4': 0,
 'F': 0, 'f': 0, '5': 0,
 'G': 0, 'g': 0, '6': 0,
 'H': 0, 'h': 0, '7': 0,
 'I': 0, 'i': 0, '8': 0,
 'J': 0, 'j': 0, '9': 0,
 'K': 0, 'k': 0, ' ': 0,
 'L': 0, 'l': 0, '.': 0,
 'M': 0, 'm': 0, '!': 0,
 'N': 0, 'n': 0, '?': 0,
 'O': 0, 'o': 0, ':': 0,
 'P': 0, 'p': 0, '-': 0,
 'Q': 0, 'q': 0, ',': 0,
 'R': 0, 'r': 0, ';': 0,
 'S': 0, 's': 0, '(': 0,
 'T': 0, 't': 0, ')': 0,
 'U': 0, 'u': 0, '\n': 0,
 'V': 0, 'v': 0,
 'W': 0, 'w': 0,
 'X': 0, 'x': 0,
 'Y': 0, 'y': 0,
 'Z': 0, 'z': 0}


import sys

for line in sys.stdin.readlines():
    for char in line:
        sym_count[char] += 1

sym_count.pop(' ')
sym_count.pop('\n')
sym_count = {i: j for i, j in sym_count.items() if j != 0}

keys = sorted(list(sym_count.keys()))

max_value = max(sym_count.values())
for i in range(max_value, 0, -1):
    for key in keys:
        print('#' if sym_count[key] >= i else ' ', end='')
    print()
print(*keys, sep='')
