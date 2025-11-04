
ano_usuario = int(input('Digite um ano: '))



if ano_usuario % 4 == 0:
    if (ano_usuario % 100 == 0) and (ano_usuario % 400 == 0):
        print('ano bissexto')
    else:
        print('ano comum')
else:
    print('ano comum')