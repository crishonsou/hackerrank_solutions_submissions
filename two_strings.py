s1 = input()
s2 = input()

def twoStrings(s1, s2):
    m1 = set(s1)
    m2 = set(s2)
    if set.intersection(m1, m2):
        return 'YES'
    return 'NO'


print(twoStrings(s1, s2))





