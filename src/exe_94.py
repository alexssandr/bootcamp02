
pessoas = []
dados = dict()
continua: str = 'S'
soma_idade = 0

while continua == 'S':
    dados['nome'] = str(input('Nome: '))
    dados['sexo'] = str(input('Sexo: [M/F] ')).upper()
    dados['idade'] = int(input('Idade: '))
    continua = str(input('Quer continuar? [S/N] ')).upper()
    soma_idade += dados['idade']
    pessoas.append(dados.copy())

print('+=' * 30)
print(f'- O grupo tem {len(pessoas)} pessoas.')
media_idade = soma_idade/ len(pessoas)
print(f'- A média de idade é de {media_idade:5.2f} anos.')

print('As mulheres cadastradas são: ')
for p in pessoas:
    if p['sexo'] == 'F':
        print(f'{p['nome']}')

print('Lista das pessoas que estão acima da media:')
for p in pessoas:
    if p['idade'] > media_idade:
        print(f'Nome = {p['nome']}; sexo = {p['sexo']}; idade = {p['idade']}')