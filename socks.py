#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    colors = {}
    pairs = 0
    if((n >= 1 and n <= 100)):
        for color in ar:
            if color in colors.keys():
                colors[color] += 1
            else:
                colors[color] = 1

    for color in colors:
        if colors[color]%2 == 0:
            pairs += colors[color] / 2
        elif (colors[color] - 1)%2 == 0:
            pairs += (colors[color] - 1) / 2
    print(colors)
    print(f'Number of pairs is: {int(pairs)}')
    return int(pairs)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
