from datetime import datetime

ano_atual = datetime.now().year

idade_aposentadoria: None

dados = dict()

dados['nome'] = str(input('Nome: '))
dados['ano_nascimento'] = int(input('Ano de Nascimento: '))
dados['idade'] = ano_atual - dados['ano_nascimento']
dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if dados['ctps'] > 0:
    dados['ano_contratacao'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: R$ '))
    dados['idade_aposentadoria'] = dados['idade'] + (35 - (ano_atual - dados['ano_contratacao']))

print('+='*30)

for k,v in dados.items():
    if k == 'ano_nascimento':
        None
    else:
        print(f'- {k} tem o valor {v}')
