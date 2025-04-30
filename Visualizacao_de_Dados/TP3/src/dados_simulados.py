# Criar um conjunto de dados de IDEB simulado para os municípios do Espírito
# Santo, gerando valores aleatórios entre 3.0 e 7.0.
#  DataFrame gerado deve conter:
#   - o cod_mun (código do município),
#   - o ideb_ano (valor simulado do IDEB).
#   - serão 78 municípios.

import pandas as pd
import numpy as np
import random
import os
import logging

# Configuração do logging
# O arquivo de logo deve ter o nome deste script com o sufixo .log
log_file_path = os.path.join(os.path.dirname(__file__), 'dados_simulados.log')  
logging.basicConfig(
    filename=log_file_path,
    filemode='w',  # 'w' para sobrescrever o arquivo a cada execução
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)   

# Ler os nomes e códigos dos municípios do Espírito Santo
path_nomes_codigos = r"../../../datasets/nomes_codigos_municipios_ES.xlsx"
nomes_codigos_df = pd.read_excel(path_nomes_codigos)
if nomes_codigos_df.empty:
    raise ValueError("O arquivo de nomes e códigos dos municípios está vazio " \
    "ou não foi lido corretamente. Verifique o caminho e o formato do arquivo.")    

# Incluir nos dataframe nomes_codigos_df uma coluna com valor ideb simulado
# Gerar valores aleatórios entre 3.0 e 7.0 para o IDEB
ideb_simulado = [round(random.uniform(3.0, 7.0), 1) for _ in range(len(nomes_codigos_df))]
nomes_codigos_df['ideb_2023'] = ideb_simulado



