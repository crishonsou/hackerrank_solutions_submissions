from collections import defaultdict

# d = defaultdict(list)
# d['python'].append('awesome')
# d['something-else'].append('not-relevant')
# d['python'].append('language')

# for i in d.items():
#    print(i)


n, m = list(map(int, input().split()))
d = defaultdict(list)
for i in range(n):
    d[input()].append(i + 1)
for i in range(m):
    print(*d[input()] or [-1])

