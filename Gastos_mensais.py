import os
import json
from datetime import datetime

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

# precisa puxar todas as compras das pastas compra_mantimentos e compras_bebidas
with open('compra_mantimentos.json', 'r', encoding='utf8') as arquivo:
    arquivo_matimentos = json.load(arquivo)
total_mantimentos = arquivo_matimentos['Total de gasto']

with open('compra_bebidas.json', 'r', encoding='utf8') as arquivo:
    arquivo_bebidas = json.load(arquivo)
total_bebidas = arquivo_bebidas['Total de gasto']

data_lista()
print(f'O total dos gastos fixos foram: {total_gasto_fixo:.2f} reais.')
print(f'O total dos gastos variávies foram: {total_gasto_variavel:.2f} reais.')
print(f'O total dos gastos com bebidas foram: {total_bebidas:.2f} reais.')
print(f'O total dos gastos com mantimentos foram: {total_mantimentos:.2f} reais.')
