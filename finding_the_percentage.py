def avg(lst): ## Define a função para retornar a porcentagem das notas de um estudante em especifico
    return (lst[0] + lst[1] +lst[2])/3

if __name__ == '__main__':
    n = int(input()) # Define a entrada da quantidade de estudantes
    student_marks = {} # Cria uma lista vazia para as notas e nomes
    for _ in range(n): ## Condição de Parada
        name, *line = input().split() ## Faz o split dos nomes dos estudantes em linha
        scores = list(map(float, line)) ## Faz a separação das notas dos estudantes (mesmo que tenham digitado as notas em formato int, por ex.) e formata em float
        student_marks[name] = scores ## Associa nomes e notas numa nova lista formatada
    query_name = input()  ## Faz a busca pelo nome do estudante em específico
    print(f'{avg(student_marks[query_name]):.2f}') ## Acha a porcentagem das notas utilizando a função definida. Printa o resultado
