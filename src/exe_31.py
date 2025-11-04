
tarifa_curta = 0.50
tarifa_longa = 0.45

km_viagem = int(input('Digite os KM da viagem: '))
if km_viagem <= 200:
    preco = km_viagem * tarifa_curta
else:
    preco = km_viagem * tarifa_longa

print(preco)