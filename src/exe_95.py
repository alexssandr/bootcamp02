from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ["nome", "numero_partidas", "gols", "total"]

base_jogadores = []
dados = dict()
continua: str = 'S'

while continua == 'S':
    
    print('-' *30)
    dados['nome'] = str(input('Nome jogador: '))
    dados['numero_partidas'] = int(input(f'Quantas partidas {dados['nome']} jogou? '))
    dados['gols'] = []
    dados['total'] = 0

    for x in range(0,dados['numero_partidas']):
        qtde_gols = int(input(f'Quantos gols na partida {x+1}? '))
        dados['gols'].append(qtde_gols)
        dados['total'] = dados['total'] + qtde_gols
    
    base_jogadores.append(dados.copy())
    continua = input(f'Quer continuar? [S/N] ').upper()

print('+=' * 30)

for x in base_jogadores:
    for v in x.values():
        jogadores = []
        jogadores.append(v)
    table.add_row(jogadores)


print(table)

for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')

print('+=' * 30)

print(f'O jogador {dados["nome"]} jogou {dados["numero_partidas"]} partidas.')

for o, v in enumerate(dados['gols'],1):
    print(f'    => Na partida {o}, fez {v} gols')

print(f'Foi um total de {dados["total"]}')
    