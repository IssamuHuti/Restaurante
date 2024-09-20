import os
import json
from datetime import datetime
from collections import defaultdict

def limpar():
    os.system('cls')

limpar()
data_compra = datetime.now()
data_formatada = data_compra.strftime('%d_%m_%Y')
print('Data: ', data_formatada)

pasta_estoque_mantimentos = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'compra_mantimentos', 'estoque')
estoque_mantimentos_combinados = defaultdict(lambda: {'Qtd': 0, 'Medida': ''})

estoque_mantimentos = {}
mantimento_combinados_medidas = {}
for arquivo_estoque_mantimento in os.listdir(pasta_estoque_mantimentos):
    if arquivo_estoque_mantimento.endswith('.json'):
        caminho_arquivo_mantimento = os.path.join(pasta_estoque_mantimentos, arquivo_estoque_mantimento)
        with open(caminho_arquivo_mantimento, 'r', encoding='utf8') as arquivo_estoque_mantimento:
            dados = json.load(arquivo_estoque_mantimento)
            estoques_itens_mantimentos = dados.get("Estoque_mantimento", {})
            for item, qtd_mantimento in estoques_itens_mantimentos.items():
                if estoque_mantimentos_combinados[item]['Medida'] == qtd_mantimento['Medida'] or not estoque_mantimentos_combinados[item]['Medida']:
                    estoque_mantimentos_combinados[item]['Qtd'] += qtd_mantimento['Qtd']
                    estoque_mantimentos_combinados[item]['Medida'] = qtd_mantimento['Medida']
estoque_mantimentos.update(estoque_mantimentos_combinados)

pasta_estoque_bebidas = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'compra_bebidas', 'estoque')
estoque_bebidas_combinados = defaultdict(int)

estoque_bebidas = {}
for arquivo_estoque_bebida in os.listdir(pasta_estoque_bebidas):
    if arquivo_estoque_bebida.endswith('.json'):
        caminho_arquivo_bebidas = os.path.join(pasta_estoque_bebidas, arquivo_estoque_bebida)
        with open(caminho_arquivo_bebidas, 'r', encoding='utf8') as arquivo_estoque_bebida:
            dados = json.load(arquivo_estoque_bebida)
            estoques_itens_bebidas = dados.get("Estoque_bebida", {})
            for item, qtd_bebida in estoques_itens_bebidas.items():
                estoque_bebidas_combinados[item] += qtd_bebida
estoque_bebidas.update(estoque_bebidas_combinados)

estoque_combinados = {"Mantimentos": dict(estoque_mantimentos_combinados), "Bebidas": dict(estoque_bebidas_combinados)}
arquivo_estoque_dia = 'estoque_dia_{}.json'.format(str(data_formatada))
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

for elemento, qtd in estoque_combinados.items():
    print(elemento)
    for q, m in qtd.items():
        print(f'- {q}: {m}')
    print()

unidade_medida = ['ml', 'unid', 'g', 'fls', 'dentes']
convert_medida = {'Kg': '1000 g', 'L': '1000 ml'}