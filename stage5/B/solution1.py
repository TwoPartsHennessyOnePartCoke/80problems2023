# AC, Принята

from itertools import groupby

def count_sequences(matrix):
        sequence_lengths = {}
        for row in matrix:
            for key, group in groupby(row):
                if key == '.':
                    length = len(list(group))
                    if length in sequence_lengths:
                        sequence_lengths[length] += 1
                    else:
                        sequence_lengths[length] = 1
        return sequence_lengths

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    matrix = []

    for i in range(n):
        matrix.append(input())

    transposed_matrix = list(map(list, zip(*matrix)))
    values = count_sequences(matrix + transposed_matrix)
    if 1 in values:
        del values[1]

    print(' '.join(str(i) + '-' + str(values[i]) for i in sorted(values.keys())))
