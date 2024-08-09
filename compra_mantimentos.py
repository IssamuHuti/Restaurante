import os
import json
from datetime import datetime

def limpar():
    os.system('cls')

limpar()
data_compra = datetime.now()
data_formatada = data_compra.strftime('%d/%m/%Y')
print('Data da compra: ', data_formatada)

print('Informe os gastos com mantimentos do dia')

produtos = {}

produto = input('Produto: ')
preco = input('R$ ')
produtos.update({produto: preco})
while True:
    limpar()
    produto = input('Produto: ')
    if produto == 'pare':
        break
    preco = input('R$ ')
    produtos.update({produto: preco})

arquivo_matimentos = {'Data': data_formatada, 'Produtos': produtos}
limpar()
with open('compra_mantimentos.json', 'w', encoding='utf8') as arquivo:
    json.dump(
        arquivo_matimentos,
        arquivo,
        ensure_ascii=False,
        indent=2,
    )

print(produtos)