
# Desenvolver um algoritmo para exibição de gráficos coropléticos dos municípios do Espírito Santo (ES), utilizando dados do IDEB.

import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import geopandas.tools
import seaborn as sns
import matplotlib.colors as mcolors
import matplotlib.cm as cm
import matplotlib as mpl
import os
import logging

# Diretório de trabalho
os.chdir(r"C:\Users\srsouza\Documents\Estudos\Pos-graduacao_Mineracao_Dados_IFES\Visualizacao_de_Dados\TP3\src")

# Configurar aquivo de log no mesmo diretório do script
# configuração dever permitir reescrever o arquivo de log a cada execução
log_file_path = os.path.join(os.path.dirname(__file__), 'execucao.log')
logging.basicConfig(
    filename=log_file_path,
    filemode='w',  # 'w' para sobrescrever o arquivo a cada execução
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Caminho para dados do ideb dos municípios do ES
path_ideb = r"..\..\..\datasets\divulgacao_ensino_medio_municipios_2023.xlsx"
ideb_df = pd.read_excel(path_ideb)

# Caminho para shapefile dos municípios do ES e df para shapefile
path_shapefile = r"../../../datasets/municipios_es/ES_Municipios_2024.shp"
municipios_shp = gpd.read_file(path_shapefile)

# Mudando o nome de uma coluna, de NM_MUN para municipio
municipios_shp.rename(columns={'NM_MUN': 'municipio'}, inplace=True)

# Verificar se o shapefile foi lido corretamente
if municipios_shp.empty:
    raise ValueError("O shapefile dos municípios do ES está vazio ou não foi lido corretamente. Verifique o caminho e o formato do arquivo.")   

# Verficar se o arquivo foi lido corretamente
if ideb_df.empty:
    raise ValueError("O arquivo de dados do IDEB está vazio ou não foi lido corretamente. Verifique o caminho e o formato do arquivo.") 

# Usando logging para registrar informações sobre o processo
# Exibir informações sobre os datasets
logging.info(f"Shape do DataFrame do IDEB: {ideb_df.shape}")
logging.info(f"Shape do GeoDataFrame dos Municípios: {municipios_shp.shape}")
logging.info(f"Colunas do DataFrame do IDEB: {ideb_df.columns.tolist()}")
logging.info(f"Colunas do GeoDataFrame dos Municípios: {municipios_shp.columns.tolist()}")
logging.info(f"Primeiras linhas do DataFrame do IDEB:\n{ideb_df.head()}")
logging.info(f"Primeiras linhas do GeoDataFrame dos Municípios:\n{municipios_shp.head()}")

# Juntar os dois DataFrames com base na coluna 'municipio'
ideb_municipios = municipios_shp.merge(ideb_df, on='municipio', how='left')

# Verificar se a junção foi realizada corretamente
if ideb_municipios.empty:
    raise ValueError("A junção dos DataFrames falhou. Verifique se as colunas 'municipio' estão corretas em ambos os DataFrames.")  


# Exibir informações sobre o DataFrame resultante
logging.info(f"Shape do DataFrame resultante da junção: {ideb_municipios.shape}")
logging.info(f"Colunas do DataFrame resultante da junção: {ideb_municipios.columns.tolist()}")
logging.info(f"Primeiras linhas do DataFrame resultante da junção:\n{ideb_municipios.head()}")

# Criar o cartograma Dorling
fig, ax = plt.subplots(1, 1, figsize=(10, 10))
ideb_municipios.boundary.plot(ax=ax, linewidth=1, color='black')
ideb_municipios.plot(column='ideb_2023', ax=ax, legend=True, cmap='viridis', edgecolor='black', linewidth=0.5)

# Limitar visualização (x = longitude, y = latitude)
# consegui estas coordenadas no Google Maps
ax.set_xlim(-42.034520, -39.351673)
ax.set_ylim(-21.385750, -17.775498)

plt.title('IDEB dos Municípios do Espírito Santo (2023)', fontsize=15)
plt.axis('off')
plt.tight_layout()
plt.savefig('../../figuras/ideb_municipios_es.png', dpi=300, bbox_inches='tight')
plt.show()

# Exibir mensagem de conclusão
logging.info("Processo de visualização de dados concluído com sucesso.")

