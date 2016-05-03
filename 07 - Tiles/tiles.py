import numpy as np
import kadane
import string

with open('submitInput', 'rb') as f:
    lines = f.readlines()
    lines = map(lambda x: x.replace('\n', ''), lines)
    cases = int(lines[0])
    lines = lines[1:]

conv_table = {'.': 0}
for index, letter in enumerate(list(string.ascii_uppercase)):
    value = index + 1
    conv_table[letter] = value
    conv_table[letter.lower()] = -value

case = 1
i = 0
with open('output.txt', 'wb') as out:
    while case != cases + 1:
        print 'Processing case ' + str(case) + ' / ' + str(cases)
        n, m = map(lambda x: int(x), lines[i].split())
        matrix = np.zeros(shape=(n, m), dtype=np.int8)
        for x in range(n):
            i += 1
            matrix[x] = map(lambda x: conv_table[x], list(lines[i]))
        # Time complexity of this algorithm is O(row*col*col)
        if n < m:
            matrix = matrix.T
            q = n
            n = m
            m = q
        # Sum of matrix positive
        if np.sum(matrix) > 0:
            out.write('Case #' + str(case) + ': INFINITY\n')
        # Sum of any row / column positive
        elif len(filter(lambda x: x > 0, np.sum(matrix, axis=0))) > 0:
            out.write('Case #' + str(case) + ': INFINITY\n')
        elif len(filter(lambda x: x > 0, np.sum(matrix, axis=1))) > 0:
            out.write('Case #' + str(case) + ': INFINITY\n')
        else:
            # Construct 2x2 tile, run kadane 2d to determine maximum sum
            two_by_two = np.tile(matrix, (2, 2))
            res_two = kadane.max_sum(two_by_two)
            out.write('Case #' + str(case) + ': ' + str(res_two[0]) + '\n')
        i += 1
        case += 1
