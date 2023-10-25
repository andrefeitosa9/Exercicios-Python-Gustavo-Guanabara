# Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.

def titulo(msg):
    tam = len(msg) + 4
    print ('~'*tam)
    print (f'       {msg}')
    print ('~' * tam)


def opcoes():
    print("""ESCOLHA UMA OPÇÃO:
    [1] Função Aumentar - Soma
    [2] Função Diminuir - Subtração
    [3] Função Dobro
    [4] Função Metade
    [5] Formatação em moeda - R$ 
    [999] ENCERRA A CALCULADORA
    """)

def aumentar(*num, formatar=False):
    print ('Função escolhida: SOMA.')
    soma = 0
    repetir = ' '
    numeros = []
    formatacao = input('Deseja formatar o número em reais? [S / N]  ').upper().strip()[0]
    while True:
        num = input('Digite um número para somar: ')
        if num.isnumeric():
            numeros.append(float(num))
            soma += float(num)
            repetir = input("Deseja continuar? [ S / N]  ").strip().upper()[0]
            if repetir == 'N':
                break
            if repetir not in 'SN':
                repetir = input('Opção inválida. Deseja continuar? [S / N]  ').strip().upper()[0]
                if repetir == 'N':
                    break
        else:
            print (f'Caractere inválido.')
        if formatacao == 'S':
            formatar == True
            if formatar == True:
                soma = moeda(soma)

    print (f'Os números informados foram {numeros} e a soma deles é {soma}')


def diminuir (*num):
    print ('Função escolhida: SUBTRAÇÃO.')
    resultado = 0
    repetir = ' '
    numeros = []
    while True:
        num = input('Digite um número para subtrair: ')
        if num.isnumeric():
            numeros.append(float(num))
            resultado -= float(num)
            repetir = input("Deseja continuar? [ S / N]  ").strip().upper()[0]
            if repetir == 'N':
                break
            if repetir not in 'SN':
                repetir = input('Opção inválida. Deseja continuar? [S / N]  ').strip().upper()[0]
                if repetir == 'N':
                    break
        else:
            print (f'Caractere inválido.')

    print (f'Os números informados foram {numeros} e a subtração deles é igual a {resultado}')


def dobro(num=0):
    print ('Função escolhida: DOBRO. ')
    while True:
        num = input('Informe um número:  ')
        if num.isnumeric():
            dobro = float(num) * 2
            print (f'O dobro de {num} é igual a {dobro}')
            break
        else:
            print ('Caractere inválido.')

def metade(num=0):
    print ('Função escolhida: METADE')
    while True:
        num = input('Digite um número:  ')
        if num.isnumeric():
            metade = float(num) / 2
            print (f'A metade de {num} é igual a {metade}')
            break
        else:
            print ('Caractere inválido.')

def moeda(num=0):
    print (f'Função Formatação de número como moeda')
    num = float(input('Digite o valor que deseja formatar em reais: '))
    num = (f'{num:.2f}')
    print('R$ ', end='')
    for d in num:
        if d == '.':
            print (',',end='')
        elif d == ',':
            print ('.',end='')
        else:
            print (f'{d}',end='')
