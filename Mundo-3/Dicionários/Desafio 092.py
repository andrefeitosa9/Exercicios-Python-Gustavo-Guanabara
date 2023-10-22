#Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from time import sleep
import datetime

ano_atual = datetime.date.today().year
cadastro = {}
cadastro["Nome"] = input('Digite o nome da pessoa: ')
ano_nascimento = int(input('Digite o ano de nascimento:  '))
idade = ano_atual - ano_nascimento
cadastro['Idade'] = idade
numero_CTPS = int(input('Digite o número da CTPS [0 caso não possua]:  '))
cadastro['Número da Carteira de Trabalho'] = numero_CTPS
if numero_CTPS != 0:
    ano_contratacao = int(input('Ano da primeira contratação: '))
    tempo_carteira = ano_atual - ano_contratacao
    cadastro['Ano de contratação'] = ano_contratacao
    cadastro['Salário'] = float(input('Digite o salário: '))
else:
    cadastro['Anos de contratação'] = "Nunca empregado"
    tempo_carteira = 0
    cadastro['Tempo de Carteira'] = 0
# Tempo de trabalho para aposentadoria = 35 anos.
aposentadoria = 35 - tempo_carteira + idade
cadastro['Idade aposentadoria'] = aposentadoria
print ('-*'*30)
print ('Processando as informações cadastradas... ')
sleep (2)
for k,v in cadastro.items():
    print (f'Para {k} foi registrado {v}')
