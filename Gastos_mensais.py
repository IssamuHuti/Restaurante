import os
import json
from datetime import datetime
from collections import defaultdict

def limpar():
    os.system('cls')

def data_lista():
    data_compra = datetime.now()
    data_formatada = data_compra.strftime('%m/%Y')
    print('Gasto do mês:', data_formatada)

limpar()
print('GASTOS MENSAIS DO RESTAURANTE')
data_lista()

print()

total_gastos = {}
gastos_categoria = {}
gastos_variaveis = {}
gastos_fixos = {}
tipo_gasto = input('Informe se o gasto é Fixo (F) ou Variável (V): ')

while True:
    while tipo_gasto.upper() != 'F' and tipo_gasto.upper() != 'V':
        limpar()
        print('Digite somente (F) ou (V)')
        tipo_gasto = input('Informe se o gasto é Fixo (F) ou Variável (V): ')

    limpar()

    if tipo_gasto.upper() == 'F':
        gasto_fixo = input('Gasto fixo: ')
        valor_gasto_fixo = input('R$ ')
        gastos_fixos.update({gasto_fixo: float(valor_gasto_fixo)})
        limpar()
    elif tipo_gasto.upper() == 'V':
        gasto_variavel = input('Gasto variavel: ')
        valor_gasto_variavel = input('R$ ')
        gastos_variaveis.update({gasto_variavel: float(valor_gasto_variavel)})
        limpar()
    
    incluir = input('Deseja incluir mais gastos? Sim (S) ou Não (N) ')
    while incluir.upper() != 'S' and incluir.upper() != 'N':
        limpar()
        print('Digite somente (S) ou (N)')
        incluir = input('Deseja incluir mais gastos? Sim (S) ou Não (N)  ')
    if incluir.upper() == 'S':
        limpar()
        tipo_gasto = input('Informe se o gasto é Fixo (F) ou Variável (V): ')
    else:
        break

total_gasto_fixo = round(sum(gastos_fixos.values()), 2)
total_gasto_variavel = round(sum(gastos_variaveis.values()), 2)
total_gastos['Gastos_fixos'] = total_gasto_fixo
total_gastos['Gastos_variaveis'] = total_gasto_variavel

gastos_categoria.update({'Gastos fixos': gastos_fixos})
gastos_categoria.update({'Gastos variáveis': gastos_variaveis})

dados_gasto_mes = {'Total de gasto':total_gastos, 'Gastos por categoria':gastos_categoria}

with open('gasto_mensal.json', 'w', encoding='utf8') as arquivo:
    json.dump(
        dados_gasto_mes,
        arquivo,
        ensure_ascii=False,
        indent=3,
    )

pasta_compra_mantimentos = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'compra_mantimentos', 'gastos')
compras_mantimentos_combinados = defaultdict(float)

for arquivo_compra_mantimento in os.listdir(pasta_compra_mantimentos):
    if arquivo_compra_mantimento.endswith('.json'):
        caminho_arquivo = os.path.join(pasta_compra_mantimentos, arquivo_compra_mantimento)
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
            compras = dados.get("Produtos", {})
            for item, valor in compras.items():
                compras_mantimentos_combinados[item] += valor

total_mantimentos = round(sum(compras_mantimentos_combinados.values()), 2)

pasta_compra_bebidas = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'compra_bebidas', 'gastos')
compras_bebidas_combinados = defaultdict(float)

for arquivo_compra_bebida in os.listdir(pasta_compra_bebidas):
    if arquivo_compra_bebida.endswith('.json'):
        caminho_arquivo = os.path.join(pasta_compra_bebidas, arquivo_compra_bebida)
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
            compras = dados.get("Produtos", {})
            for item, valor in compras.items():
                compras_bebidas_combinados[item] += valor

total_bebidas = round(sum(compras_bebidas_combinados.values()), 2)

data_lista()
print(f'O total dos gastos fixos foram: {total_gasto_fixo:.2f} reais.')
print(f'O total dos gastos variávies foram: {total_gasto_variavel:.2f} reais.')
print(f'O total dos gastos com bebidas foram: {total_bebidas:.2f} reais.')
print(f'O total dos gastos com mantimentos foram: {total_mantimentos:.2f} reais.')
