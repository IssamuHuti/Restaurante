import os

def limpar():
    os.system('cls')

limpar()
print('GASTOS MENSAIS DO RESTAURANTE')

gastos_variaveis = {}
gastos_fixos = {}
tipo_gasto = input('Informe se o gasto é Fixo (F) ou Variável (V): ')
while True:
    while tipo_gasto.upper() != 'F' and tipo_gasto.upper() != 'V':
        limpar()
        print('Digite somente (F) ou (V)')
        tipo_gasto = input('Informe se o gasto é Fixo (F) ou Variável (V): ')

    if tipo_gasto.upper() == 'F':
        gasto_fixo = input('Gasto fixo: ')
        valor_gasto_fixo = input('R$ ')
        gastos_fixos.update({gasto_fixo: int(valor_gasto_fixo)})
        limpar()
    elif tipo_gasto.upper() == 'V':
        gasto_variavel = input('Gasto variavel: ')
        valor_gasto_variavel = input('R$ ')
        gastos_variaveis.update({gasto_variavel: int(valor_gasto_variavel)})
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

total_gasto_fixo = sum(gastos_fixos.values())
total_gasto_variavel = sum(gastos_variaveis.values())

print(f'O total dos gastos fixos foram: {total_gasto_fixo} reais.')
print(f'O total dos gastos variávies foram: {total_gasto_variavel} reais.')