import pandas as pd
pd.set_option('display.max_columns', 500)

# Dataframe
caminho_csv = '../../datasets/igm_modificado.csv'
dataframe = pd.read_csv(caminho_csv, sep=',', encoding='utf-8', thousands=',')

