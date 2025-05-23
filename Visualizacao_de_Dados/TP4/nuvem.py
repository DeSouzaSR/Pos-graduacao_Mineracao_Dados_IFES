# -*- coding: utf-8 -*-

import pandas as pd
from wordcloud import WordCloud
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
import nltk
import numpy as np
from PIL import Image

# Baixar stopwords em português (executar só 1 vez)
nltk.download('stopwords')


# Usar stopwords em português
stopwords_pt = set(stopwords.words('portuguese'))

# Ler o dataframe
df = pd.read_csv(r'..\..\datasets\brazilian_headlines_sentiments.csv')

# Carregar a imagem que será usada como máscara
mascara = np.array(Image.open(r'../figuras/brasil4.jpg'))

# Concatenar o dataframe, na coluna de textos, em um único texto
text = " ".join(df['headlinePortuguese'])

# Gerar a nuvem com stopwords em português
wordcloud = WordCloud(
    width=2000,
    height=2000,
    random_state=42,
    background_color='white',
    mask=mascara,
    colormap='Reds',
    collocations=False,
    stopwords=stopwords_pt
).generate(text)

# Plotar a nuvem
plt.figure(figsize=(15, 10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
#plt.savefig(r'..\figuras\nuvem_palavras.png', bbox_inches='tight', dpi=300)