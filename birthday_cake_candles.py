def birthdayCakeCandles(ar):
    size = 0
    count = 0

    for i in ar:
        if i > size:
            size = i
            count = 0

        if i == size:
            count += 1

    return count
