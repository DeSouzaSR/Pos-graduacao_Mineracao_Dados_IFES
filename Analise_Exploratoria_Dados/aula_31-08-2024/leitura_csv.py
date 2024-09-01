import pandas as pd
from collections import Counter

file_path = '../../datasets/extended_essay-br.csv'

dataset = pd.read_csv(file_path)

lista_competencias = ['c1', 'c2', 'c3', 'c4', 'c5']

for competencia in lista_competencias:
    notas = dataset[competencia].values
    distribuicao_notas = Counter(notas)
    
    print(f'Competências: {competencia}')
    print(f'Distribuição de notas')

    for nota, frequencia in distribuicao_notas.items():
        print(f'\t\tNota: {nota} -- Frequência: {frequencia}')

