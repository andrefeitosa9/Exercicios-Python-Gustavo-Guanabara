# Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.
from time import sleep
import random
quantidade_jogos = int(input('Quantos jogos deseja jogar? '))
jogo_final = list()
jogo_temporario = list()
contador_num = 0
total_jogos = 0
while True:
    if total_jogos < quantidade_jogos:
        total_jogos += 1
        contador_num = 0
        while True:
            num = random.randint(1, 60)
            if num not in jogo_temporario:
                jogo_temporario.append(num)
                contador_num += 1
            if contador_num == 6:
                jogo_temporario.sort()
                jogo_final.append(jogo_temporario[:])
                jogo_temporario.clear()
                break
    else:
        break
for d in range (0, len(jogo_final)):
    print (f'{jogo_final[d]}')

