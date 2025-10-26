

valor = 10000
while valor > 9999:
    valor = int(input('Digite um numero de 0 a 9999: '))

valor_str = str(valor)
len_str = len(valor_str)
if len_str == 1:
    unidade = valor_str[0:1]
    print(f'Unidade: {unidade}')
elif len_str == 2:
    dezena = valor_str[0:1]
    unidade = valor_str[1:2]
    print(f'Unidade: {unidade}')
    print(f'Dezena: {dezena}')
elif len_str == 3:
    centena = valor_str[0:1]
    dezena = valor_str[1:2]
    unidade = valor_str[2:3]
    print(f'Unidade: {unidade}')
    print(f'Dezena: {dezena}')
    print(f'Centena: {centena}')
else:
    milhar = valor_str[0:1]
    centena = valor_str[1:2]
    dezena = valor_str[2:3]
    unidade = valor_str[3:4]
    print(f'Unidade: {unidade}')
    print(f'Dezena: {dezena}')
    print(f'Centena: {centena}')
    print(f'Milhar: {milhar}')
    


