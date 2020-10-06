def breakingRecords(scores):
    min_ele = scores[0]
    max_ele = scores[0]
    min_cnt = 0
    max_cnt = 0
     
    for ele in scores:
        if ele > max_ele:
            max_ele = ele
            max_cnt += 1
        if ele < min_ele:
            min_ele = ele
            min_cnt += 1
     
    return max_cnt, min_cnt


if __name__ == '__main__':
    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    print(result)

