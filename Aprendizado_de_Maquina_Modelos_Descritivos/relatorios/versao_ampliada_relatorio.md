## Relatório Final: Modelo de Segmentação de Clientes em Shopping Center

**1. Introdução**

Este relatório apresenta as conclusões de um exercício de clustering destinado à segmentação de clientes de um shopping center. O objetivo principal deste estudo foi praticar a interpretação de modelos de dados agrupados, reconhecendo que a dificuldade reside em entender os resultados sem uma variável de destino predefinida. A análise explorou diversas alternativas para interpretar os clusters formados após o treinamento de um modelo K-Means, visando fornecer *insights de negócios* valiosos a partir dos resultados obtidos.

**2. Metodologia**

A metodologia adotada neste estudo envolveu as seguintes etapas principais:

*   **Importação de Módulos:** As bibliotecas pandas, numpy, matplotlib, seaborn e scipy.stats foram importadas para manipulação de dados, cálculos numéricos e visualização. Adicionalmente, a biblioteca scikit-learn foi utilizada para transformação de dados (PowerTransformer, MinMaxScaler, PCA), modelagem de clustering (KMeans) e avaliação (silhouette\_score, classification\_report, confusion\_matrix, DecisionTreeClassifier, tree).
*   **Leitura e Inspeção da Base de Dados:** O dataset "segmentation\_data.csv" foi carregado utilizando pandas. A função `.sample(5)` exibiu uma amostra dos dados. A forma do dataset foi verificada, constatando-se que continha 2000 registros e 8 colunas. Um dicionário de dados descreveu cada variável, incluindo seu tipo e faixa de valores.
*   **Análise Exploratória de Dados (EDA):**
    *   **Informações Gerais e Estatísticas Descritivas:** Os métodos `.info()` e `.describe()` foram utilizados para entender os tipos de dados, a estrutura geral e obter estatísticas descritivas das variáveis. As colunas categóricas foram convertidas para o tipo string para facilitar a análise descritiva. Foi confirmado que **não havia valores faltantes** no dataset.
    *   **Distribuição das Variáveis Numéricas:** Histograms revelaram que as variáveis 'ID', 'Age' e 'Income' apresentavam distribuições distintas. 'ID' mostrou uma distribuição uniforme (sendo descartado posteriormente), enquanto 'Age' e 'Income' exibiram uma **assimetria à direita**.
    *   **Distribuição das Variáveis Categóricas:** Gráficos de contagem indicaram um equilíbrio entre gêneros e status marital. A maioria dos clientes possuía ensino médio. As categorias de ocupação e tamanho do assentamento apresentaram uma distribuição razoável.
    *   **Análise Bivariada:**
        *   A relação entre 'Age' e 'Income' foi investigada através de um gráfico de dispersão e do cálculo do coeficiente de correlação de Pearson, revelando uma **pequena correlação positiva** entre elas. A análise segmentada por gênero manteve essa baixa correlação.
        *   A comparação entre variáveis categóricas e numéricas utilizando gráficos de densidade (kdeplot) revelou tendências como: pessoas casadas tendem a ser mais velhas, maior nível educacional está associado a faixas etárias intermediárias e maior renda, e homens parecem ter uma distribuição de renda mais elevada.
        *   A relação entre variáveis categóricas foi explorada com gráficos de contagem, mostrando associações como: mulheres tendem a ser casadas com mais frequência, pessoas casadas possuem maior concentração nos níveis médio e superior de educação, e homens tendem a ser empregados com mais frequência.
    *   **Análise Multivariada:** Gráficos de dispersão (scatterplot) de 'Age' vs 'Income' segmentados por variáveis categóricas aprofundaram a análise, confirmando a influência da educação e ocupação na renda e indicando uma maior distribuição de renda em faixas superiores para pessoas casadas e residentes em cidades maiores.
    *   **Conclusão da Análise Bivariada e Multivariada:** A análise revelou padrões demográficos, de emprego, educação e suas interações com a renda, sugerindo a importância de fatores socioeconômicos e geográficos na segmentação de clientes.
