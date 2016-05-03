import numpy as np


def kadane(arr):
    max = 0
    max_start = -1
    max_end = -1
    current_start = 0
    max_so_far = 0
    for i in range(len(arr)):
        max_so_far += arr[i]
        if max_so_far < 0:
            max_so_far = 0
            current_start = i + 1
        if max < max_so_far:
            max_start = current_start
            max_end = i
            max = max_so_far
    return max, max_start, max_end


def max_sum(matrix):
    rows, cols = matrix.shape
    temp = np.zeros(shape=rows, dtype=np.int32)
    result = (0, 0, 0, 0, 0)
    for left in range(cols):
        for i in range(rows):
            temp[i] = 0
        for right in range(left, cols):
            for i in range(rows):
                temp[i] += matrix[i][right]
            kad_result = kadane(temp)
            if kad_result[0] > result[0]:
                result = (kad_result[0], left, right,
                          kad_result[1], kad_result[2])
    return result
