a = [[ input(), float(input())] for i in range(int(input()))] ## Define as entradas das notas e dos nomes dos estudantes dentro de uma lista
s = sorted(set([x[1] for x in a])) ## Coloca a lista das notas e nomes dos estudantes em ordem alfabética
for name in sorted(x[0] for x in a if x[1] == s[1]): ## Verifica a ordem alfabetica e sua ordem para a impressão correta
    print(name)
