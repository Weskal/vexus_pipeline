import random
import os
from datetime import datetime
import pandas as pd
from datetime import datetime, timedelta
from db_utils import carregar_produtos_sql  

def gerar_pedidos_excel(execution_date_str=None, num_pedidos=15, pasta_saida='../raw_data'):
    data = datetime.strptime(execution_date_str, '%Y-%m-%d') + timedelta(days=1)

    os.makedirs(pasta_saida, exist_ok=True)
    nome_arquivo = os.path.join(pasta_saida, f"pedidos_{data.strftime('%Y-%m-%d')}.csv")

    produtos = carregar_produtos_sql()
    pedidos_lista = []

    for i in range(num_pedidos):
        ordem_venda = 4000 + i
        rand_number = random.randint(1, 5)
        preco_final = 0.0
        produtos_pedido = []

        for _ in range(rand_number):
            produto = random.choice(produtos)
            qtd = random.randint(1, 5)

            preco_unitario = float(str(produto['preco']).replace(',', '.'))
            preco_total_produto = preco_unitario * qtd
            preco_final += preco_total_produto

            produtos_pedido.append({
                'ordem_venda': ordem_venda,
                'id_produto': produto['id_produto'],
                'quantidade': qtd,
                'preco_total_produto': round(preco_total_produto, 2),
                'preco_final': None,
                'data_pedido': data.strftime('%Y-%m-%d')
            })

        for item in produtos_pedido:
            item['preco_final'] = round(preco_final, 2)
            pedidos_lista.append(item)

    df_pedidos = pd.DataFrame(pedidos_lista)
    df_pedidos.to_csv(nome_arquivo, index=False)

    print(f"Arquivo CSV gerado com sucesso: {nome_arquivo}")
