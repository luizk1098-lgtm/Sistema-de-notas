# VARIÁVEL QUE ARMAZENA O NOME DO ALUNO
nome_aluno = str(input('Digite o nome do aluno: '))

# LISTA QUE ARMAZENA A NOTA DO ALUNO INSERIDA NO LAÇO DE REPETIÇÃO 
nota = []

# LAÇO DE REPETIÇÃO QUE RECEBE A NOTA DO ALUNO E ARMAZENA NA LISTA OU ENCERRA O PROGRAMA
while True: 
    entrada = str(input("Digite a nota do aluno (ou 'S' para sair): "))
    if entrada.lower() == 's':
        print('Operação encerrada')
        break
    nota.append(float(entrada))
   
# CALCULO DA NOTA DENTRO DA LISTA   
print('_'*55) 
if len(nota) > 0:
    media = sum(nota) / len(nota)
    if media >= 7:
        situacao = ('Aluno Aprovado')
    else:
        situacao = ('Aluno Reprovado')
    
    # SITUAÇÃO DO ALUNO BASEADO NA NOTA   
    print(f'Nome do aluno: {nome_aluno}')
    print(f'Média = {media}')
    print(f'Situação do aluno: {situacao}')
else:
    print('A lista está vazia, não foi possível calcular a média. ')