import os
import json
from datetime import datetime

def limpar():
    os.system('cls')

limpar()
data_compra = datetime.now()
data_formatada = data_compra.strftime('%d/%m/%Y')
print('Data da compra: ', data_formatada)

print('VENDAS DO DIA')
vendas_pratos = {}
vendas_bebidas = {}

with open('cardapio.json', 'r', encoding='utf8') as arquivo:
    cardapio_vendas = json.load(arquivo)

venda_prato = input('Prato: ')
while venda_prato != cardapio_vendas[0]:
    print('Informe o prato que está no cardápio')
    venda_prato = input('Prato: ')
qtd_prato = input('Quantidade vendida: ')

# venda_bebida = input('Bebida: ')
# while venda_prato not in cardapio_vendas():
#     print('Informe o prato que está no cardápio')
#     venda_prato = input('Prato: ')