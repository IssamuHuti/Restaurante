import os

def limpar():
    os.system('cls')

def ingrediente_usado():
    insira_ingrediente = input('Insira ingrediente para o prato: ')
    medida_ingrediente = input('Medida do ingrediente: ')
    ingredientes.update({insira_ingrediente: int(medida_ingrediente)})
    limpar()

def obter_ingrediente():
    i, _ = ingrediente_usado()
    return i

limpar()

print('Cardápio do restaurante')
pratos = []
while True:
    novo_prato = input('Informe o nome do novo prato: ')
    ingredientes = {}
    ingrediente_usado()
    while obter_ingrediente != 'pare':
        ingrediente_usado()
    print(novo_prato)
    for ingrediente in ingredientes:
        print(ingrediente.items())
    