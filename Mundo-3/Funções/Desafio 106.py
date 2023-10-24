# Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará.

def ajuda(msg):
    help(msg)


def titulo (msg):
    tam = len(msg) + 4
    print ('~' * tam)
    print (f'     {msg}')
    print ('~' * tam)


# Programa principal
while True:
    titulo('Sistema PyHelp')
    comando = input('Qual comando você deseja ver o manual?  ')
    if comando.upper() == 'FIM':
        titulo('Até logo')
        break
    else:
        ajuda(comando)