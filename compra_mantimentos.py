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
und_medida = input('Medida: ') # adicionar unidade de medida dentro da biblioteca
produto_med = {'Qtd': int(qtd_produto), 'Medida': und_medida}
qtd_produtos.update({produto: produto_med})
while True:
    limpar()
    produto = input('Produto: ')
    if produto == 'pare':
        break
    preco = input('R$ ')
    produtos.update({produto: float(preco)})
    qtd_produto = input('Quantidade: ')
    und_medida = input('Medida: ') # adicionar unidade de medida dentro da biblioteca
    produto_med = {'Qtd': int(qtd_produto), 'Medida': und_medida.upper()}
    qtd_produtos.update({produto: produto_med})

total_gasto_produtos = round(sum(produtos.values()), 2)

arquivo_matimentos = {'Data': data_formatada, 'Total de gasto': total_gasto_produtos, 'Produtos': produtos}
estoque_mantimentos = {'Data': data_formatada, 'Estoque_mantimento': qtd_produtos}
# acrescentar unidade de medida em estoque_mantimentos

pasta_salva_gastos = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'compra_mantimentos', 'gastos')
pasta_salva_estoque = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'compra_mantimentos', 'estoque')
os.makedirs(pasta_salva_gastos, exist_ok=True)
os.makedirs(pasta_salva_estoque, exist_ok=True)

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
    print(detalhe, mais_detalhe)
    if type(mais_detalhe) == dict:
        for i, j in mais_detalhe.items():
            print('- ', i, j)
    