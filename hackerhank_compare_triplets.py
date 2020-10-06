import math
import os
import random
import re
import sys

def solve(a, b):
    score_a = score_b = 0
    # loop over each element and compare with corresponding element in other array
    for i, elem in enumerate(a):
        if elem > b[i]:
            score_a = score_a + 1
        elif elem == b[i]:
            pass
        elif elem < b[i]:
            score_b = score_b + 1

    return '{}{}'.format(score_a, score_b)


