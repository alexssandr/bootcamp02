from random import randint
from operator import itemgetter
from time import sleep

print('Iniciando o game')
print('')
sorteio = dict()
ranking = []

for x in range(1,5):
    sorteio[f'Jogador{x}'] = randint(1,6)
    sleep(2)

print('Valores sorteados')

for k, v in sorteio.items():
    print(f'{k} tirou {v}')

print('+=' * 30)
print('== Ranking dos jogadores ==')
ranking = sorted(sorteio.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}.')