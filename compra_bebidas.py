import os
from util import limpar, data_dia
import json
from datetime import datetime

limpar()
data_compra = data_dia()
print('Data da compra: ', data_compra)

print('Informe os gastos com bebidas do dia')

bebidas = {}
qtd_bebidas = {}

while True:
    bebida = input('Produto: ')
    if bebida.strip():
        break
    else:
        print('Informe uma bebida')
while bebida.lower() != 'pare':
    while True:
        preco_bebida = input('R$ ')
        try:
            numero = int(preco_bebida)
            break
        except ValueError:
            try:
                numero = float(preco_bebida)
                break
            except ValueError:
                print('Entrada inválida, digite somente números')
    bebidas.update({bebida: float(preco_bebida)})
    while True:
        qtd_bebida = input('Quantidade: ')
        try:
            numero = int(qtd_bebida)
            break
        except ValueError:
            try:
                numero = float(qtd_bebida)
                break
            except ValueError:
                print('Entrada inválida, digite somente números')
    qtd_bebidas.update({bebida: int(qtd_bebida)})
    limpar()
    while True:
        bebida = input('Produto: ')
        if bebida.strip():
            break
        else:
            print('Informe uma bebida')

total_gasto_bebidas = round(sum(bebidas.values()), 2)

arquivo_bebidas = {'Data': data_compra, 'Total de gasto': total_gasto_bebidas, 'Produtos': bebidas}
estoque_bebidas = {'Data': data_compra, 'Estoque_bebida': qtd_bebidas}

pasta_salva_gastos = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'compra_bebidas', 'gastos')
pasta_salva_estoque = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'compra_bebidas', 'estoque')
os.makedirs(pasta_salva_gastos, exist_ok=True)
os.makedirs(pasta_salva_estoque, exist_ok=True)

compra_bebida_dia = os.path.join(pasta_salva_gastos, 'compra_bebida_{}.json'.format(data_compra))
compra_bebida_estoque = os.path.join(pasta_salva_estoque, 'estoque_bebida_{}.json'.format(data_compra))

limpar()
with open(compra_bebida_dia, 'w', encoding='utf8') as arquivo:
    json.dump(
        arquivo_bebidas,
        arquivo,
        ensure_ascii=False,
        indent=2,
    )

with open(compra_bebida_estoque, 'w', encoding='utf8') as arquivo:
    json.dump(
        estoque_bebidas,
        arquivo,
        ensure_ascii=False,
        indent=2,
    )

for detalhe, mais_detalhe in arquivo_bebidas.items():
    if type(mais_detalhe) == dict:
        for i, j in mais_detalhe.items():
            print('- ', i, j)
    print(detalhe, mais_detalhe)