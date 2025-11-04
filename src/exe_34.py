salario = float(input('Digite seu salario: '))
SALARIO_TH = 1250

if salario <= SALARIO_TH:
    percentual_aumento = 15
    aumento = salario * (percentual_aumento /100)
else:
    percentual_aumento = 10
    aumento = salario * (percentual_aumento /100)
    
print(f'Seu aumento foi de {percentual_aumento}% - {aumento:.2f} com o novo salário de {salario+aumento}')