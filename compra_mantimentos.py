import os
import json
from datetime import datetime

def limpar():
    os.system('cls')

limpar()
data_compra = datetime.now()
data_formatada = data_compra.strftime('%d_%m_%Y')
print('Data da compra: ', data_formatada)

print('Informe os gastos com mantimentos do dia')

produtos = {}
qtd_produtos = {}

produto = input('Produto: ')
preco = input('R$ ')
produtos.update({produto: float(preco)})
qtd_produto = input('Quantidade: ')
preco_unitario_produto = round(float(preco) / int(qtd_produto), 2)
qtd_produtos.update({produto: [qtd_produto, preco_unitario_produto]})
while True:
    limpar()
    produto = input('Produto: ')
    if produto == 'pare':
        break
    preco = input('R$ ')
    produtos.update({produto: float(preco)})
    qtd_produto = input('Quantidade: ')
    preco_unitario_produto = round(float(preco) / int(qtd_produto), 2)
    qtd_produtos.update({produto: [qtd_produto, preco_unitario_produto]})

total_gasto_produtos = round(sum(produtos.values()), 2)

arquivo_matimentos = {'Data': data_formatada, 'Total de gasto': total_gasto_produtos, 'Produtos': produtos}
estoque_mantimentos = {'Data': data_formatada, 'Gasto por mantimento': qtd_produtos}

pasta_salva_gastos = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'compra_mantimentos', 'gastos')
pasta_salva_estoque = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'compra_mantimentos', 'estoque')
os.makedirs(os.path.dirname(os.path.abspath(__file__)), exist_ok=True)

compra_mantimentos_dia = os.path.join(pasta_salva_gastos, 'compra_mantimentos_{}.json'.format(str(data_formatada)))
compra_mantimentos_estoque = os.path.join(pasta_salva_estoque, 'estoque_mantimentos_{}.json'.format(str(data_formatada)))

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
    if type(mais_detalhe) == dict:
        for i, j in mais_detalhe.items():
            print('- ', i, j)
    print(detalhe, mais_detalhe)