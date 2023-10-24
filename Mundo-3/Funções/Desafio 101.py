# Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de
# uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
from datetime import datetime

def voto(ano_nascimento):
    ano_atual = datetime.today().year
    idade = ano_atual - ano_nascimento
    if 18 > idade >= 16 or idade >= 70:
        print (f'Com {idade} anos o voto é OPCIONAL.')
    elif 70 > idade >= 18:
        print (f'Com {idade} anos o voto é OBRIGATÓRIO.')
    else:
        print (f'Pessoas de {idade} anos ainda não podem votar.')


ano_nascimento = int(input('Digite o ano de nascimento: '))
voto(ano_nascimento)