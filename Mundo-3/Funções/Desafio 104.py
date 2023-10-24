# Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante
# ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

def leiaInt(msg):
    """
- > Lê o valor inserido, faz a validação se é ou não um número e retorna o número digitado
    :param msg: String que irá aparecer com a solicitação para o usuário digitar o número
    :return: Retorna o número inteiro
    """
    num = input(f'{msg}')
    if num.isnumeric():
        return int(num)
    else:
        while num.isnumeric() == False:
            print('\033[031mERRO.\033[m')
            num = input(f'Digite um número inteiro válido:  ')
            if num.isnumeric():
                return int(num)
                break


n = leiaInt('Digite um número: ')
print (f'Você digitou o número {n}')