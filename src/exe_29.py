velocidade_permitida = 80
velocidade_informada = int(input('Digite a velocidade do carro: '))

if velocidade_informada > velocidade_permitida:
    print('VOCê FOI MULTADO!')
    valor_multa = (velocidade_informada - velocidade_permitida) * 7
    print(f'Multa no valor de {valor_multa:.2f}')
else:
    print('Tudo certo')
    