-- Para manipular o dataset criado no Mysql foi necessário cria uma banco de dados para importar os dados.
-- Criação do banco de dados Teste_Analytics.

create Database Teste_Analytics;

-- Comando para utilização do banco de dados criado.
use Teste_Analytics;

-- Após a criação do banco de dados foi relizada a importação da base de dados dataclean.csv.
-- Consulta da base dados recém importada.
select * from dataclean;

-- Consulta criada para retonar a listagem de produtos categorias e a soma total das vendas em ordem decrescente.
-- Por meio do comando Select foi selecionado as colunas produto e categoria do banco de dados.
-- A comando SUM() realiza o somatório do produto obtido pela multiplicação da quantidade pelo preço par obter a soma total das vendas.
-- o resultado é retornado em uma colnua como Valor_total.
-- A comando FROM indica em qual tabela as informações serão extraídas paraa consulta.
-- A comando Group By agrega todos os produtos e categoria em grupos de dados que são comuns,
-- neste cenário elimina duplicidade de produtos e categorias consolidando as informações.
-- A comando Order By está ordenando a consulta pelo Valor_total de forma descrescente dos maiores para os menores valores.

select produto,categoria, SUM(Quantidade * Preço) as Valor_Total
from dataclean
group by produto,categoria
order by Valor_total desc;

-- Para realizar a consulta que permite identificar os produto que menos venderam em junho de 20244, foi necessário atualizar o campo de data,
-- que estava com o tipo de dados String para o tipo de dados data.
-- A comando a serguir atualiza os valores do campo data que se encontram no formato de texto para o formato data.
UPDATE dataclean
set Data = str_to_date(data, '%Y-%m-%d');

-- Por meio do comando Select foram selecionado as colunas produto e quantidade do banco de dados.
-- O comando FROM indica em qual tabela as informações serão extraídas paraa consulta.
-- O comando where informa que na coluna data será aplicada a restrição imposta pelo comando BETWEEN que é o intervalo na qual a consulta será aplicada.
-- o comando Order By está ordenando a consulta pelo Quantidade de forma crescente dos menores para os maiores valores, 
-- possibilitando verificar quais produtos venderam menos.

select Data,produto,Quantidade, Quantidade * Preço as Valor_Total 
from dataclean
where Data BETWEEN '2023-06-01' AND'2023-06-30'
order by Quantidade;


