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
estoque_mantimentos_combinados = defaultdict(int)

estoque_mantimentos = {}
for arquivo_estoque_mantimento in os.listdir(pasta_estoque_mantimentos):
    if arquivo_estoque_mantimento.endswith('.json'):
        caminho_arquivo = os.path.join(pasta_estoque_mantimentos, arquivo_estoque_mantimento)
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo_estoque_mantimento:
            dados = json.load(arquivo_estoque_mantimento)
            estoques_itens = dados.get("Estoque_mantimento", {})
            for item, qtd_mantimento in estoques_itens.items():
                estoque_mantimentos_combinados[item] += qtd_mantimento

arquivo_estoque_dia = 'estoque_dia_{}.json'.format(str(data_formatada))
caminho_arquivo_combinado = os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Estoque', arquivo_estoque_dia))
with open(caminho_arquivo_combinado, 'w', encoding='utf8') as arquivo_estoque_combinada:
    json.dump(
            dict(estoque_mantimentos_combinados),
            arquivo_estoque_combinada,
            ensure_ascii=False,
            indent=4
        )

estoque_bebidas = {}

pasta_estoque = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Estoque')
os.makedirs(pasta_estoque, exist_ok=True)

for elemento, qtd in dict(estoque_mantimentos_combinados).items():
    print(elemento, qtd)