### Plus Minus Hacker Hank

import sys
from decimal import *

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

def plusMinus(arr):
    numOfPositives = 0
    numOfNegatives = 0
    numOfZeros = 0
    
    for i in arr:
        if (i > 0):
            numOfPositives += 1

        elif (i < 0):
            numOfNegatives += 1

        else:
            numOfZeros += 1

    fractionOfPositives = Decimal(numOfPositives) / Decimal(n)
    fractionOfPositivesWithPrecision = format(fractionOfPositives, '.6f')
    print(fractionOfPositivesWithPrecision)

    fractionOfNegatives = Decimal(numOfNegatives) / Decimal(n)
    fractionOfNegativesWithPrecision = format(fractionOfNegatives, '.6f')
    print(fractionOfNegativesWithPrecision)

    fractionOfZeros = Decimal(numOfZeros) / Decimal(n)
    fractionOfZerosWithPrecision = format(fractionOfZeros, '.6f')
    print(fractionOfZerosWithPrecision)

plusMinus(arr)




