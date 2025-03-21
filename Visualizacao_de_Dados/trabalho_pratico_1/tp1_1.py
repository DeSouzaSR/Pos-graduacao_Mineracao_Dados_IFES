"""
O Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira
(Inep) disponibiliza, por meio de sua página na web, indicadores educacionais,
como a Média de Alunos por Turma. Fazer o download da base de dados dos 
Municípios referente a 2023 (ou usar o arquivo ATU_MUNICIPIOS_2023.xlsx).
Estes arquivos estão contidos num arquivo zip acessando o seguinte
link: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadoreseducacionais/media-de-alunos-por-turma) 
 
Elaborar um gráfico que mostre a distribuição da média de alunos por turma 
(do 1º ao 9º ano incluindo a Turma Multietapa, Multi ou Correção de Fluxo, 
sendo todas estas do Ensino Fundamental) do Município de Vitória/ES. 
O gráfico deve apresentar apenas os dados de localização TOTAL (isto é, não 
use os dados de áreas urbanas ou rurais), nos cinco tipos de escola (Federal,
Estadual, Municipal, Privada, Pública). Dica: seus dados de análise ficarão
restritos a cinco linhas e dez colunas.

O arquivo csv Vitoria.csv contém apenas os dados de Vitória, já com os totais
por cada esfera administrativa. Também possui os seguintes campos:
Dependência Administrativa;1º Ano;2° ano;3° ano;
4° ano;5° ano;6° ano; 7° ano; 8° ano;9° ano;TMMCF

E possui as seguintes dependências administrativas: Federal, Estadual,
Municipal, Privada, Pública.

"""

import pandas as pd
import matplotlib.pyplot as plt

# Carregar o arquivo csv
df = pd.read_csv('vitoria.csv', sep=';')

# Separando escolas privadas e públicas
privadas = df[df['Dependência Administrativa'] == 'Privada']
publicas = df[df['Dependência Administrativa'] == 'Pública']

# Plotar gráfico de barras com a média de alunos por turma para privadas e pública
plt.bar(privadas['Dependência Administrativa'], privadas.mean()[1:], label='Privadas')
plt.bar(publicas['Dependência Administrativa'], publicas.mean()[1:], label='Públicas')  


plt.title('Média de alunos por turma por dependência administrativa')
plt.xlabel('Dependência Administrativa')
plt.ylabel('Média de alunos por turma')
plt.legend()
plt.show()

