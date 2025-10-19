

nome: str = str(input('Nome: '))
media: float = float(input(f'Média de {nome}: '))
if media >= 7:
    situacao = 'Aprovado'
else:
    situacao = 'Reprovado'
    
print(f'Nome é igual a {nome}')
print(f'Média é igual a {media}')
print(f'Situação é igual a {situacao}')


