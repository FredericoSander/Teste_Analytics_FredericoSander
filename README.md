# Teste Analytics FredericoSander

## Estrutura do Repositório

Este repositório está divido e três pastas denomidadas, Python, SQL, Base de Dados e Relatório, que contém os arquivos criados na elaboração do projeto Teste Analytics.

- Python: Nesta pasta estão arquivados os script criados em python contendo os códigos de criação do Dataframe, análise exoploratória e análise de vendas.
- SQL: nesta pasta esta armazenado o script das consultas em SQL.
- Base de dados: Nesta pasta está armazenado o arquivo datacleancsv.
- Relatório: Nesta pasta está armazenado o relatório de insights

## Python
A pasta python contém os seguintes arquivos:

- Script.py
- Análise_Vendas.py
- Análise_Exploratória.py

<p align="justify">O arquivo Script.py é o primeiro arquivo que deve ser executado, este foi criado utilizando o Visual Studio Code e o Python 3.12.4.
Para implementação do script e anaálises futuras será necessário a utilização das biblioteca pandas numpy e matiplolib. Este script contém o código e os dados utilizados na criação do DataFrame. Este script ainda contém os códigos para a eliminação de duplicidades e valores nulos. Ao termino da criação do Dataframe e do tratamento dos dados, o dataframe limpo é exportado para um arquivo no formato csv com o nome dataclean.csv.</P>

O arquivo dataclean.csv criado, foi utilizado para realização das consultas em SQL, análise de vendas e análise exploratória.

<p align="justify">O arquivo Análise_Vendas possui um código que realiza o cálculo do total de vendas criando uma lista de produto e a quantidade de itens vendidos por produto.</P>  

<p align="justify">O arquivo Análise_Exploratória, implementa um conjuto de códigos que realizam os cálculos do valor total das vendas e da quantidade de itens vendidos distribuidos por mês, imprimindo um grafico de linhas, para representar do valor total das vendas e um gráfico de barras, para representar as informações das quantidades de itens vendidos por mês. No arquivo, ainda é implementado o cálculo do ticket médio mensal, fornecendo mais detalhes do comportamento das vendas. Por ultimo é implementado o cálculo do valor total das vendas por produto, apresentando os produtos com maior faturamento em ordem decrescente.</P>

## SQL
<p align="justify">O arquivo SQL foi desenvolvido no software MySQL Workbench 8.0. O Script SQL, cria um banco de dados denomidado Teste_Analytics, que utiliza o arquivo dataclean.csv. No Script, ainda são criadas duas consultas, sendo que uma foi implementada para retorna a relação do valor total das vendas para cada produto e suas categorias. A segunda consulta, foi implementada para retornar a quantidade de itens vendidos de cada produto no mês de junho de 2023, possibilitando identificar o produto menos vendido no período selecionado.</P>

## Base de dados
O arquivo dataset.csv criado pelo script.py será abase de dados utilizada na realização das consultas e análise está base já está tratada e sem valore duplicados ou nulos.

## Relatório
<p align="justify">O arquivo relatório insights.pdf contém um relatório com os principais insights encontrados durante a realização das análises contendo as resposta as perguntas realizadas e ainda uma recomendação de pesquisa futuras na base de dados para melhoria dos resultados das vendas.</p>

## Autores
- [Frederico S N Cota](https://github.com/FredericoSander)