numero1 = int(input('Digite um numero: '))
numero2 = int(input('Digite um numero: '))
numero3 = int(input('Digite um numero: '))

lista_valores = [numero1, numero2, numero3]
lista_valores.sort()
menor = lista_valores[0]
maior = lista_valores[2]


print(f'Maior {maior}')
print(f'Menor {menor}')