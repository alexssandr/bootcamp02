cidade = str(input('Digite o nome da sua cidade: ')).lower().strip()

if cidade.startswith('santo'):
    print(f'A cidade {cidade} começa com a palavra "santo"')
else:
    print(f'A cidade {cidade} não começa com a palavra "santo"')