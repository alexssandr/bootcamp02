valor_produto = None
valor_produto_final = None
condicao_pagamento = None
desconto = 0
juros = 0

valor_produto = float(input('Digite o valor do produto: '))
opcao_compra = str(input('A compra será a vista? [S/N] '))

if opcao_compra == 'S':
    forma_pgto = str(input('Qual a forma de pagamento? [dinheiro/ cheque/cartao] '))
    if forma_pgto == 'dinheiro' or forma_pgto == 'cheque':
        desconto = (10 / 100)
    else:
        desconto = (5 / 100)
else:
    condicao_pagamento = int(input('Quantas vezes deseja dividir? [2x, 3x, ou mais/] '))
    if condicao_pagamento > 2:
        juros = (20/ 100)

valor_produto_final = valor_produto - (valor_produto * desconto) + (valor_produto * juros)
print(valor_produto_final)
                
        