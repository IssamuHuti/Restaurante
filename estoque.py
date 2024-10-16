import os
from util import limpar, data_dia
import json
from collections import defaultdict

limpar()
data_compra = data_dia()
print('Data da compra: ', data_compra)

pasta_estoque_mantimentos = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'compra_mantimentos', 'estoque')
estoque_mantimentos_combinados = defaultdict(lambda: {'Qtd': 0, 'Medida': ''})

mantimento_combinados_medidas = {}
for arquivo_estoque_mantimento in os.listdir(pasta_estoque_mantimentos):
    if arquivo_estoque_mantimento.endswith('.json'):
        caminho_arquivo_mantimento = os.path.join(pasta_estoque_mantimentos, arquivo_estoque_mantimento)
        with open(caminho_arquivo_mantimento, 'r', encoding='utf8') as arquivo_estoque_mantimento:
            dados = json.load(arquivo_estoque_mantimento)
            estoques_itens_mantimentos = dados.get("Estoque_mantimento", {})
            for item, qtd_mantimento in estoques_itens_mantimentos.items():
                estoque_detalhado = estoque_mantimentos_combinados[item]['Medida']
                if estoque_detalhado == qtd_mantimento['Medida'] or not estoque_detalhado:
                    if qtd_mantimento['Medida'].upper() == 'L':
                        estoque_mantimentos_combinados[item]['Qtd'] += qtd_mantimento['Qtd'] * 1000
                        estoque_detalhado = 'ML'
                    elif qtd_mantimento['Medida'].upper() == 'KG':
                        estoque_mantimentos_combinados[item]['Qtd'] += qtd_mantimento['Qtd'] * 1000
                        estoque_detalhado = 'G'
                    else:
                        estoque_mantimentos_combinados[item]['Qtd'] += qtd_mantimento['Qtd']
                        estoque_detalhado = qtd_mantimento['Medida'].upper()

pasta_estoque_bebidas = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'compra_bebidas', 'estoque')
estoque_bebidas_combinados = defaultdict(int)

for arquivo_estoque_bebida in os.listdir(pasta_estoque_bebidas):
    if arquivo_estoque_bebida.endswith('.json'):
        caminho_arquivo_bebidas = os.path.join(pasta_estoque_bebidas, arquivo_estoque_bebida)
        with open(caminho_arquivo_bebidas, 'r', encoding='utf8') as arquivo_estoque_bebida:
            dados = json.load(arquivo_estoque_bebida)
            estoques_itens_bebidas = dados.get("Estoque_bebida", {})
            for item, qtd_bebida in estoques_itens_bebidas.items():
                estoque_bebidas_combinados[item] += qtd_bebida

estoque_combinados = {"Mantimentos": dict(estoque_mantimentos_combinados),
                      "Bebidas": dict(estoque_bebidas_combinados)}
arquivo_estoque_dia = 'estoque_dia_{}.json'.format(data_compra)
caminho_arquivo_combinado = os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Estoque', arquivo_estoque_dia))
with open(caminho_arquivo_combinado, 'w', encoding='utf8') as arquivo_estoque_combinada:
    json.dump(
            estoque_combinados,
            arquivo_estoque_combinada,
            ensure_ascii=False,
            indent=4
        )

pasta_estoque = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Estoque')
os.makedirs(pasta_estoque, exist_ok=True)


for elemento, quantidade in estoque_combinados.items():
    print(elemento)
    if elemento == 'Mantimentos':
        for qtd, medida in quantidade.items():
            print(f'- {qtd}:', end=' ')
            for qt, med in medida.items():
                print(f'{med}', end=' ')
            print()
        print()
    else:
        for qtd, medida in quantidade.items():
            print(f'- {qtd}: {medida}')
        print()

