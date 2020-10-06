# print('Enter the lenght of chocolate bar: ') # Ler o tamanho da barra
# n = int(input())

# sq = [int(ele) for ele in input().split()]

# d, m = [int(ele) for ele in input().split()]

# res = 0

# for i in range(0, n - m + 1):
#    print(sq[i : i + m] , ':' , sum(sq[i : i + m]))
#     if(sum(sq[i : i + m]) == d):
#         res = res + 1
# print(res)


n = int(input())
s = [int(ele) for ele in input().split()]
d, m = [int(ele) for ele in input().split()]
result = 0
for i in range(0, n - m + 1):
    if (sum(s[i : i + m]) == d):
        result = result + 1
print(result)



    
