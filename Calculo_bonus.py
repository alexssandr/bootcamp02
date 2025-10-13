
print("Iniciando o calculo de KPI...")
try:
    Nome: str = input("Digite o Nome:")
except Exception as e:
    print(f'Ocorreu o erro: {e}')

try:
    Salario = float(input("Digite o Salario:"))

except ValueError:
    print("Digite um numero")

bonus = 1000
percentual_bonus = 1.5

try: 
    Valor_bonus = bonus + (Salario * percentual_bonus)
except TypeError:
    print("Não foi possível realizar a soma por erro de tipagem")
print(Valor_bonus)
