from datetime import datetime

ano_atual = datetime.now().year
ano_nascimento = int(input('Digite o ano de seu nascimento: '))
idade = ano_atual - ano_nascimento

if idade <= 9:
    print('Mirim')
elif idade <= 14:
    print('Infantil')
elif idade <= 19:
    print('Junior')
elif idade <= 20:
    print('Senior')
else:
    print('Master')