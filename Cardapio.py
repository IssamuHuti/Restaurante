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
    medida_ingrediente = {'Medida': medida, 'Unidade': unidade}
    return insira_ingrediente, medida_ingrediente

def obter_ingrediente():
    ingrediente, medida = ingrediente_usado()
    return ingrediente, medida

def composicao_prato():
    print(f'Prato: {novo_prato}')
    for ingrediente, medidas in ingredientes.items():   
        print(f'{ingrediente}: {medidas}')

limpar()

print('Cardápio do restaurante')

cadastrar_vizualizar_cardapio = input('Deseja cadastrar (C) novo prato ou visualizar (V) o cardápio? ')
while cadastrar_vizualizar_cardapio.upper() != 'C' and cadastrar_vizualizar_cardapio.upper() != 'V':
    print('Informe (C) ou (V)')
    cadastrar_vizualizar_cardapio = input('Deseja cadastrar (C) novo prato ou visualizar (V) o cardápio? ')
    if cadastrar_vizualizar_cardapio.upper() == 'C':
        limpar()
        continue
    else:
        break

caminho_cardapio_json = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cardapio')

if cadastrar_vizualizar_cardapio.upper() == 'C':
    pratos = {}
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
        
        pratos.update({novo_prato: ingredientes})

        limpar()
        mais_um_prato = input('Deseja cadastrar mais um prato? Sim (S) Não (N)')
        while mais_um_prato.upper() != 'S' and mais_um_prato.upper() != 'N':
            print('Informe Sim (S) ou Não (N)')
            mais_um_prato = input('Deseja cadastrar mais um prato? Sim (S) Não (N): ')
        if mais_um_prato.upper() == 'S':
            limpar()
            continue
        else:
            break

    composicao_prato()

    pasta_cardapio = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cardapio')
    os.makedirs(pasta_cardapio, exist_ok=True)

    card = os.path.join(pasta_cardapio, 'cardapio.json')

    with open(card, 'w', encoding='utf8') as arquivo:
        json.dump(
            pratos,
            arquivo,
            ensure_ascii=False,
            indent=2,
        )

if cadastrar_vizualizar_cardapio.upper() == 'V':
    with open(caminho_cardapio_json, 'r', encoding='utf8') as arquivo_cardapio:
        dados_cardapio = json.load(arquivo_cardapio)
        print(dados_cardapio)
