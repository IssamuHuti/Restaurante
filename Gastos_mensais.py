import os

def limpar():
    os.system('cls')

limpar()
print('Gastos mensais do restaurante\n')

tipo_gasto = input('Informe se o gasto é Fixo (F) ou Variável (V): ')
while True:
    while tipo_gasto.upper() != 'F' and tipo_gasto.upper() != 'V':
        limpar()
        print('Digite somente (F) ou (V)')
        tipo_gasto = input('Informe se o gasto é Fixo (F) ou Variável (V): ')

    gastos_variaveis = {}
    gastos_fixos = {}
    if tipo_gasto.upper() == 'F':
        gasto_fixo = input('Gasto fixo: ')
        valor_gasto_fixo = input('R$ ')
        gastos_fixos.update({gasto_fixo: valor_gasto_fixo})
        limpar()
    elif tipo_gasto.upper() == 'V':
        gasto_variavel = input('Gasto variavel: ')
        valor_gasto_variavel = input('R$ ')
        gastos_variaveis.update({gasto_variavel: valor_gasto_variavel})
        limpar()
    
    incluir = input('Deseja incluir mais gastos? Sim (S) ou Não (N) ')
    while incluir != 'S' and incluir != 'N':
        limpar()
        print('Digite somente (S) ou (N)')
        incluir = input('Deseja incluir mais gastos? Sim (S) ou Não (N)  ')
    if incluir.upper() == 'S':
        tipo_gasto = input('Informe se o gasto é Fixo (F) ou Variável (V): ')
    else:
        break
