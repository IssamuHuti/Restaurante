import os
import json

def limpar():
    os.system('cls')

def ingrediente_usado():
    insira_ingrediente = input('Insira ingrediente para o prato: ')
    if insira_ingrediente.lower() == 'pare':
        return None, None
    medida_ingrediente = input('Medida do ingrediente: ')
    return insira_ingrediente, medida_ingrediente

def obter_ingrediente():
    ingrediente, medida = ingrediente_usado()
    return ingrediente, medida

limpar()

print('Cardápio do restaurante')
pratos = []
while True:
    novo_prato = input('Informe o nome do novo prato (ou "pare" para finalizar): ')
    if novo_prato.lower() == 'pare':
        break

    ingredientes = {}

    ingrediente, medida = obter_ingrediente()
    if ingrediente is None:
        break
    ingredientes.update({ingrediente: medida})
    while True:
        limpar()
        ingrediente, medida = obter_ingrediente()
        if ingrediente is None:
            break
        ingredientes.update({ingrediente: medida})
    
    pratos.append((novo_prato, ingredientes))

    print(f'Prato: {novo_prato}')
    for ingrediente, medida in ingredientes.items():
        print(f'{ingrediente}: {medida}')
    
    break

with open('cardapio.jason', 'w', encoding='utf8') as arquivo:
    json.dump(
        pratos,
        arquivo,
        ensure_ascii=False,
        indent=2,
    )

