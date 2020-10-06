### Min-Max Sum


arr = list(map(int, input().rstrip().split()))


def miniMaxSum(arr):
    arr=sorted(arr)
    s = sum(arr)
    print(s-arr[-1],s-arr[0])


miniMaxSum(arr)
