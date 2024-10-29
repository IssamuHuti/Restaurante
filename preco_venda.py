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
