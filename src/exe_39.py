from datetime import datetime

ano_atual = datetime.now().year
ano_nascimento = int(input('Digite o ano de seu nascimento: '))
idade = ano_atual - ano_nascimento

if idade < 17:
    print('Não está na idade de se alistar')
    print(f'Faltam {17-idade} ano(s)')
elif idade >=18:
    print('Já passou a idade de alistamento')
    print(f'Já passou {idade-17} ano(s) do seu alistamento')
else:
    print('É a hora de se alistar')
