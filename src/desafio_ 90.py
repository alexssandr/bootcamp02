

alunos = dict()
alunos['nome'] = str(input('Nome: '))
alunos['media'] = float(input(f'Média de {alunos["nome"]}: '))


if alunos['media'] >= 7:
    alunos['situacao'] = 'Aprovado'
elif alunos['media'] >= 5:
    alunos['situacao'] = 'Em Recuperação'
else:
    alunos['situacao'] = 'Reprovado'

print('-=' * 30)
for k, v in alunos.items():
    print(f'{k} é igual a {v}')


