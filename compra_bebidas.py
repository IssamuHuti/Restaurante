import os
import json
from datetime import datetime

def limpar():
    os.system('cls')

limpar()
data_compra = datetime.now()
data_formatada = data_compra.strftime('%d_%m_%Y')
print('Data da compra: ', data_formatada)

print('Informe os gastos com bebidas do dia')

bebidas = {}

bebida = input('Produto: ')
preco_bebida = input('R$ ')
bebidas.update({bebida: float(preco_bebida)})
while True:
    limpar()
    bebida = input('Produto: ')
    if bebida == 'pare':
        break
    preco_bebida = input('R$ ')
    bebidas.update({bebida: float(preco_bebida)})

total_gasto_bebidas = round(sum(bebidas.values()), 2)

arquivo_bebidas = {'Data': data_formatada, 'Total de gasto': total_gasto_bebidas, 'Produtos': bebidas}

pasta_salva = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'compra_bebidas')
os.makedirs(os.path.dirname(os.path.abspath(__file__)), exist_ok=True)

compra_bebida_dia = os.path.join(pasta_salva, 'compra_bebida_{}.json'.format(str(data_formatada)))

limpar()
with open(compra_bebida_dia, 'w', encoding='utf8') as arquivo:
    json.dump(
        arquivo_bebidas,
        arquivo,
        ensure_ascii=False,
        indent=2,
    )

for detalhe, mais_detalhe in arquivo_bebidas.items():
    if type(mais_detalhe) == dict:
        for i, j in mais_detalhe.items():
            print('- ', i, j)
    print(detalhe, mais_detalhe)