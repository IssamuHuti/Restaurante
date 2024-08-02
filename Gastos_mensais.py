import os

def limpar():
    os.system('cls')

limpar()
print('GASTOS MENSAIS DO RESTAURANTE')

gastos_variaveis = {}
gastos_fixos = {}
gastos_bebidas = {}
gastos_alimentos = {}
tipo_gasto = input('Informe se o gasto é Fixo (F), Variável (V), Bebida (B) ou Alimento (A): ')
while True:
    while tipo_gasto.upper() != 'F' and tipo_gasto.upper() != 'V':
        limpar()
        print('Digite somente (F), (V), (B) ou (A)')
        tipo_gasto = input('Informe se o gasto é Fixo (F), Variável (V), Bebida (B) ou Alimento (A): ')

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
    elif tipo_gasto.upper() == 'A':
        gasto_alimento = input('Gasto com alimento: ')
        valor_gasto_alimento = input('R$ ')
        gastos_alimentos.update({gasto_alimento: float(valor_gasto_alimento)})
        limpar()
    
    incluir = input('Deseja incluir mais gastos? Sim (S) ou Não (N) ')
    while incluir.upper() != 'S' and incluir.upper() != 'N':
        limpar()
        print('Digite somente (S) ou (N)')
        incluir = input('Deseja incluir mais gastos? Sim (S) ou Não (N)  ')
    if incluir.upper() == 'S':
        limpar()
        tipo_gasto = input('Informe se o gasto é Fixo (F), Variável (V), Bebida (B) ou Alimento (A): ')
    else:
        break

total_gasto_fixo = sum(gastos_fixos.values())
total_gasto_variavel = sum(gastos_variaveis.values())
total_gasto_bebida = sum(gastos_bebidas.values())
total_gasto_alimento = sum(gastos_alimentos.values())

print(f'O total dos gastos fixos foram: {total_gasto_fixo:.2f} reais.')
print(f'O total dos gastos variávies foram: {total_gasto_variavel:.2f} reais.')
print(f'O total dos gastos com bebidas foram: {total_gasto_bebida:.2f} reais.')
print(f'O total dos gastos com alimentos foram: {total_gasto_alimento:.2f} reais.')
