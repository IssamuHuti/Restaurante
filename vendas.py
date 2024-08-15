import os
import json
from datetime import datetime

def limpar():
    os.system('cls')

def verificar_prato(venda_prato):
    return venda_prato in cardapio_vendas

limpar()
data_compra = datetime.now()
data_formatada = data_compra.strftime('%d/%m/%Y')
print('Data da compra: ', data_formatada)

print('VENDAS DO DIA')
vendas_pratos = {}
vendas_bebidas = {}

with open('cardapio.json', 'r', encoding='utf8') as arquivo:
    cardapio_vendas = json.load(arquivo)

while True:
    while True:
        venda_prato = input('Prato: ')
        if verificar_prato(venda_prato):
            break
        else:
            print('Informe o prato que está no cardápio')

    qtd_prato = input('Quantidade vendida: ')

    # venda_bebida = input('Bebida: ')
    # while venda_prato not in cardapio_vendas():
    #     print('Informe o prato que está no cardápio')
    #     venda_prato = input('Prato: ')