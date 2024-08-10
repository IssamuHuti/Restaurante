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
gastos_bebidas = {}
tipo_gasto = input('Informe se o gasto é Fixo (F), Variável (V) ou Bebida (B): ')

while True:
    while tipo_gasto.upper() != 'F' and tipo_gasto.upper() != 'V' and tipo_gasto.upper() != 'B':
        limpar()
        print('Digite somente (F), (V) ou (B)')
        tipo_gasto = input('Informe se o gasto é Fixo (F), Variável (V) ou Bebida (B): ')

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
    elif tipo_gasto.upper() == 'B':
        gasto_bebida = input('Gasto com bebida: ')
        valor_gasto_bebida = input('R$ ')
        gastos_bebidas.update({gasto_bebida: float(valor_gasto_bebida)})
        limpar()
    
    incluir = input('Deseja incluir mais gastos? Sim (S) ou Não (N) ')
    while incluir.upper() != 'S' and incluir.upper() != 'N':
        limpar()
        print('Digite somente (S) ou (N)')
        incluir = input('Deseja incluir mais gastos? Sim (S) ou Não (N)  ')
    if incluir.upper() == 'S':
        limpar()
        tipo_gasto = input('Informe se o gasto é Fixo (F), Variável (V) ou Bebida (B): ')
    else:
        break

total_gasto_fixo = round(sum(gastos_fixos.values()), 2)
total_gasto_variavel = round(sum(gastos_variaveis.values()), 2)
total_gasto_bebida = round(sum(gastos_bebidas.values()), 2)
total_gastos['Gastos_fixos'] = total_gasto_fixo
total_gastos['Gastos_variaveis'] = total_gasto_variavel
total_gastos['Gastos_bebidas'] = total_gasto_bebida

gastos_categoria.update({'Gastos fixos': gastos_fixos})
gastos_categoria.update({'Gastos variáveis': gastos_variaveis})
gastos_categoria.update({'Gastos bebidas': gastos_bebidas})

dados_gasto_mes = {'Total de gasto':total_gastos, 'Gastos por categoria':gastos_categoria}

with open('gasto_mensal.json', 'w', encoding='utf8') as arquivo:
    json.dump(
        dados_gasto_mes,
        arquivo,
        ensure_ascii=False,
        indent=3,
    )

with open('compra_mantimentos.json', 'r', encoding='utf8') as arquivo:
    arquivo_matimentos = json.load(arquivo)
total = arquivo_matimentos['Total de gasto']

data_lista()
print(f'O total dos gastos fixos foram: {total_gasto_fixo:.2f} reais.')
print(f'O total dos gastos variávies foram: {total_gasto_variavel:.2f} reais.')
print(f'O total dos gastos com bebidas foram: {total_gasto_bebida:.2f} reais.')
print(f'O total dos gastos com mantimentos foram: {total:.2f} reais.')
