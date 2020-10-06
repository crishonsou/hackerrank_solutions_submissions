####### Print Staircase


def staircase(n):
    for i in range(0, n):
        print(' ' * (n - i -1) + "#" * (i + 1))

staircase(6)
