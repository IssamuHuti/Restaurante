import os
import json

def limpar():
    os.system('cls')

def ingrediente_usado():
    insira_ingrediente = input('Insira ingrediente para o prato: ')
    if insira_ingrediente.lower() == 'pare':
        return None, None
    medida = input('Medida do ingrediente: ')
    unidade = input('Unidade de medida: ')
    medida_ingrediente = [medida, unidade]
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

    ingrediente, medidas = obter_ingrediente()
    if ingrediente is None:
        break
    ingredientes.update({ingrediente: medidas})
    while True:
        limpar()
        ingrediente, medidas = obter_ingrediente()
        if ingrediente is None:
            break
        ingredientes.update({ingrediente: medidas})
    
    pratos.append((novo_prato, ingredientes))

    print(f'Prato: {novo_prato}')
    for ingrediente, medidas in ingredientes.items():
        print(f'{ingrediente}: {medidas[0]} {medidas[1]}')
    
    break

with open('cardapio.json', 'w', encoding='utf8') as arquivo:
    json.dump(
        pratos,
        arquivo,
        ensure_ascii=False,
        indent=2,
    )

