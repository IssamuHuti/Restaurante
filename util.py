import os
from datetime import datetime

def limpar():
    os.system('cls')

def data_dia():
    data_compra = datetime.now()
    data_formatada = data_compra.strftime('%d_%m_%Y')
    return data_formatada

def permissao_int(mensagem):
    while True:
        x = input(mensagem)
        if x.isdigit(): 
            return int(x)
        else:
            print("Entrada inválida. Informe apenas números.")

def permissao_str(mensagem):
    while True:
        x = input(mensagem)
        if x.isalpha(): 
            return x
        else:
            print("Entrada inválida. Informe apenas caracteres.")

caminho_cardapio_pasta = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cardapio')
caminho_estoque = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Estoque')
caminho_compra_mantimentos = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'compra_mantimentos')
caminho_gastos_mensais = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gastos_mensais')

