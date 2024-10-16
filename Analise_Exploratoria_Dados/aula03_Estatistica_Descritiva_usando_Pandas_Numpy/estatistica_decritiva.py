import numpy as np
import pandas as pd
import statistics as st
from collections import Counter

notas_alunos = [9.5, 7.2, 4.1, 8.9, 10.0]
print('Notas\n', notas_alunos)

#### Média Aritmética ####
media_aritmetica = sum(notas_alunos) / len(notas_alunos)
print(f'\nmédia usando definição: {media_aritmetica:0.1f}')

# Média aritmética usando numpy
media_aritmetica_numpy = np.mean(notas_alunos)
print(f'\nmédia usando numpy: {media_aritmetica_numpy:0.1f}')

# Média aritmética usando pandas
df = pd.DataFrame({'notas': notas_alunos})
media_aritmetica_pandas = df['notas'].mean()
print(f'\nmédia usando pandas: {media_aritmetica_pandas:0.1f}')

#### Média ponderada ####
pesos = [0.1, 0.2, 0.2, 0.3, 0.2]

media_ponderada = 0
for nota, peso in zip(notas_alunos, pesos):
    media_ponderada += nota * peso

media_ponderada = media_ponderada / sum(pesos)
print(f'\nMédia ponderada: {media_ponderada: .1f}')

media_ponderada_numpy = np.average(notas_alunos, weights=pesos)
print(f'\nMédia ponderada numpy: {media_ponderada_numpy: .1f}')

#### Moda ####
notas_alunos = [9.5, 7.2, 4.1, 8.9, 10.0, 4.1, 8.5, 6.3, 9.0,
                4.1, 8.5, 8.5]

c = Counter(notas_alunos)
moda = c.most_common()
print(f'\nModa: {moda}')

# Moda com pandas
df = pd.DataFrame({'notas': notas_alunos})
moda = df['notas'].mode()
print(f'\nModa: {moda}')

# Moda usando statistics
moda = st.mode(notas_alunos)
print(f'\nModa: {moda}')

#### Mediana ####
notas_alunos = [9.5, 7.2, 4.1, 8.9, 10.0, 4.1, 8.5, 6.3, 9.0,
                4.1, 8.5]
mediana = np.median(notas_alunos)
print(f'Mediana usando numpy: {mediana:0.1f}')

#### Amplitude #### 
notas_alunos = [9.5, 7.2, 4.1, 8.9, 10.0, 4.1, 8.5, 6.3, 9.0, 4.1, 8.5]
amplitude = np.ptp(notas_alunos)
print(f'Amplitude: {amplitude:0.2f}')

#### Variância e desvio padrão ####
notas_alunos = [9.5, 7.2, 4.1, 8.9, 10.0, 4.1, 8.5, 6.3, 9.0, 4.1, 8.5]
variancia = np.var(notas_alunos, ddof=1)
desvio_padrao = np.std(notas_alunos, ddof=1)

print(f'\nVariância: {variancia: .1f}')
print(f'\nDesvio Padrão: {desvio_padrao: .1f}')