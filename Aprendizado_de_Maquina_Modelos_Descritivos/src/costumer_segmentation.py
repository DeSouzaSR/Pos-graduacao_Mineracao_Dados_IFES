# %% [markdown]
# ---
# title: Estudos estatíticos
# author: Sandro Ricardo De Souza
# date: 04/26/2024
# format:
#   pdf:
#       toc: true
#       number-sections: true
#       colorlinks: true
# ---

# %%
#| echo: false
# Importação
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
# Set to display all columns
pd.set_option('display.max_columns', None)


# %%
#| echo: false
def cabecalho(titulo):
    print('\n'+titulo)
    print('-'*80)

# %% 
# Caminho
path_file = r'./data/segmentation_data_antigo.csv'

# %%
# Leitura do dataframe
custumer_info = pd.read_csv(path_file)

# %% [markdown]
## Amostra dos dados
# =============================================================================
# Vamos obter uma amostra aleatória dos dados para verificarmos, entre outras
# coisas, os dados faltantes. Se não fizer diferença, vamos remover da amostra, 
# estes dados. Podemos usar a função $f(x) = x^2$, se for preciso.
# 
# A equação
# 
# $$h(x) = \int_a^b (1 - x)dx$$,
# 
# simula melhor.
# =============================================================================


# %%
cabecalho('Amostra')
print(custumer_info.sample(5))


# %% [markdown]
## Informações gerais

# %%
cabecalho('Resumo')
print(custumer_info.info())


# %%
# Contagens
num_columns = ['ID','Age','Income']
cat_columns = ['Sex','Marital status','Education','Occupation','Settlement size']
custumer_info[cat_columns] = custumer_info[cat_columns].astype('str')

# %% [markdown]
## Dados categóricos


# %%
cabecalho('Describe')
print(custumer_info.describe(include='object').T)


# %%
print('\nPrograma finalizado com sucesso!!!')