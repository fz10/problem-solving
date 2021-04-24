#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    highest = 0
    sums = []
    j = 0
    for i in range(4):
        sums.append(arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2])
        sums.append(arr[i][j+1] + arr[i][j+2] + arr[i][j+3] + arr[i+1][j+2] + arr[i+2][j+1] + arr[i+2][j+2] + arr[i+2][j+3])
        sums.append(arr[i][j+2] + arr[i][j+3] + arr[i][j+4] + arr[i+1][j+3] + arr[i+2][j+2] + arr[i+2][j+3] + arr[i+2][j+4])
        sums.append(arr[i][j+3] + arr[i][j+4] + arr[i][j+5] + arr[i+1][j+4] + arr[i+2][j+3] + arr[i+2][j+4] + arr[i+2][j+5])
    highest = sums[0]
    for sum in sums:
        if sum > highest:
            highest = sum
    return highest


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
