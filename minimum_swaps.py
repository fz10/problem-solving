#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):

    array = dict(enumerate(arr,1))
    array2 = {v:k for k,v in array.items()}
    swaps = 0
    for v in array:
        x = array[v]
        if x != v:
            y = array2[v]
            array[y] = x
            array2[x] = y
            swaps += 1
    return(swaps)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    res = minimumSwaps(arr)
    fptr.write(str(res) + '\n')
    fptr.close()
