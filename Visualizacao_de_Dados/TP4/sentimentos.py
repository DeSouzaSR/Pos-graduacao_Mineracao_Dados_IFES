# -*- coding: utf-8 -*-

import pandas as pd
from transformers import pipeline
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------------------------------------------------------
# Funções
# -----------------------------------------------------------------------------

# Função para aplicar a análise de sentimento e extrair rótulo e score
def analisar_sentimento(texto, analisador):
    if analisador is None or not texto or pd.isna(texto):
        return None, None  # Retorna None se o analisador não carregou ou o texto é inválido
    try:
        resultado = analisador(texto)
        # O resultado é uma lista com um dicionário, e.g., [{'label': 'POSITIVE', 'score': 0.99}]
        # Alguns modelos podem retornar labels como '1 star', '5 stars', etc.
        # É importante verificar o output específico do modelo ou mapear para POSITIVE/NEGATIVE/NEUTRAL
        label = resultado[0]['label']
        score = resultado[0]['score']

        # Padronização dos rótulos (exemplo, pode precisar de ajuste conforme os modelos)
        if label.upper() in ['POSITIVE', 'LABEL_2', ' Alegria', 'Positivo']: # Adicionar outros rótulos positivos que o modelo possa retornar
             label_padronizado = 'Positivo'
        elif label.upper() in ['NEGATIVE', 'LABEL_0', 'Tristeza', 'Raiva', 'Medo', 'Negativo']: # Adicionar outros rótulos negativos
             label_padronizado = 'Negativo'
        elif label.upper() in ['NEUTRAL', 'LABEL_1', 'Neutro']: # Adicionar outros rótulos neutros
             label_padronizado = 'Neutro'
        else: # Se o rótulo não for reconhecido, manter o original para inspeção
            label_padronizado = label 
        return label_padronizado, score
    except Exception as e:
        print(f"Erro ao analisar texto: '{texto[:50]}...': {e}")
        return None, None


# -----------------------------------------------------------------------------
# Passo 1: Preparação dos Dados
# -----------------------------------------------------------------------------


# Carregar o dataframe
try:
    df = pd.read_csv(r'..\..\datasets\brazilian_headlines_sentiments.csv') # Ajuste o caminho se necessário
except FileNotFoundError:
    print("Arquivo 'brazilian_headlines_sentiments.csv' não encontrado. Por favor, verifique o caminho.")

# Filtrar manchetes que contêm 'Bolsonaro' nas keywords
# Assegurando que a coluna 'keywords' é do tipo string antes de usar .str
df['keywords'] = df['keywords'].astype(str)
df_bolsonaro = df[df['keywords'].str.contains("'Bolsonaro'", case=False, na=False)].copy()

# Verificar o número de manchetes relacionadas a Bolsonaro
print(f"Número de manchetes relacionadas a Bolsonaro: {len(df_bolsonaro)}")
if not df_bolsonaro.empty:
    print("Amostra das manchetes filtradas:")
    print(df_bolsonaro[['website', 'keywords', 'headlinePortuguese']].head())
else:
    print("Nenhuma manchete relacionada a Bolsonaro foi encontrada com o critério de filtro.")


# -----------------------------------------------------------------------------
# Passo 2: Seleção e Carregamento dos Modelos
# -----------------------------------------------------------------------------

# Modelo 1
modelo_1_nome = "turing-usp/FinBertPTBR"
analisador_sentimento_1 = None # Inicializa como None
try:
    analisador_sentimento_1 = pipeline("sentiment-analysis", model=modelo_1_nome)
    print(f"Modelo 1 ({modelo_1_nome}) carregado com sucesso.")
except Exception as e:
    print(f"Erro ao carregar modelo 1 ({modelo_1_nome}): {e}")
    print("Verifique se o nome do modelo está correto, se há conexão com a internet e se as dependências (como TensorFlow ou PyTorch) estão instaladas.")

# Modelo 2
modelo_2_nome = "neuralmind/bert-base-portuguese-cased"
analisador_sentimento_2 = None # Inicializa como None
try:
    analisador_sentimento_2 = pipeline("sentiment-analysis", model=modelo_2_nome)
    print(f"Modelo 2 ({modelo_2_nome}) carregado com sucesso.")
except Exception as e:
    print(f"Erro ao carregar modelo 2 ({modelo_2_nome}): {e}")
    print("Verifique se o nome do modelo está correto, se há conexão com a internet e se as dependências (como TensorFlow ou PyTorch) estão instaladas.")


# -----------------------------------------------------------------------------
# Passo 3: Aplicação dos Modelos às Manchetes
# (Já definida a função acima)
# -----------------------------------------------------------------------------

