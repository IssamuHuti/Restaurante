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
gastos_mantimentos = {}
tipo_gasto = input('Informe se o gasto é Fixo (F), Variável (V), Bebida (B) ou Mantimento (M): ')

while True:
    while tipo_gasto.upper() != 'F' and tipo_gasto.upper() != 'V' and tipo_gasto.upper() != 'B' and tipo_gasto.upper() != 'M':
        limpar()
        print('Digite somente (F), (V), (B) ou (A)')
        tipo_gasto = input('Informe se o gasto é Fixo (F), Variável (V), Bebida (B) ou Mantimento (M): ')

    limpar()

    if tipo_gasto.upper() == 'F':
        gasto_fixo = input('Gasto fixo: ')
        valor_gasto_fixo = input('R$ ')
        gastos_fixos.update({gasto_fixo: float(valor_gasto_fixo)})
        gastos_categoria.update({gasto_fixo: float(valor_gasto_fixo)})
        limpar()
    elif tipo_gasto.upper() == 'V':
        gasto_variavel = input('Gasto variavel: ')
        valor_gasto_variavel = input('R$ ')
        gastos_variaveis.update({gasto_variavel: float(valor_gasto_variavel)})
        gastos_categoria.update({gasto_variavel: float(valor_gasto_variavel)})
        limpar()
    elif tipo_gasto.upper() == 'B':
        gasto_bebida = input('Gasto com bebida: ')
        valor_gasto_bebida = input('R$ ')
        gastos_bebidas.update({gasto_bebida: float(valor_gasto_bebida)})
        gastos_categoria.update({gasto_bebida: float(valor_gasto_bebida)})
        limpar()
    elif tipo_gasto.upper() == 'M':
        gasto_mantimento = input('Gasto com mantimento: ')
        valor_gasto_mantimento = input('R$ ')
        gastos_mantimentos.update({gasto_mantimento: float(valor_gasto_mantimento)})
        gastos_categoria.update({gasto_mantimento: float(valor_gasto_mantimento)})
        limpar()
    
    incluir = input('Deseja incluir mais gastos? Sim (S) ou Não (N) ')
    while incluir.upper() != 'S' and incluir.upper() != 'N':
        limpar()
        print('Digite somente (S) ou (N)')
        incluir = input('Deseja incluir mais gastos? Sim (S) ou Não (N)  ')
    if incluir.upper() == 'S':
        limpar()
        tipo_gasto = input('Informe se o gasto é Fixo (F), Variável (V), Bebida (B) ou Mantimento (M): ')
    else:
        break

total_gasto_fixo = round(sum(gastos_fixos.values()), 2)
total_gasto_variavel = round(sum(gastos_variaveis.values()), 2)
total_gasto_bebida = round(sum(gastos_bebidas.values()), 2)
total_gasto_mantimento = round(sum(gastos_mantimentos.values()), 2)
total_gastos['Gastos_fixos'] = total_gasto_fixo
total_gastos['Gastos_variaveis'] = total_gasto_variavel
total_gastos['Gastos_bebidas'] = total_gasto_bebida
total_gastos['Gastos_mantimentos'] = total_gasto_mantimento

dados_gasto_mes = {'Total de gasto':total_gastos, 'Gastos por categoria':gastos_categoria}

with open('gasto_mensal.json', 'w', encoding='utf8') as arquivo:
    json.dump(
        dados_gasto_mes,
        arquivo,
        ensure_ascii=False,
        indent=3,
    )

data_lista()
print(f'O total dos gastos fixos foram: {total_gasto_fixo:.2f} reais.')
print(f'O total dos gastos variávies foram: {total_gasto_variavel:.2f} reais.')
print(f'O total dos gastos com bebidas foram: {total_gasto_bebida:.2f} reais.')
print(f'O total dos gastos com alimentos foram: {total_gasto_mantimento:.2f} reais.')
