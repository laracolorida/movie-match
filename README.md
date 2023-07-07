# Movie Match

## Sistema Inteligente de Recomendação de Filmes com Matrix Factorization e KNN

### Introdução
Com a crescente oferta e disponibilidade de conteúdos midiáticos atualmente, encontrar um conteúdo correspondente aos seus interesses pode ser uma tarefa desafiadora para os usuários. Nesse cenário, os sistemas de recomendação desempenham um papel crucial ao filtrar e fornecer sugestões personalizadas aos usuários, ajudando-os a descobrir conteúdos interessantes, considerando seus históricos de avaliação e preferências individuais. Partindo dessa premissa, o presente trabalho explora a construção de um sistema inteligente de recomendação de filmes utilizando os métodos Matrix Factorization e KNN.

### Metodologia
Nesse projeto foram utilizados os métodos SVD, SDV++, NMF, KNN Basic, KNN With Means, KNN Baseline e KNN WithZ-Score da biblioteca Surprise. O dataset utilizado foi o MovieLens 1M, construído pela GroupLens Research, da Universidade de Minnesota, que contém 1M de avaliações coletadas de usuários reais, com 6000 usuários e 4000 filmes. Utilizamos o RMSE como métrica de análise.

### Conclusão
A análise dos resultados revelou que tanto o SVD++ quanto o KNN Baseline apresentaram desempenhos semelhantes em termos de precisão na geração de recomendações ao se analisar os resultados do RMSE referente a cada um deles. Com base nos resultados obtidos, podemos concluir que ambos são algoritmos de recomendação eficazes, capazes de fornecer recomendações personalizadas aos usuários.<br>
<div align=center><img src="https://github.com/laracolorida/movie-match/blob/main/imagens/rmse.png"></div><br>
É importante ressaltar que, apesar dos resultados promissores, este estudo possui algumas limitações. Dentre elas, destacam-se as restrições de hardware, o que acarretou na ausência de de um dataset atual, pois devido a isso os dataset mais recentes do MovieLens não puderam ser utilizados, tendo em vista que as versões mais recentes possuem mais dados e por consequência exigindo maior poder computacional, resultando na utilização do MovieLens 1M que possui filme até o ano de 2003. 
Encorajamos que pesquisas futuras explorem outras abordagens e considerem a combinação de múltiplos algoritmos, além de uma abordagem que utilize deep learning para melhorar ainda mais a qualidade das recomendações em sistemas de recomendação.

### Artigo 
O artigo produzido a partir desse experimento está disponível na pasta docs do repositório.
