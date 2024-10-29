import os
from datetime import datetime

def limpar():
    os.system('cls')

def data_dia():
    data_compra = datetime.now()
    data_formatada = data_compra.strftime('%d_%m_%Y')
    return data_formatada

caminho_cardapio_pasta = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cardapio')
caminho_estoque = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'estoque')
caminho_compra_mantimentos = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'compra_mantimentos')