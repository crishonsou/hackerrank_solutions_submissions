s, n, m = map(int, input().strip().split())

keyboard = sorted(map(int, input().strip().split()), reverse=True)
usb = sorted(map(int, input().strip().split()))

i = j = 0
ans = -1

for i in keyboard:
    for j in usb:
        if i + j > s:
            break
        ans = max(ans, i + j)

print(ans)
