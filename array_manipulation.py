#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    array = [0 for x in range(n)]
    highest = 0

    for query in queries:
        start = query[0] - 1
        end = query[1] - 1
        num = query[2]
        ind = start
        for ind in range(start, end + 1):
            array[ind] += num
            if array[ind] > highest:
                highest = array[ind]

    return(highest)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')


    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))


    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