*   **Transformação e Dimensionamento de Atributos:**
    *   **Teste de Normalidade:** Testes de normalidade (normaltest do scipy.stats) confirmaram que 'Income' e 'Age' **não seguiam uma distribuição normal**, com p-values extremamente baixos.
    *   **Transformação dos Dados:** Foram aplicadas transformações logarítmica e PowerTransformer (Box-Cox ou Yeo-Johnson) para tentar aproximar as distribuições de 'Income' e 'Age' da normalidade. Embora ambas as transformações tenham reduzido a assimetria, os testes de normalidade ainda indicaram não normalidade.
    *   **Transformações Definitivas:** As colunas transformadas ('transf\_income' usando PowerTransformer e 'transf\_age' usando log) foram adicionadas ao DataFrame `customer_info`, e as colunas originais 'Income', 'Age' e 'ID' foram descartadas, criando o DataFrame `customer_transformed`.
    *   **Escala de Atributos:** O MinMaxScaler foi utilizado para escalar todos os atributos no intervalo de 0 a 1, equiparando a escala das variáveis numéricas transformadas às variáveis categóricas codificadas (0 ou 1). Essa etapa é crucial para o algoritmo K-Means, que se baseia em medidas de distância.
*   **Modelos de Clusterização (K-Means):**
    *   **Seleção do Número de Clusters:**
        *   **Método Elbow:** A inércia (soma das distâncias quadradas dos pontos ao centroide de seu cluster) foi calculada para um intervalo de números de clusters (2 a 18). O gráfico do método Elbow sugeriu que o "cotovelo" ocorria em torno de 6-7 clusters.
        *   **Silhouette Scores:** O Silhouette Score foi calculado para diferentes números de clusters (2 a 19) e várias sementes aleatórias. Um heatmap visualizou os resultados, indicando que **k = 7 apresentou alguns dos maiores Silhouette Scores médios**, sugerindo uma boa separação dos clusters. **k = 6 também mostrou bons valores**. A decisão foi de testar modelos com 6 e 7 clusters.
    *   **Aplicação do K-Means com 6 Clusters:** O algoritmo K-Means foi executado com 6 clusters.
    *   **Visualização dos Resultados com PCA:** A técnica de Análise de Componentes Principais (PCA) foi aplicada para reduzir a dimensionalidade dos dados para 3 componentes principais (X1, X2, X3), facilitando a visualização dos clusters em um espaço tridimensional. Gráficos de dispersão 2D e 3D mostraram uma **boa separação visual entre os 6 clusters formados**.
*   **Interpretação dos Clusters:**
    *   **Estatísticas Resumidas por Cluster:** O método `.describe()` foi aplicado a cada um dos 6 clusters para obter estatísticas descritivas (média, mediana, desvio padrão, mínimo, máximo, quartis) para cada variável. Essa análise forneceu uma visão geral das características de cada grupo de clientes. As conclusões parciais para cada cluster foram as seguintes:
        *   **Cluster 0:** Mulheres, não solteiras com renda média, geralmente empregadas, vivendo em cidades médias e grandes.
        *   **Cluster 3:** Homens, não solteiros, idade variando de 20 a 40 anos, predominantemente com ensino médio, renda em torno de 100000, empregado, trabalhando em cidades dos três portes.
        *   **Cluster 1:** Homens, solteiros, com idade em torno de 36 anos, majoritariamente com ensino médio ou sem educação, salário em torno de 100000, principalmente não empregados, mas com alguns empregados.
        *   **Cluster 2:** Mulheres, solteiras, com idade bem distribuída, predominantemente com ensino médio, com renda bem distribuída em torno de 100000, predominantemente desempregadas e vivendo em cidades pequenas.
        *   **Cluster 4:** Mulheres casadas, relativamente jovens, predominantemente com ensino médio ou superior, com renda bem centrada em torno de 100000, ou desempregadas ou com cargos gerenciais ou autônomas, vivendo em cidades pequenas.
        *   **Cluster 5:** Homens, solteiros, com idade variando bastante, predominantemente com ensino médio, mas também alguns sem ensino e outros com curso superior, renda, em média, um pouco mais alta, empregados em sua maioria, mas também autônomos ou gerentes. Eles vivem em cidades médias a grandes.
    *   **Uso de Centroides de Cluster:** Os centroides de cada cluster foram calculados e apresentados como uma medida de tendência central para uma rápida visão geral dos valores médios de cada variável em cada cluster. No entanto, o documento ressalta que esse método pode ser incompleto devido à influência de outliers.
    *   **Árvore de Decisão para Interpretação de Clusters:** Uma Árvore de Decisão (DecisionTreeClassifier) foi treinada para prever os rótulos dos clusters com base nas variáveis originais. A alta precisão do modelo (próxima de 1.00 para a maioria dos clusters no relatório de classificação) indicou que a árvore conseguiu capturar bem as características distintivas de cada grupo. A visualização da árvore de decisão (limitada no documento) forneceu *regras claras baseadas nas variáveis mais importantes* para distinguir os clusters.

