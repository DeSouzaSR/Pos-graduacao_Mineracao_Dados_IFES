# Textos

* Text Mining: processo de extração de informações úteis de textos não estruturados.
* Mineração de dados estrutrados e não estruturados.
  * Estrutuados: números, datas, categorias.
  * Não estruturados: textos, imagens, vídeos, áudios.
* Conceito de texto:
  * stopwords: palavras que não trazem informação relevante para o texto, como artigos, preposições, conjunções.
  * tokenização: processo de dividir um texto em palavras, frases ou parágrafos.
  * lematização: processo de reduzir uma palavra à sua forma base ou raiz.
  * Bigramas: sequência de duas palavras consecutivas em um texto.
  * Trigramas: sequência de três palavras consecutivas em um texto.
  * stematização: processo de reduzir uma palavra à sua forma base ou raiz, levando em consideração o contexto da frase. A diferença entre lematização e stematização é que a lematização considera o contexto da frase, enquanto a stematização não considera o contexto. Faz mais sentido usar em uma língua como o inglês, onde a flexão é mais simples. Em português, a lematização é mais adequada.

Em Python, podemos usar:

* NLTK: Natural Language Toolkit, biblioteca para processamento de linguagem natural: pode ser usada para tokenização, lematização, stematização, análise de sentimentos, entre outros.
* Spacy: biblioteca para processamento de linguagem natural, mais rápida e eficiente que o NLTK, mas com menos recursos. Pode ser usada para tokenização, lematização, análise de sentimentos, entre outros.
* transformers: biblioteca para processamento de linguagem natural, desenvolvida pela Hugging Face, que permite o uso de modelos pré-treinados para tarefas de NLP, como classificação de texto, tradução, resumo, entre outros. É mais voltada para deep learning e modelos baseados em transformers.
* wordcloud: biblioteca para criar nuvens de palavras a partir de textos. Pode ser usada para visualizar a frequência de palavras em um texto.
* scikit-learn: biblioteca para aprendizado de máquina, que pode ser usada para tarefas de NLP, como classificação de texto, clustering, entre outros. Possui funções para pré-processamento de textos, como remoção de stopwords, tokenização, lematização, entre outros. Vetoriza textos via Bag of Words, TF-IDF, entre outros.

Tedências recentes:

* Grandes modelos de linguagem (LLMs): modelos de deep learning que podem gerar texto, traduzir, resumir, entre outros. Exemplos: GPT-3, BERT, T5.
* PLN em Multi-Modalidade: modelos que podem lidar com diferentes tipos de dados, como texto, imagem e áudio. Exemplos: CLIP, DALL-E.
* Foco no multilíngue: modelos que podem lidar com diferentes idiomas, como mBERT, XLM-R.
