"""
Questão 2
Encontre a média, a mediana e a moda das distribuições de dados apresentadas
nas tabelas a seguir.

Exemplo de Tabela
"""
#%%
# Imports
import numpy as np
import pandas as pd
import statistics as st
import matplotlib.pyplot as plt
import seaborn as sns

#%% 
# Entrada
numeros = [6, 1, 1, 10, 6, 4, 8, 1, 6, 2, 1, 4, 10, 0, 4, 9, 5, 6, 4, 9, 10,
           1, 6, 7, 6, 1, 4, 3, 6, 0, 2, 4, 5, 5, 5, 2, 9, 0, 6, 8, 1, 8, 4,
           6, 1, 1, 8, 7, 4, 3]

#%%
# Exploração dos dados
sns.histplot(numeros, kde=True)
plt.title('Histograma dos dados')
plt.xlabel('Valores')
plt.ylabel('Frequência')
plt.show()

#%%
# Cálculo
mean = np.mean(numeros)
median = np.median(numeros)
moda = st.multimode(numeros)

#%%
# Saída
print(f'A média dos dados é: {mean:.2f}')
print(f'A mediana dos dados é: {median:.2f}')
print(f'A moda dos dados é: {moda} - bimodal')