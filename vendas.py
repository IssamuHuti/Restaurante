import os
import json
from datetime import datetime

def limpar():
    os.system('cls')

def verificar_prato(venda_prato):
    return venda_prato in cardapio_vendas

def venda_duplicada(venda_prato, qtd_prato):
    if venda_prato in vendas_pratos:
        vendas_pratos[venda_prato] += qtd_prato
    else:
        vendas_pratos[venda_prato] = qtd_prato

limpar()
data_compra = datetime.now()
data_formatada = data_compra.strftime('%d_%m_%Y')
print('Data da compra: ', data_formatada)

print('VENDAS DO DIA')
vendas_pratos = {}
vendas_bebidas = {}

caminho_cardapio = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cardapio', 'cardapio.json')
with open(caminho_cardapio, 'r', encoding='utf8') as arquivo:
    cardapio_vendas = json.load(arquivo)

# problema para criar caminho para acessar arquivo json

while True:
    limpar()
    while True:
        venda_item = input('Prato: ')
        if verificar_prato(venda_item):
            break
        else:
            print('Informe um item que está no cardápio')
    qtd_prato = input('Quantidade vendida: ')
    venda_duplicada(venda_item, int(qtd_prato))

    mais_venda = input('Teve outros itens vendidos? Sim (S) Não (N) ')
    if mais_venda.upper() == 'S':
        continue
    elif mais_venda.upper() == 'N':
        break
    while mais_venda.upper() != 'S' and mais_venda.upper() != 'N':
        print('Digite somente "S" ou "N"')
        mais_venda = input('Teve outros itens vendidos? Sim (S) Não (N) ')

print(vendas_pratos)
vendas_dia = {'data': data_formatada, 'Vendas_pratos': vendas_pratos}

pasta_salva = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'vendas_diarias')
os.makedirs(pasta_salva, exist_ok=True)

arquivo_venda_dia = os.path.join(pasta_salva, 'venda_{}.json'.format(str(data_formatada)))
with open(arquivo_venda_dia, 'w', encoding='utf8') as arquivo_json:
    json.dump(
        vendas_dia,
        arquivo_json,
        ensure_ascii=False,
        indent=2,
    )