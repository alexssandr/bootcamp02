import math

numero = int(input('Digite um numero: '))
numero_mod = numero % 2
if numero_mod == 0:
    print('O número é par')
else:
    print('O número é impar')