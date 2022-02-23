![house_rocket_baner](https://user-images.githubusercontent.com/93053350/155342564-66db52d1-bf4e-4f23-9c75-0364638f55b6.jpg)

![GitHub Release Date](https://img.shields.io/badge/Release%20Date-February%202022-blue?style=plastic)
![GitHub Release Date](https://img.shields.io/badge/Project%20Status-Finished-brightgreen?style=plastic)
![GitHub Release Date](https://img.shields.io/badge/Programming%20Languages-1-blueviolet?style=plastic)

# :house_with_garden: Análise Exploratória de Dados para criar recomendações de compra e revenda de imóveis afim de maximizar o lucro 

<h1>índice</h1>

<h3>
  
• [Questões de Negócio](Questões-de-Negócio)

• [Premissas do Negócio](Premissas-do-Negócio)

• [Planejamento da Solução](Planejamento-da-Solução)

• [Top 7 Insights de Negócio](Top-7-Insights-de-Negócio)

• [Resultados Financeiros para o negócio](Resultados-Financeiros-para-o-negócio)

• [Conclusão](Conclusão)
  
</h3>
<h1>:mag_right: Sobre o projeto</h1>
  <p>Esse é um projeto do tipo Insights que realizei para fazer parte do meu portfólio de projetos de Ciência de Dados. De forma resumida, é uma análise exploratória de dados
  com o intuito de resolver os problemas de negócio e tomada de decisão da empresa fictícia House Rocket.</p>

  <p>A House Rocket é uma plataforma digital que tem como modelo de negócio, a compra e a venda de imóveis usando tecnologia. O ponto central da o problema de negócio
  da House Rocket é a identificação de bons negócios e por qual preço esses imóveis deveriam se revendidos.</p>
  
  <p>O objetivo desse projeto é solucionar o problema de negócio da House Rocket construindo indicações de compra e revenda dos imóveis a partir da análise exploratória
  de dados desenvolver insights que possam ser utilizados pelo time de negócios par amaximizar o lucro e auxiliar na tomada de decisão da empresa.</p>
 
 <h1>:briefcase: Questões de Negócio</h1>
  <p>1. Quais casas o CEO da House Rocket deveria comprar e por qual preço de compra?</p>
    <p>2. Uma vez a casa em posse da empresa, qual o melhor preço da venda?</p>
      <p>3. A House Rocket deveria fazer uma reforma para aumentar o preço da venda? Quais seriam as sugestões de mudanças? Qual o incremento no preço dado por cada opção 
      de reforma?</p>
 
 <h1>:gear: Premissas do Negócio</h1>
  <p>1. Não existe informação sobre a coluna "date" do dataset, então estou assumindo que seja a data que o imóvel ficou disponível para compra no portfólio da empresa.</p>
    <p>2. O custo para construir um porão em um imóvel será considerado de USD $35.000. Segundo o site comozed, o custo varia de USD $12.000 para construções onde o dono do
    imóvel realize grande parte da obra, e chega até USD $35.000 quando uma empreiteira é contratada para realizar a obra por completo, irei utilizar o segundo caso como
    parâmetro já que se trata de um serviço B2B. (fonte: https://comozed.com/quanto-custa-colocar-um-por%C3%A3o-sob-uma-casa-m%C3%B3vel)</p>
 
<h1>:computer: Planejamento da Solução</h1>
  <h3>1. Planejamento de Produto Final</h3>
    <p>1.1 O produto final será um dashboard contendo os gráficos relacionados as hypóteses de negócio e as tabelas de recomendação de compra e venda de imóveis, e um produto 
    de dados aonde o CEO da House Rocket poderá realizar suas próprias análises no dataset a partir de gráficos e tabelas com filtros interativos, dados estatísticos, etc.
    O produto final será colocado em produção na plataforma de Cloud Heroku, e entregue por um link de acesso.</p>
  
<h3>2. Planejamento de Processo</h3>
<p>2.1 Baixar os dados no site Kaggle.</p>
<p>2.2 Limpar os dados encontrando outliers, linhas em branco, dados em formato incorreto, etc.</p>
<p>2.3 Entendimento do negócio, compreender os atributos do dataset, suas correlações e de que maneira a empresa lucra.</p>
<p>2.4 Após o entendimento do negócio, elaborar a tabela de recomenações de compra dos imóveis</p>
<p><ul>2.4.1 Como o preço dos imóveis varia bastante de acordo com a região (que também é um fator que determina sua valorização ou não) os dados serão agrupados de acordo com
  seu zipcode.</ul></p>
<p><ul>2.4.2 Dentro de cada conjunto de dados agrupados pelo seu zipcode, irei encontrar a mediana do preços dos imóveis de cada conjunto.</ul></p>
<p><ul>2.4.3 Consideramos os imóveis com preço abaixo do preço mediano do seu conjunto barato, porém não é interessante adquirir imóveis baratos em más condições, já que
  provavelmente o gasto para reformar seria alto de mais, então irei recomendar a compra dos imóveis que tenham o preço abaixo do  preço mediano do seu conjunto, e que 
  estejam em boas condições.</ul></p>
  <p>2.5 Elaborar a tabela de recomendações de venda dos imóveis.</p>
<p><ul>2.5.1 Dado a variação de preço dos imóveis ao longo do ano, irei elaborar dois cenários de venda.</ul></p>
<p><ul><ul>2.5.1.1 Se no momento o preço do imóvel está acima do preço mediano dos imóveis da região, o imóvel será vendido com uma pequena margem de lucro para não ficar
  tão caro que não consiga ser vendido, será o preço do imóvel + 10%.</ul></ul></p>
<p><ul><ul>2.5.1.2 Se no momento o preço do imóvel estiver abaixo do preço mediano dos imóveis da regão, então a empresa tem maior margem para lucrar já que pagou bem mais
  barato do que o preço que o mercado está exercendo no momento, nesse caso o imóvel será vendido pelo preço pago + 30%.</ul></ul></p>
<p>2.6 Realizar a análise exploratória de dados.</p>
<p>2.7 Elaborar o produto de dados, quais filtros serão utilizados, quais estatísticas descritivas irão conter no produto, definir quais os atributos serão utilizados
  nos filtros e etc.</p>
  <p><ul>2.7.1 O produto será composto por duas tabelas, uma com as médias de alguns atributos do dataset, e outra com as estatísticas descritivas.</ul></p>
  <p><ul>2.7.2 Doas mapas, um irá mostrar a densidade dos imóveis e o outro a densidade do preço de acordo com a região.</ul></p>
  <p><ul>2.7.3 Um gráfico de preço médio de acordo com o ano de construção dos imóveis, e um filtro para selecionar até qual ano o gráfico irá mostrar.</ul></p>
  <p><ul>2.7.4 Um gráfico de preço médio de acordo com os dias do ano e um filtro para selecionar até qual dia do ano o gráfico irá mostrar.</ul></p>
  <p><ul>2.7.5 Um gráfico que mostra a distribuição do preço do imóveis e um filtro para selecionar até qual preço o gráfico irá mostrar.</ul></p>
  <p><ul>2.7.6 Quatro gráficos que irão representar os atributos: quartos, banheiros, pisos e vista para a água e filtros para selecionar até qual quantidade de atributos 
  será filtrado e se o imóvel tem ou não vista para a água.</ul></p>
  <p>2.8 Organizar os códigos em funções e em ETL.</p>
  <p>2.9 Disponibilizar o dashboard e o produto de dados no Streamlit.</p>
  <p>2.10 Realizar o versionamento dos códigos com o Git.</p>
  <p>2.11 Uploadar os dois produtos na Cloud Heroku.</p>
  
  <h3>3. Planejamento de Ferramentas</h3>
  <p>3.1 Anaconda e Jupyter Notebook para análise exploratória de dados.</p>
  <p>3.2 Python e VSCode para as demais etapas de programação.</p>
  <p>3.3 Streamlit Python Framework Web para visualização dos mapas, gráficos, tabelas e filtros.</p>
  <p>3.4 Heroku Cloud para o deploy do modelo.</p>
  
   <h1>:bar_chart: Top 7 Insights de Negócio</h1>
   <p>1. Imóveis com vista para a água são 60% mais caros do que imóveis sem vista para a água na média.</p>
   <p><ul>1.1 A hipótese está validada já que os imóveis com vista para a água são aproximadamente 212% mais caros na média do que imóveis que não possuem vista para 
  água, assim, imóveis em boas condiçoes de compra com vista para a água possuem maior margem para gerar mais lucra para a empresa, já que possuem maior potencial 
  de valorização por seus altos preços.</ul></p>
  
  ![vista_agua](https://user-images.githubusercontent.com/93053350/155401663-8f0536a9-27f2-4c44-9e4b-c9559a2a738f.png)

  
  <p>2. Imóveis antigos (construídos antes de 1955) são 20% mais baratos na média do que imóveis atuais.</p>
  <p><ul>2.1 A hipótese é inválida já que a diferença de preço entre os dois grupo de imóveis é quase nula, o que nos indica que é mais vantajoso comprar imóveis atuais
  pois terão quase o mesmo preço do que os antigos na média e um menor desgaste físico por serem mais novos, gerando menor custo de manutenção.</ul></p>
  
  ![imoveis_antigos](https://user-images.githubusercontent.com/93053350/155401432-f546b0e1-3e31-409a-b4cf-0acaae214b17.png)
  
  <p>3. Imóveis que possuem porão são 20% mais caros na média do que imóveis sem porão.</p>
  <p><ul>3.1 A hipótese é válida, já que imóveis que possuem porão são aproximadamente 28% mais caros do que imóveis que não possuem. A média de preço dos imóveis que não
  possuem porão é de aproximadamente USD $486.000, acrescentando 28% sobre esse preço que seria o novo valor para vende-lo caso tivesse porão, o preço médio desses imóveis
  seria de USD 622.080. O custo total da obra para colocar um porão em um imóvel é de aproximadamente USD $35.000, e o aumento do preço de um imóvel sem porão para um com
  porão é de USD $136.080 na média, o que resultaria em um lucro médio de USD $101.000 por cada venda de imóvel após a reforma para colocar um porão.</ul></p>
  
  ![imoveis_porao](https://user-images.githubusercontent.com/93053350/155402011-c9a6593d-27e1-46c4-8b5a-a618377b8a8f.png)
  
  <p>4. O crescimento Year over Year do preço dos imóveis é de 15%.</p>
  <p><ul>4.1 A hipótese é inválida, o crescimento YoY do preço dos imóveis é praticamente nulo, o preço médio continuou quase o mesmo.</ul></p>
  
 ![YoY](https://user-images.githubusercontent.com/93053350/155402175-f149bcce-a879-4251-84ec-07092557edea.png)
 
 <p>5. O preço médio dos imóveis reformados é 25% mais caro do que o preço médio dos imóveis que nunca foram reformados.</p>
 <p><ul>5.1 A hipótese está validada, imóveis que foram reformados são aproximadamente 43% mais caros na média do que imóveis que não foram reformados. </ul></p>
 
 ![imoveis_reformados](https://user-images.githubusercontent.com/93053350/155402290-ac827b5a-9a7b-4a93-a599-de995fc195bc.png)

<p>6. Imóveis com mais de um piso são 40% mais caros na média do que imóveis que possuem apenas um piso.</p>
<p><ul>6.1 Hipótese validada, imóveis com mais de um piso são aproximadamente 44% mais caros na média do que imóveis que possuem apenas um piso.</ul></p>

![imoveis_1piso](https://user-images.githubusercontent.com/93053350/155402399-599cf49f-e6f9-4923-bfe4-de528203ae9e.png)

<p>7. O crescimento Month Over Month do preço de imóveis com 3 banheiros é de 10%.</p>
<p><ul>7.1 A hipótese é inválida, apenas nos meses de maio de 2014 e fevereiro de 2015 o crescimento MoM do preço do imóveis com 3 banheiros foi acima de 10%.</ul></p>

![MoM](https://user-images.githubusercontent.com/93053350/155402478-175151a3-d3de-4ca5-b6a9-fd10a614dc7b.png)

<p>8. Imóveis com o tamanho da sala de estar acima da média são 30% mais caros do que imóveis com tamanho abaixo da média.</p>
<p><ul>8.1 A hipótese está validada, imóveis com o tamanho da sala de estar acima da média são aproximadamente 89% mais caros do que imóveis com imóveis com tamanho
  da sala de estar abaixo da média.</ul></p>

  ![sala_estar](https://user-images.githubusercontent.com/93053350/155402613-d4926f07-7a80-4729-9d38-f0568b913395.png)

<h1>:chart_with_upwards_trend: Resultados Financeiros para o negócio</h1>
<p>1. A partir dos mais de 21000 imóveis disponíveis no dataset da House Rocket, após fazer a seleção de quais seriam os imóveis recomendados para compra com base no preço
  médio da sua região e nas condiçõesdo imóvel, um pouco mais de 10500 imóveis foram classificados como um bom negócio para a empresa comprar. Considerando que todos os 
  imóveis que foram recomendados para compra sejam comprados e posteriosmente revendidos pelo preço recomendado, a empresa irá gerar uma receita aproximada de USD $13,92bi e 
  um lucro aproximado de USD $840mi. Como não existe informações sobre quantos imóveis a empresa costuma vender ao longo do tempo, não é possível fazer uma estimativa de
  resultados financeiros ao longo do tempo.</p>

<h1>:pushpin: Conclusão</h1>
<p>1. Para concluir, o objtivo inicial deste projeto foi alcançado, as questões de negócio foram resolvidas e insights foram gerados para a empresa. Agora a House Rocket é 
  capaz de montar sua estratégia com base nos dados e identificar de maneira mais acertiva quais são os melhores negócios e bons preços para revendê-los, quais são as melhores
  reformas a serem aplicadas em um imóvel para valoriza-lo afim de maximizar o lucro e utilizar o produto de dados para realizar análises que irão aulixar na tomada de
  decisão.</p>
  <p>Link para acessar os gráficos das hipóteses e as tabelas de recomendação de compra e venda:<br>
  https://house-rocket-insights.herokuapp.com/</br></p>
  
   <p>Link para acessar o produto de dados:<br>
   https://house-rocket-hypoteses.herokuapp.com/</br></p>
