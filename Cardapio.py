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

caminho_cardapio_pasta = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cardapio')
os.makedirs(caminho_cardapio_pasta, exist_ok=True)

while True:
    if cadastrar_vizualizar_cardapio.upper() == 'C':
        card = os.path.join(caminho_cardapio_pasta, 'cardapio.json')
        if os.path.exists(card):
            with open(card, 'r', encoding='utf8') as arquivo:
                try:
                    cardapios = json.load(arquivo)
                except:
                    cardapios = {}
        else:
            cardapios = {}

        while True:
            novo_prato = input('Informe o nome do novo prato (ou "pare" para finalizar): ')
            if novo_prato.lower() == 'pare':
                break

            ingredientes = {}
            limpar()
            print(novo_prato)
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
            
            cardapios[novo_prato] = ingredientes

            limpar()
            mais_um_prato = input('Deseja cadastrar mais um prato? Sim (S) Não (N): ')
            while mais_um_prato.upper() != 'S' and mais_um_prato.upper() != 'N':
                print('Informe Sim (S) ou Não (N)')
                mais_um_prato = input('Deseja cadastrar mais um prato? Sim (S) Não (N): ')
            if mais_um_prato.upper() == 'S':
                limpar()
                continue
            else:
                break

        composicao_prato()

        with open(card, 'w', encoding='utf8') as arquivo:
            json.dump(
                cardapios,
                arquivo,
                ensure_ascii=False,
                indent=2,
            )

    caminho_cardapio_arquivo = os.path.join(caminho_cardapio_pasta, 'cardapio.json')
    if cadastrar_vizualizar_cardapio.upper() == 'V':
        with open(caminho_cardapio_arquivo, 'r', encoding='utf8') as arquivo_cardapio:
            dados_cardapio = json.load(arquivo_cardapio)
            for pr, ings in dados_cardapio.items():            
                print(pr)
                for ing, md in ings.items():
                    print(f'- {ing}:', end=' ')
                    mds = list(md.values())
                    for i in range(0, len(mds), 2):
                        print(f'{mds[0]} {mds[1]}')
                print()
        
        retirada_prato = input('Deseja retirar algum prato do cardápio? Sim(S) Não(N) ')
        while retirada_prato.upper() != 'S' and retirada_prato.upper() != 'N':
            print('Digite "S" ou "N"')
            retirada_prato = input('Deseja retirar algum prato do cardápio? Sim(S) Não(N) ')
        if retirada_prato.upper() == 'S':
            prato_a_retirar = input('Escolha o prato que será retirado: ')
            if prato_a_retirar in dados_cardapio:
                del dados_cardapio[prato_a_retirar]
                print(f'{prato_a_retirar} foi retirado do cardápio!') # não foi retirado o prato
            else:
                print(f'O prato digitado não foi encontrada no cardápio')
        elif retirada_prato.upper() == 'N':
            break

    fechar_cardapio = input('Deseja fechar o cardápio? Sim(S) Não(N)')
    while fechar_cardapio.upper() != 'S' and fechar_cardapio.upper() != 'N':
        print('Digite "S" ou "N"')
        fechar_cardapio = input('Deseja fechar o cardápio? Sim(S) Não(N)')
    if fechar_cardapio == 'S':
        break
    else:
        continue
