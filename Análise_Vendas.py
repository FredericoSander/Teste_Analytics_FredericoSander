import pandas as pd
import numpy as np

dataclean = "F:\Git\Teste_Analytics_FredericoSander/dataclean.csv"

df = pd.read_csv(dataclean)

print(f"Imprimir as primeira linhas do Dataframe para ter uma noção da estrutura.")
print(df.head())
print()
print('Verificar os tipos de dados do Dataframe')
print(df.info())

print()
print(f'Calcular o total de vendas por produto.')
df['Valor total'] = df['Quantidade']*df['Preço'] # Cria uma nova coluna no dataframe chamada valor vendido
vendas_por_produto = df.groupby(['Produto']).agg({'Valor total': 'sum'})
Agrupar_vendas_por_produto = vendas_por_produto.sort_values('Valor total', ascending=False)
print(Agrupar_vendas_por_produto)

print()
print('Agrupando dados por Produtos')
Agrupar_por_quantidade = df.groupby(['Produto']).agg({'Quantidade': 'sum'})
Agrupar = Agrupar_por_quantidade.sort_values('Quantidade', ascending=False)
print(Agrupar)