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
estoque_mantimentos_combinados = defaultdict(float)

for arquivo_estoque_mantimento in os.listdir(pasta_estoque_mantimentos):
    if arquivo_estoque_mantimento.endswith('.json'):
        caminho_arquivo = os.path.join(pasta_estoque_mantimentos, arquivo_estoque_mantimento)
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
            estoques_itens = dados.get("Gasto por mantimento", {})
            for item, qtd_mantimento in estoques_itens.items():
                pasta_estoque_mantimentos[item] += qtd_mantimento

estoque_mantimentos = {}
estoque_bebidas = {}

pasta_estoque = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Estoque')
os.makedirs(pasta_estoque, exist_ok=True)
