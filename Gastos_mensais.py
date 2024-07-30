import os

def limpar():
    os.system('cls')

print('Gastos mensais do restaurante\n')

tipo_gasto = input('Informe se o gasto é Fixo (F) ou Variável (V): ')
while tipo_gasto.upper() != 'F' and tipo_gasto.upper() != 'V':
    print('Digite somente (F) ou (V)')
    limpar()
    tipo_gasto = input('Informe se o gasto é Fixo (F) ou Variável (V): ')

gastos_variaveis = {}
gastos_fixox = {}
if tipo_gasto.upper() == 'F':
    gasto_fixo = input('Gasto fixo: ')
    valor_gasto_fixo = input()
    limpar()
elif tipo_gasto.upper() == 'V':
    gasto_variavel = input('Gasto fixo: ')
    valor_gasto_variavel = input()
    limpar()