# Aplicar Modelo 1 (se carregado)
if analisador_sentimento_1:
    print(f"\nAplicando Modelo 1 ({modelo_1_nome})...")
    # Usar .loc para evitar SettingWithCopyWarning
    df_bolsonaro.loc[:, 'sentimento_modelo1'] = None
    df_bolsonaro.loc[:, 'score_modelo1'] = None

    for index, row in df_bolsonaro.iterrows():
        label, score = analisar_sentimento(row['headlinePortuguese'], analisador_sentimento_1)
        df_bolsonaro.loc[index, 'sentimento_modelo1'] = label
        df_bolsonaro.loc[index, 'score_modelo1'] = score
    print("Modelo 1 aplicado.")
    print(df_bolsonaro[['headlinePortuguese', 'sentimento_modelo1', 'score_modelo1']].head())

# Aplicar Modelo 2 (se carregado)
if analisador_sentimento_2:
    print(f"\nAplicando Modelo 2 ({modelo_2_nome})...")
    df_bolsonaro.loc[:, 'sentimento_modelo2'] = None
    df_bolsonaro.loc[:, 'score_modelo2'] = None

    for index, row in df_bolsonaro.iterrows():
        label, score = analisar_sentimento(row['headlinePortuguese'], analisador_sentimento_2)
        df_bolsonaro.loc[index, 'sentimento_modelo2'] = label
        df_bolsonaro.loc[index, 'score_modelo2'] = score
    print("Modelo 2 aplicado.")
    print(df_bolsonaro[['headlinePortuguese', 'sentimento_modelo2', 'score_modelo2']].head())

# -----------------------------------------------------------------------------
# Passo 4: Análise dos Resultados
# -----------------------------------------------------------------------------

# Para esta etapa, vamos assumir que pelo menos um modelo foi carregado e aplicado.
# Se ambos foram carregados, podemos escolher um para a análise principal ou comparar.
# Vamos usar o Modelo 1 como exemplo, se disponível, caso contrário o Modelo 2.

coluna_sentimento_ativa = None
if 'sentimento_modelo1' in df_bolsonaro.columns and analisador_sentimento_1:
    coluna_sentimento_ativa = 'sentimento_modelo1'
    print(f"\nAnalisando resultados com base no Modelo 1 ({modelo_1_nome}).")
elif 'sentimento_modelo2' in df_bolsonaro.columns and analisador_sentimento_2:
    coluna_sentimento_ativa = 'sentimento_modelo2'
    print(f"\nAnalisando resultados com base no Modelo 2 ({modelo_2_nome}).")
else:
    print("\nNenhum modelo de sentimento foi aplicado com sucesso. Não é possível analisar os resultados.")

if coluna_sentimento_ativa:
    # Pergunta 1: Qual é o sentimento geral dos jornalistas para o presidente Bolsonaro?
    print("\n--- Sentimento Geral sobre Bolsonaro ---")
    sentimento_geral_bolsonaro = df_bolsonaro[coluna_sentimento_ativa].value_counts(normalize=True) * 100
    print(sentimento_geral_bolsonaro)
    print(f"Contagem total: {df_bolsonaro[coluna_sentimento_ativa].value_counts().to_dict()}")


    # Pergunta 2: Qual é o sentimento por site?
    print("\n--- Sentimento sobre Bolsonaro por Site ---")
    sentimento_por_site = df_bolsonaro.groupby('website')[coluna_sentimento_ativa].value_counts(normalize=True).mul(100).unstack(fill_value=0)
    # Para melhor visualização, podemos adicionar a contagem total por site também
    contagem_por_site = df_bolsonaro.groupby('website')[coluna_sentimento_ativa].count()
    sentimento_por_site_com_contagem = pd.concat([sentimento_por_site, contagem_por_site.rename('Total_Manchetes_Bolsonaro')], axis=1)

    print(sentimento_por_site_com_contagem)

    # Se ambos os modelos foram aplicados, você pode querer comparar as contagens
    if 'sentimento_modelo1' in df_bolsonaro.columns and 'sentimento_modelo2' in df_bolsonaro.columns and analisador_sentimento_1 and analisador_sentimento_2:
        print("\n--- Comparação entre Modelos (Contagem Geral) ---")
        print("Modelo 1:")
        print(df_bolsonaro['sentimento_modelo1'].value_counts())
        print("\nModelo 2:")
        print(df_bolsonaro['sentimento_modelo2'].value_counts())

        # Comparação de concordância (exemplo simples)
        concordancia = (df_bolsonaro['sentimento_modelo1'] == df_bolsonaro['sentimento_modelo2']).mean() * 100
        print(f"\nPercentual de concordância entre Modelo 1 e Modelo 2: {concordancia:.2f}%")

        # Casos de discordância para inspeção (primeiros 5)
        discordantes = df_bolsonaro[df_bolsonaro['sentimento_modelo1'] != df_bolsonaro['sentimento_modelo2']]
        if not discordantes.empty:
            print("\nExemplos de manchetes com sentimentos discordantes entre os modelos:")
            print(discordantes[['headlinePortuguese', 'sentimento_modelo1', 'score_modelo1', 'sentimento_modelo2', 'score_modelo2']].head())
        else:
            print("\nNão houve discordância entre os modelos ou apenas um foi executado.")