**3. Resultados e Conclusões Baseadas na Árvore de Decisão**

A Árvore de Decisão se mostrou uma ferramenta eficaz para interpretar os clusters, fornecendo regras simples para caracterizar cada segmento de clientes. As conclusões principais, baseadas na estrutura da árvore (conforme parcialmente visível no documento), são:

*   **Cluster 5:** Caracterizado inicialmente por clientes solteiros (Marital status <= 0.5) e vivendo em cidades médias ou grandes (Settlement size > 0.5). Dentro desse grupo, uma subdivisão importante ocorre pelo sexo (Sex <= 0.5), separando provavelmente homens solteiros vivendo em cidades maiores.
*   **Cluster 1:** Dentro do grupo de solteiros (Marital status <= 0.5) vivendo em cidades pequenas (Settlement size <= 0.5), o sexo (Sex <= 0.5) novamente se mostra um fator de separação, direcionando para este cluster. Uma subdivisão adicional por ocupação (Occupation <= 1.5) refina ainda mais a definição deste grupo, possivelmente indicando homens solteiros não empregados ou empregados em certas categorias, vivendo em cidades pequenas.
*   **Cluster 2:** Dentro do grupo de solteiros, vivendo em cidades pequenas e sendo do sexo feminino (Sex > 0.5 após o primeiro nó), uma subdivisão por ocupação (Occupation <= 1.5 e Occupation > 1.5) leva a este cluster, sugerindo mulheres solteiras em ocupações específicas vivendo em cidades pequenas.
*   **Cluster 4:** Caracterizado inicialmente por clientes não solteiros (Marital status > 0.5). Uma divisão subsequente pelo sexo (Sex <= 0.5) direciona para este cluster, indicando mulheres não solteiras. Uma nova divisão por ocupação (Occupation <= 1.5) dentro deste grupo define ainda mais as características deste cluster, possivelmente mulheres casadas ou não solteiras, com certas categorias de ocupação.
*   **Cluster 0:** Dentro do grupo de não solteiros (Marital status > 0.5), a divisão por sexo (Sex > 0.5) leva a este cluster, indicando homens não solteiros. Uma divisão posterior por tamanho do assentamento (Settlement size <= 0.5) e ocupação (Occupation <= 0.5) refina a definição, sugerindo homens não solteiros vivendo em cidades pequenas e possivelmente desempregados.
*   **Cluster 3:** A árvore de decisão também identifica um caminho que leva diretamente ao Cluster 3, embora os nós específicos que o definem não estejam totalmente visíveis na captura de tela fornecida. A análise das estatísticas descritivas sugere que este cluster é composto por homens não solteiros, com idade entre 20 e 40 anos, predominantemente com ensino médio, renda em torno de 100000, empregados e vivendo em cidades de todos os tamanhos.

Em resumo, a análise de clustering utilizando o algoritmo K-Means, complementada pela interpretação através de estatísticas descritivas e, principalmente, por uma Árvore de Decisão, permitiu a identificação de seis distintos segmentos de clientes. As características mais relevantes para a segmentação incluem **estado civil, tamanho do assentamento, sexo e ocupação**.

**4. Aplicações**

O notebook original menciona a sugestão de aplicações das metodologias aplicadas na Secretaria de Educação do Espírito Santo. Embora o documento fornecido não explore essas aplicações, a metodologia de segmentação de clientes pode ser adaptada para diversas finalidades na área da educação, como:

*   Segmentar alunos com base em características socioeconômicas, desempenho acadêmico ou necessidades educacionais específicas para direcionar intervenções e recursos de forma mais eficaz.
*   Identificar perfis de evasão escolar para implementar estratégias de retenção direcionadas.
*   Agrupar escolas com características semelhantes para comparar resultados e identificar boas práticas.

A aplicação direta dos clusters identificados neste estudo específico (baseado em clientes de um shopping center) para a Secretaria de Educação exigiria uma adaptação do modelo com dados relevantes do contexto educacional.