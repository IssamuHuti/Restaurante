import os
import json
from util import limpar, caminho_estoque, caminho_cardapio_pasta, caminho_compra_mantimentos

limpar()

gastos_matimentos = os.path.join(caminho_compra_mantimentos, 'gastos')
for arquivo_gastos in os.listdir(gastos_matimentos):
    if arquivo_gastos.endswith('.json'):
        caminho_arquivo__gastos_mantimento = os.path.join(gastos_matimentos, arquivo_gastos)
        with open(caminho_arquivo__gastos_mantimento, 'r', encoding='utf8') as arquivo_gasto_mantimento:
            dados = json.load(arquivo_gasto_mantimento)
            gastos_itens_mantimentos = dados.get("Produtos", {})
            for item, gasto in gastos_itens_mantimentos.items():
                print(item, gasto)

for arquivo_estoque in os.listdir(caminho_estoque):
    if arquivo_estoque.endswith('.json'):
        caminho_arquivo__estoque_mantimento = os.path.join(caminho_estoque, arquivo_estoque)
        with open(caminho_arquivo__estoque_mantimento, 'r', encoding='utf8') as arquivo_estoque_mantimento:
            dados = json.load(arquivo_estoque_mantimento)
            estoque_itens_mantimentos = dados.get("Mantimentos", {})
            for item, estoque in estoque_itens_mantimentos.items():
                print(item, estoque)
