import os
import json
from datetime import datetime
from util import limpar, data_dia

limpar()
data_compra = data_dia()
print('Data da compra: ', data_compra)

print('Informe os gastos com mantimentos do dia')

produtos = {}
qtd_produtos = {}

while True:
    produto = input('Produto: ')
    if produto.strip():
        break
    else:
        print('Informe um produto')
while True:
    preco = input('R$ ')
    try:
        numero = int(preco)
        break
    except ValueError:
        try:
            numero = float(preco)
            break
        except ValueError:
            print('Entrada inválida, digite somente números')
produtos.update({produto: float(preco)})
while True:
    qtd_produto = input('Quantidade: ')
    try:
        numero = int(qtd_produto)
        break
    except ValueError:
        try:
            numero = float(qtd_produto)
            break
        except ValueError:
            print('Entrada inválida, digite somente números')
while True:
    und_medida = input('Medida: ')
    if und_medida.strip():
            break
    else:
        print('Informe o produto')
produto_med = {'Qtd': int(qtd_produto), 'Medida': und_medida}
qtd_produtos.update({produto: produto_med})

total_gasto_produtos = round(sum(produtos.values()), 2)

arquivo_matimentos = {'Data': data_compra, 'Total de gasto': total_gasto_produtos, 'Produtos': produtos}
estoque_mantimentos = {'Data': data_compra, 'Estoque_mantimento': qtd_produtos}
# acrescentar unidade de medida em estoque_mantimentos

pasta_salva_gastos = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'compra_mantimentos', 'gastos')
pasta_salva_estoque = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'compra_mantimentos', 'estoque')
os.makedirs(pasta_salva_gastos, exist_ok=True)
os.makedirs(pasta_salva_estoque, exist_ok=True)

compra_mantimentos_dia = os.path.join(pasta_salva_gastos, 'compra_mantimentos_{}.json'.format(data_compra))
compra_mantimentos_estoque = os.path.join(pasta_salva_estoque, 'estoque_mantimentos_{}.json'.format(data_compra))

limpar()
with open(compra_mantimentos_dia, 'w', encoding='utf8') as arquivo:
    json.dump(
        arquivo_matimentos,
        arquivo,
        ensure_ascii=False,
        indent=2,
    )

with open(compra_mantimentos_estoque, 'w', encoding='utf8') as arquivo:
    json.dump(
        estoque_mantimentos,
        arquivo,
        ensure_ascii=False,
        indent=2,
    )

for detalhe, mais_detalhe in arquivo_matimentos.items():
    print(detalhe, mais_detalhe)
    if type(mais_detalhe) == dict:
        for i, j in mais_detalhe.items():
            print('- ', i, j)
    