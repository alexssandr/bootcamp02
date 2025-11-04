salario = float(input('Digite o seu salário: '))
valor_imovel = float(input('Digite o valor do imovel: '))
qtde_anos = int(input('Em quantos anos pretende pagar? '))
parcela_limite = salario * (30/ 100)

qtde_meses = qtde_anos * 12
prestacao_mensal = valor_imovel/qtde_meses

if prestacao_mensal <= parcela_limite:
    print(f'Emprestimo Aprovado, parcela de R$ {prestacao_mensal}')
else:
    print(f'Seu emprestimo foi negado, porque seu limite é de R${parcela_limite} e a parcela do ímovel é de R$ {prestacao_mensal}')

# 30% emprestimo