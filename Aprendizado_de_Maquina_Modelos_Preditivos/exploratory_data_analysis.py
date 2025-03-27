# Importante pacotes
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets

# Carregando datasets
iris = datasets.load_iris()
print(iris.DESCR)


#### Preparando os dados ####

# Características
X = iris.data

# Classes
y = iris.target

print('Nomes das Características (x1, x2, x3, x4):\n',
      iris.feature_names, '\n\n',
      'Classes (y):\n',
      iris.target_names)

# Criando DataFrame para armazenar os dados e facilitar a manipulação
df_iris = pd.DataFrame(X, columns=iris.feature_names)

# Adicionando a coluna "species"
df_iris['species'] = y

# Estatísticas
print("Estatísticas descritivas")
print("------------------------")
print(df_iris.describe())

print("\nQuantidade de elementos de cada classe")
print(df_iris['species'].value_counts())

# Correlação
print('\nCorrelação das colunas')
df_iris = df_iris.drop('species', axis=1)
df_iris_corr = df_iris.corr(method='pearson')
print(df_iris_corr)

# Mapa de calor
f, ax = plt.subplots(figsize=(6, 5))
sns.heatmap(df_iris.corr(), annot=True, fmt=".2f", linewidths=.5, ax=ax,
            vmin=-1, vmax=1, cmap='vlag_r')
f.subplots_adjust(top=0.959, bottom=0.293, left=0.245, right=0.972,
                  hspace=0.5, wspace=0.5)
plt.savefig('figures/iris_heatmap.png')
plt.show()

# Criando uma máscara triangular
f, ax = plt.subplots(figsize=(6, 5))
mask = np.triu(df_iris_corr)
sns.heatmap(df_iris_corr, ax=ax, mask=mask,
            annot=True, fmt=".2f", linewidths=0.5,
            vmin=-1, vmax=1, cmap="vlag")
f.subplots_adjust(top=0.959, bottom=0.293, left=0.245, right=0.972,
                  hspace=0.5, wspace=0.5)
plt.savefig('figures/iris_heatmap2.png')
plt.show()