# Este notebook tem como objetivo demonstrar a identificação de perfis de
# estudantes com base em dados educacionais, utilizando modelos 
# descritivos e técnicas de agrupamento (clustering)
#
# Pontos-chave:
#
# Modelos descritivos ajudam a resumir, explorar e visualizar dados.
# No contexto educacional, podemos usar esses modelos para identificar perfis de engajamento e desempenho.
# O clustering é uma técnica não supervisionada que agrupa instâncias semelhantes entre si.
# 
# Técnicas usadas neste notebook:
#
# Estatística descritiva (média, desvio padrão)
# Visualização de dados (gráficos)
# K-means clustering


# Importação de bibliootecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score

# Porque o wsl fica tentando usar o OpenGL e não fucnciona muito bem.
# Estou usando o TK
import matplotlib
matplotlib.use('TkAgg')

# Simulação do dataset
# Será feita uma simulação de dataset
# O dataset simulado contém dados de estudantes com as seguintes colunas:
#
# 'id': identificador do estudante
# 'acessos': número de acessos ao AVA
# 'participacoes': número de interações em fóruns
# 'entregas': percentual de tarefas entregues
# 'nota_final': nota final no curso
data = {
    'id': range(1, 21),
    'acessos': [25, 10, 5, 40, 35, 20, 15, 8, 50, 30, 45, 12, 18, 22, 28, 6, 4, 38, 44, 7],
    'participacoes': [12, 4, 2, 18, 16, 8, 5, 2, 20, 14, 19, 3, 6, 10, 11, 1, 0, 17, 18, 2],
    'entregas': [0.9, 0.6, 0.4, 1.0, 0.95, 0.8, 0.7, 0.5, 1.0, 0.85, 1.0, 0.55, 0.65, 0.75, 0.8, 0.3, 0.2, 0.9, 1.0, 0.4],
    'nota_final': [8.5, 6.0, 4.5, 9.5, 9.0, 7.5, 6.5, 5.0, 10.0, 8.0, 9.5, 5.5, 6.0, 7.0, 7.5, 3.5, 2.0, 8.5, 9.5, 4.0]
}
df = pd.DataFrame(data)

# Estatística descritiva
print("Perfil dos estudantes\n")
print("\nEstatísticas Descritivas:")
print(df.describe())

# Visualização dos dados
sns.pairplot(df.drop('id', axis=1))
plt.suptitle('Visualização Inicial das Variáveis', y=1.02)
plt.show()

# Normalização de dados
features = ['acessos', 'participacoes', 'entregas', 'nota_final']
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df[features])

# Determinação do Melhor Número de Clusters com Silhouette
range_n_cluster = range(2, 10)
best_n = 2
best_score = -1

for n_clusters in range_n_cluster:
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    cluster_labels = kmeans.fit_predict(df_scaled)
    silhouette_avg = silhouette_score(df_scaled, cluster_labels)
    print(f'Para n_cluster = {n_clusters}, o coeficiente de silhouette é {silhouette_avg:.4f}')
    if silhouette_avg > best_score:
        best_n = n_clusters
        best_score = silhouette_avg

print(f'\nMelhor número de clusters com base no silhouette: {best_n}')

#Aplicando KMeans com o melhor número de clusters
kmeans = KMeans(n_clusters=best_n, random_state=42)
df['cluster'] = kmeans.fit_predict(df_scaled)
df
print('\nMédias por cluster:')
print(df.groupby('cluster')[features].mean().round(2))

# Análise do cluster 0
df0 = df[df['cluster'] == 0]
df0.hist(figsize=(10, 10))
plt.suptitle('Histograma dos dados do cluster 0')
plt.show()

# Análise do cluster 1
df0 = df[df['cluster'] == 1]
df0.hist(figsize=(10, 10))
plt.suptitle('Histograma dos dados do cluster 1')
plt.show()

# Visualização dos Clusters com PCA
pca = PCA(n_components=2)
df_pca = pca.fit_transform(df_scaled)
df['pca1'] = df_pca[:, 0]
df['pca2'] = df_pca[:, 1]

# Plot
plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x='pca1', y='pca2', hue='cluster', palette='Set2', s=100)
plt.title('Visualização dos Clusters com PCA')
plt.xlabel('Componente Principal 1')
plt.ylabel('Componente Principal 2')
plt.legend(title='Cluster')
plt.grid(True)
plt.show()

# Embora o PCA reduza a dimensionalidade, ele mantém a maior parte da variabilidade dos 
# dados, distribuída entre as componentes principais. Para entender quais atributos são 
# mais importantes na nova representação, podemos analisar os loadings 
# (pesos de cada variável nas componentes principais).
# Obtendo os loadings (importância das variáveis em cada componente)
loadings = pca.components_

# Criando um DataFrame para melhor visualização
pca_loadings_df = pd.DataFrame(loadings, columns=features, index=['PC1', 'PC2'])
print("\nImportância das variáveis nas componentes principais:")
print(pca_loadings_df.round(2))
