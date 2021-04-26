#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swaps = 0
    for i in range(1, len(arr)):
        if(arr.index(i) != i - 1):
            arr[arr.index(i)] = arr[i - 1]
            arr[i -1 ] = i
            swaps += 1
    print(arr)
    return(swaps)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    res = minimumSwaps(arr)
    fptr.write(str(res) + '\n')
    fptr.close()
