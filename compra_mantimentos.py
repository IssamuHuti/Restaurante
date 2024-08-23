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

produto = input('Produto: ')
preco = input('R$ ')
produtos.update({produto: float(preco)})
while True:
    limpar()
    produto = input('Produto: ')
    if produto == 'pare':
        break
    preco = input('R$ ')
    produtos.update({produto: float(preco)})

total_gasto_produtos = round(sum(produtos.values()), 2)

arquivo_matimentos = {'Data': data_formatada, 'Total de gasto': total_gasto_produtos, 'Produtos': produtos}

pasta_salva = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'compra_mantimentos')
os.makedirs(os.path.dirname(os.path.abspath(__file__)), exist_ok=True)

compra_mant_dia = os.path.join(pasta_salva, 'compra_mant_{}.json'.format(str(data_formatada)))

limpar()
with open(compra_mant_dia, 'w', encoding='utf8') as arquivo:
    json.dump(
        arquivo_matimentos,
        arquivo,
        ensure_ascii=False,
        indent=2,
    )

for detalhe, mais_detalhe in arquivo_matimentos.items():
    if type(mais_detalhe) == dict:
        for i, j in mais_detalhe.items():
            print('- ', i, j)
    print(detalhe, mais_detalhe)