import os
import json
from datetime import datetime
from collections import defaultdict

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

while True:
    limpar()
    while True:
        venda_item = input('Prato: ')
        if verificar_prato(venda_item):
            break
        else:
            print('Informe um item que está no cardápio')
    qtd_prato = input('Quantidade vendida: ')

    # verificar se possui estoque de mantimentos suficiente para produzir a quantidade de pratos pedidos
    # 1 - criar um caminho para acessar os itens dentro do cardápio por prato
    # 2 - criar um caminho para puxar os itens no estoque
    # 3 - fazer a comparação entre o estoque e a quantidade de insumos utilizados
    
    with open(caminho_cardapio, 'r', encoding='utf8') as arquivo_cardapio:
        dados_cardapio = json.load(arquivo_cardapio)

    mantimentos_usadas = {}
    for prato, ingredientes in dados_cardapio.items():
        if venda_item == prato:
            for ingrediente, quantidade in ingredientes.items():
                ingredientes_usadas = int(quantidade['Medida']) * int(qtd_prato)
                print(f'- {ingrediente}: {ingredientes_usadas} {quantidade['Unidade']}')
                mantimentos_usadas.update({ingrediente: {'Qtd': ingredientes_usadas, 'Medida': quantidade['Unidade']}})

    caminho_estoque = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'estoque')
    retirada_estoque = defaultdict(lambda: {'Qtd': 0, 'Medida': ''})
    arquivos_json = [arq for arq in os.listdir(caminho_estoque) if arq.endswith('.json')]
    if arquivos_json:
        arquivo_mais_recente = max(arquivos_json, key=lambda arq: os.path.getatime(os.path.join(caminho_estoque, arq)))
    caminho_estoque_arquivo = os.path.join(caminho_estoque, arquivo_mais_recente)
    with open(caminho_estoque_arquivo, 'r', encoding='utf8') as arquivo_estoque:
        dados_estoque = json.load(arquivo_estoque)
        estoques_mantimentos = dados_estoque.get('Mantimentos', {})
        for mantimento, qtd_mantimento in mantimentos_usadas.items():
            if mantimento in estoques_mantimentos:
                retirada_estoque[mantimento]['Qtd'] += estoques_mantimentos[mantimento]['Qtd']
                if mantimentos_usadas[mantimento]['Qtd'] <= estoques_mantimentos[mantimento]['Qtd']:
                    retirada_estoque[mantimento]['Qtd'] -= int(ingredientes[mantimento]['Medida'])
                    estoques_mantimentos[mantimento]['Qtd'] = retirada_estoque[mantimento]['Qtd']
                else:
                    pode_produzir = retirada_estoque[mantimento]['Qtd']
                    print(f'Mantimentos suficientes para produzir {pode_produzir} pratos')
                    for prato, ingredientes2 in dados_cardapio.items(): # atualizar a quantia de ingredientes que será usada
                        if venda_item == prato:
                            for ingrediente, quantidade in ingredientes2.items():
                                ingredientes_usadas2 = int(quantidade['Medida']) * pode_produzir
                                mantimentos_usadas.update({ingrediente: {'Qtd': ingredientes_usadas2, 'Medida': quantidade['Unidade']}})
                    retirada_estoque[mantimento]['Qtd'] -= int(mantimentos_usadas[mantimento]['Qtd'])
                    estoques_mantimentos[mantimento]['Qtd'] -= pode_produzir
            elif mantimento not in mantimentos_usadas[ingrediente]:
                limpar()
                print('Ingrediente inexistente no estoque')
                break

    venda_duplicada(venda_item, int(qtd_prato))

    mais_venda = input('Teve outros itens vendidos? Sim (S) Não (N) ')
    if mais_venda.upper() == 'S':
        continue
    elif mais_venda.upper() == 'N':
        break
    while mais_venda.upper() != 'S' and mais_venda.upper() != 'N':
        print('Digite somente "S" ou "N"')
        mais_venda = input('Teve outros itens vendidos? Sim (S) Não (N) ')

# atualização do estoque


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