# -----------------------------------------------------------------------------
# Passo 5: Plotar resultados
# -----------------------------------------------------------------------------

# Configurar um estilo visual mais agradável para os gráficos
sns.set_style("whitegrid")
plt.rcParams['font.family'] = 'sans-serif' # Garante uma fonte padrão consistente

if coluna_sentimento_ativa:
    # --- Plotagem dos Resultados ---

    # 1. Gráfico Geral de Sentimentos sobre Bolsonaro
    print("\n--- Visualização: Sentimento Geral sobre Bolsonaro ---")
    plt.figure(figsize=(8, 6))
    # Usar value_counts() diretamente para obter as contagens por categoria
    sentimento_counts = df_bolsonaro[coluna_sentimento_ativa].value_counts()
    
    # Definir uma ordem preferencial para as categorias e cores consistentes
    ordem_sentimentos = ['Positivo', 'Neutro', 'Negativo']
    cores_sentimentos = {'Positivo': 'green', 'Neutro': 'lightgray', 'Negativo': 'red'}
    
    # Filtrar para categorias presentes e reordenar
    sentimento_counts = sentimento_counts.reindex(ordem_sentimentos).dropna()
    
    sns.barplot(x=sentimento_counts.index, y=sentimento_counts.values, palette=[cores_sentimentos.get(s, 'blue') for s in sentimento_counts.index])
    plt.title(f'Distribuição Geral de Sentimentos sobre Bolsonaro\n(Modelo: {coluna_sentimento_ativa})', fontsize=14)
    plt.ylabel('Número de Manchetes', fontsize=12)
    plt.xlabel('Sentimento', fontsize=12)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    # Adicionar os valores no topo das barras
    for i, v in enumerate(sentimento_counts.values):
        plt.text(i, v + (sentimento_counts.values.max()*0.01), str(v), color='black', ha='center', va='bottom', fontsize=10)
    plt.tight_layout() # Ajusta o layout para evitar sobreposição
    plt.show()

    # 2. Gráfico de Sentimento Predominante por Site (mostrando a distribuição percentual)
    print("\n--- Visualização: Distribuição Percentual de Sentimentos sobre Bolsonaro por Site ---")
    
    # Calcular a distribuição percentual de sentimentos por site
    sentimento_por_site_percentual = df_bolsonaro.groupby('website')[coluna_sentimento_ativa].value_counts(normalize=True).mul(100).unstack(fill_value=0)
    
    # Reordenar colunas para consistência (Positivo, Neutro, Negativo)
    sentimento_por_site_percentual = sentimento_por_site_percentual.reindex(columns=ordem_sentimentos, fill_value=0)

    if not sentimento_por_site_percentual.empty:
        sentimento_por_site_percentual.plot(kind='bar', stacked=True, figsize=(14, 8), 
                                            color=[cores_sentimentos.get(s, 'blue') for s in sentimento_por_site_percentual.columns])
        plt.title(f'Distribuição Percentual de Sentimentos sobre Bolsonaro por Site\n(Modelo: {coluna_sentimento_ativa})', fontsize=16)
        plt.ylabel('Percentual de Manchetes (%)', fontsize=12)
        plt.xlabel('Website', fontsize=12)
        plt.xticks(rotation=45, ha='right', fontsize=10)
        plt.yticks(fontsize=10)
        plt.legend(title='Sentimento', bbox_to_anchor=(1.02, 1), loc='upper left', fontsize=10)
        plt.tight_layout(rect=[0, 0, 0.85, 1]) # Ajustar layout para dar espaço à legenda
        plt.show()
        
        # Para mostrar o "maior sentimento por site" de forma tabular, podemos fazer:
        maior_sentimento_por_site = sentimento_por_site_percentual.idxmax(axis=1)
        contagem_total_por_site = df_bolsonaro.groupby('website')[coluna_sentimento_ativa].count()
        
        resultado_maior_sentimento = pd.DataFrame({
            'Maior_Sentimento': maior_sentimento_por_site,
            'Percentual_Maior_Sentimento': sentimento_por_site_percentual.max(axis=1).round(2),
            'Total_Manchetes_Bolsonaro': contagem_total_por_site
        })
        print("\n--- Sentimento Predominante sobre Bolsonaro por Site (com base no maior percentual) ---")
        print(resultado_maior_sentimento.sort_values(by='Total_Manchetes_Bolsonaro', ascending=False))

    else:
        print("Não há dados suficientes para gerar o gráfico de sentimento por site.")

else:
    print("\nPlotagem não realizada pois nenhuma coluna de sentimento ativa foi definida (provavelmente devido a erro no carregamento ou aplicação dos modelos).")