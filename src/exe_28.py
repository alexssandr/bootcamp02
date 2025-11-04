from random import randint

numero_sorteado = int(randint(0,5))
numero_usuario = int(input('Digite o número que você acha que foi sorteado: '))

print('Venceu' if numero_sorteado == numero_usuario else 'Perdeu')