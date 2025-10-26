
nome: str = str(input('Digite seu nome completo:'))

nome_maiuscula = nome.upper()
nome_minuscula = nome.lower()
total_letras = len(nome.strip().replace(' ','',-1))
total_letras_primeiro_nome = len(nome[:nome.find(' ')])
print(f'Nome com as letras maiusculas: {nome_maiuscula}')
print(f'Nome com as letras minusculas: {nome_minuscula}')
print(f'Total de letras no nome: {total_letras}')
print(f'Total de letras no nome: {total_letras_primeiro_nome}')