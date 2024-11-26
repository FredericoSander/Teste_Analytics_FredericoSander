import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataclean = "https://github.com/FredericoSander/Teste_Analytics_FredericoSander/blob/main/Base%20de%20dados/dataclean.csv"

df = pd.read_csv(dataclean)

print(f"Imprimir as primeira linhas do Dataframe para ter uma noção da estrutura.")
print(df.head())

print()

print('Verificar os tipos de dados do Dataframe')
print(df.info())

print()

print(f'Calcular o total de vendas por produto.')
df['Valor_vendido'] = df['Quantidade']*df['Preço']

print()

meses_pt_br = {1:'Janeiro', 2:'Fevereiro', 3:'Março',4:'Abril',5:'Maio', 6:'Junho', 7:'Julho',8:'Agosto',9:'Setembro',10:'Outubro', 11:'Novembro', 12:'Dezembro'}

date_col = pd.DatetimeIndex(df['Data'])
df['Mês'] = date_col.month

df['Mês_nome'] = df['Mês'].replace(meses_pt_br)

df['Mês_nome'] = pd.Categorical(df['Mês_nome'], categories=meses_pt_br.values(), ordered=True)
                                
print()

print('Valor total das vendas por mês')
valor_vendas_por_mes = df.groupby(['Mês_nome']).agg({'Valor_vendido': 'sum'})
Agrupar_valor_vendas_por_mes = valor_vendas_por_mes.sort_values('Mês_nome', ascending=True)
print(Agrupar_valor_vendas_por_mes)

print(f'Gráfico de linhas com o total de vendas por produto.')
Agrupar_valor_vendas_por_mes.plot(kind='line', legend=False)
plt.title('Valor total de vendas por produto')
plt.xlabel('Meses')
plt.ylabel('Valor vendido (R$)')
plt.tight_layout()
plt.show()

print()

print('Quantidade total das vendas por mês')
quantidade_vendas_por_mes = df.groupby(['Mês_nome']).agg({'Quantidade': 'sum'})
Agrupar_quantidade_vendas_por_mes = quantidade_vendas_por_mes.sort_values('Mês_nome', ascending=True)
print(Agrupar_quantidade_vendas_por_mes)

print(f'Gráfico de barras com o total de unidades vendidas')
Agrupar_quantidade_vendas_por_mes.plot(kind='bar', legend=False)
plt.title('Quantidade total unidades vendidas')
plt.xlabel('Meses')
plt.ylabel('Quantidade (Unid.)')
plt.tight_layout()
plt.show()

print('Ticket médio das vendas por mês')
ticket_medio_vendas = (valor_vendas_por_mes['Valor_vendido'] / quantidade_vendas_por_mes['Quantidade'])
ticket_medio_vendas = ticket_medio_vendas.reset_index(name='Ticket_médio')
Agrupar_ticket_medio_vendas= ticket_medio_vendas.sort_values('Mês_nome', ascending=True)
print(Agrupar_ticket_medio_vendas)

print()

print(f'Calcular o total de vendas por produto.')
vendas_por_produto = df.groupby(['Produto']).agg({'Valor_vendido': 'sum'})
Agrupar_vendas_por_produto = vendas_por_produto.sort_values('Valor_vendido', ascending=False)
print(Agrupar_vendas_por_produto)

print(f'Gráfico de barras com o total de vendas por produto.')
Agrupar_vendas_por_produto.plot(kind='bar', legend=False)
plt.title('Total de vendas por produto')
plt.xlabel('Produto')
plt.ylabel('Valor vendido (R$)')
plt.tight_layout()
plt.show()
