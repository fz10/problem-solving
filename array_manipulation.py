#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    array = []
    highest = 0

    for i in range(n):
        array.append(0)

    for query in queries:
        start = query[0] - 1
        end = query[1] - 1
        num = query[2]
        ind = start
        for ind in range(start, end + 1):
            array[ind] += num

    for value in array:
        if value > highest:
            highest = value

    return(highest)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    valid = True

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))


    for query in queries:
        if not (query[0] >= 1 and query[1] >= query[0] and query[1] <= n):
            valid = False


    if (n >= 3 and n <= 10**7 and m >= 1 and m <= 2*10**7 and valid):
        result = arrayManipulation(n, queries)
    else:
        print('Invalid operation')

    fptr.write(str(result) + '\n')

    fptr.close()
