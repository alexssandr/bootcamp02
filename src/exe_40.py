n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2

if media >= 7:
    print(f'APROVADO: Média {media}')
elif media < 5:
    print(f'REPROVADO: Média {media}')
else:
    print(f'RECUPERAÇÃO: Média {media}')
