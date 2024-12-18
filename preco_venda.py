import os
import json
from util import limpar, caminho_estoque, caminho_cardapio_pasta, caminho_compra_mantimentos, caminho_gastos_mensais, permissao_int
from collections import defaultdict

limpar()

gastos_item = {}
gastos_matimentos = os.path.join(caminho_compra_mantimentos, 'gastos')
soma_gastos_mantimentos = defaultdict(float)
for arquivo_gastos in os.listdir(gastos_matimentos):
    if arquivo_gastos.endswith('.json'):
        caminho_arquivo__gastos_mantimento = os.path.join(gastos_matimentos, arquivo_gastos)
        with open(caminho_arquivo__gastos_mantimento, 'r', encoding='utf8') as arquivo_gasto_mantimento:
            dados_gastos = json.load(arquivo_gasto_mantimento)
            gastos_itens_mantimentos = dados_gastos.get("Produtos", {})
            for item, gasto in gastos_itens_mantimentos.items():
                soma_gastos_mantimentos[item] += gasto
                if item not in gastos_item:
                    gastos_item.update(soma_gastos_mantimentos)
                else:
                    gastos_item[item] = soma_gastos_mantimentos
                # print(item, soma_gastos_mantimentos[item])

for arquivo_estoque in os.listdir(caminho_estoque):
    if arquivo_estoque.endswith('.json'):
        caminho_arquivo__estoque_mantimento = os.path.join(caminho_estoque, arquivo_estoque)
        with open(caminho_arquivo__estoque_mantimento, 'r', encoding='utf8') as arquivo_estoque_mantimento:
            dados = json.load(arquivo_estoque_mantimento)
            estoque_itens_mantimentos = dados.get("Mantimentos", {})
            # for item, estoque in estoque_itens_mantimentos.items():
            #     print(item, estoque)

proporcao_gasto = {}
for i, _ in estoque_itens_mantimentos.items():
    proporcao = gastos_item[i] / estoque_itens_mantimentos[i]['Qtd']
    proporcao_gasto.update({i: round(proporcao, 4)})

# for i, j in proporcao_gasto.items():
#     print(i, j)

custo_prato = {}
for arquivos_cardapio in os.listdir(caminho_cardapio_pasta):
    if arquivos_cardapio.endswith('.json'):
        caminho_arquivo_cardapio = os.path.join(caminho_cardapio_pasta, arquivos_cardapio)
        with open(caminho_arquivo_cardapio, 'r', encoding='utf8') as arquivo_cardapio:
            dados_cardapio = json.load(arquivo_cardapio)
            for prato, ingredientes in dados_cardapio.items():
                # print(prato, ingredientes)
                custo_por_prato = 0
                for ingrediente, medida in ingredientes.items():
                    if ingrediente in estoque_itens_mantimentos:
                        custo_por_prato += int(medida['Medida']) * proporcao_gasto[ingrediente]
                    else:
                        custo_por_prato = 0
                        break
                if custo_por_prato == 0:
                    custo_prato.update({prato: 'Não disponivel'})
                else:
                    custo_prato.update({prato: round(custo_por_prato, 2)})

print('Custo por prato com mantimentos')
for prato, custo in custo_prato.items():
    if type(custo) == int or type(custo) == float:
        print(prato + ': ' + str(round(custo, 3)))
    else:
        print(prato + ': ' + custo)

print()
for arquivo_despesas_gerais in os.listdir(caminho_gastos_mensais):
    if arquivo_despesas_gerais.endswith('.json'):
        caminho_gasto_mes = os.path.join(caminho_gastos_mensais, arquivo_despesas_gerais)
        with open(caminho_gasto_mes, 'r', encoding='utf8') as arquivo_gasto_mensal:
            dados_gastos_mensais = json.load(arquivo_gasto_mensal)
            gastos_mensais = dados_gastos_mensais.get("Total_de_gasto", {})
            total_despesas = 0
            for tipo_gasto, valor_gasto in gastos_mensais.items():
                total_despesas += valor_gasto
            # print(round(total_despesas, 2))

proporcao_despesas_gerais = len(custo_prato)
for i in custo_prato.values():
    if i == 'Não disponivel':
        proporcao_despesas_gerais -= 1

distribuicao_prato = total_despesas / proporcao_despesas_gerais

print(distribuicao_prato)

print()
print('Estimativa de venda de prato por mês')
estimativa_venda = {}
for prato, _ in custo_prato.items():
    estimativa_produto = (f'Estimativa de venda {prato}: ')
    estimativa_venda.update({prato: int(estimativa_produto)})

print()
print('Custo por prato')
custo_total_prato = {}
for prato, estimativa in estimativa_venda.items():
    if custo_prato[prato] != 'Não disponivel':
        estimativa_prato = distribuicao_prato / estimativa + float(custo_prato[prato])
        custo_total_prato.update({prato: float(estimativa_prato)})

for prato, custo_prato_total in custo_total_prato.items():
    print(f'{prato}: {round(custo_prato_total, 2)}')


alavancagem = float(permissao_int('Por quantas vezes a mais do custo praneja vender? '))
preco_venda = {}
for prato, custo_prato_total in custo_total_prato.items():
    preco_alavancado = custo_prato_total * alavancagem
    preco_venda.update({prato: preco_alavancado})

for prato, preco_prato in preco_venda.items():
    print(f'{prato}: {round(preco_prato, 2)}')
