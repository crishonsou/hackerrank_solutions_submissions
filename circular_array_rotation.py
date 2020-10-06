import math
import os
import random
import re
import sys

def circularArrayRotation(a, k, queries):
    new_arr = a[-k%len(a):] + a[:-k%len(a)]
    result = []
    for i in queries:
        result.append(new_arr[i])
    return result

if __name__ == '__main__':

    nkq = input().split()

    n = int(nkq[0])

    k = int(nkq[1])

    q = int(nkq[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
