def diagonalDifference(arr):
    diagonal1 = 0
    diagonal2 = 0
    for i in range(len(arr)):
        diagonal1+= arr[i][i]
        diagonal2+= arr[i][len(arr)-i-1]
    return (abs(diagonal1- diagonal2))
