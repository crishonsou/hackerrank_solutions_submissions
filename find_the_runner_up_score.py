if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

largest = max(arr)
l = list(filter(lambda x: x != largest, arr))
print(max(l))
