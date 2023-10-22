# Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from time import sleep
from random import randint
from operator import itemgetter
ranking = {}
jogo = {'Jogador 1': randint(1,6), 'Jogador 2': randint(1,6), 'Jogador 3': randint (1,6), 'Jogador 4': randint(1,6)}
print ('Jogando os dados...\n')
sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print (f'{i+1}º lugar: O {v[0]} tirou {v[1]} no dado.')
    sleep(1)
