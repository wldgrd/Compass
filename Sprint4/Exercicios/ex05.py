'''Um determinado sistema escolar exporta a grade de notas dos estudantes em formato CSV. 
Cada linha do arquivo corresponde ao nome do estudante, acompanhado de 5 notas de avaliação, no intervalo [0-10]. 
É o arquivo estudantes.csv de seu exercício.

Precisamos processar seu conteúdo, de modo a gerar como saída um relatório em formato textual contendo as seguintes informações:

Nome do estudante
Três maiores notas, em ordem decrescente
Média das três maiores notas, com duas casas decimais de precisão

O resultado do processamento deve ser escrito na saída padrão (print), 
ordenado pelo nome do estudante e obedecendo ao formato descrito a seguir:

Nome: <nome estudante> Notas: [n1, n2, n3] Média: <média>

Exemplo:

Nome: Maria Luiza Correia Notas: [7, 5, 5] Média: 5.67

Nome: Maria Mendes Notas: [7, 3, 3] Média: 4.33

Em seu desenvolvimento você deverá utilizar lambdas e as seguintes funções:

round

map

sorted'''

def processa_dados(arquivo):    
    from functools import reduce

    with open(arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
    
    relatorio =  reduce( lambda info, aluno: info + [f"Nome: {aluno['Nome']} Notas: {aluno['Notas']} Média: {aluno['Média']}"],
    sorted(
        map(
            lambda linha: {
                'Nome': linha.split(',')[0],
                'Notas': sorted(map(int, linha.strip().split(',')[1:]), reverse = True)[:3],
                'Média': round(sum(sorted(map(int, linha.strip().split(',')[1:]), reverse = True)[:3]) /3 ,2)
                                },linhas), key=lambda x: x['Nome']), [])
    print('\n'.join(relatorio))
    
processa_dados('estudantes.csv')