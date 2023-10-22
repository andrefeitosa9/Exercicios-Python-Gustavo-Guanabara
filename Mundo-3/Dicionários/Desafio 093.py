# Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
from time import sleep

estatisticas = {}
estatisticas['Jogador'] = input('Qual o nome do jogador? ')
partidas = int(input('Quantas partidas ele jogou? '))
estatisticas['Partidas jogadas'] = partidas
total_gols = 0
for p in range (0,partidas):
    gols_marcados_partida = int(input(f'Quantos gols marcados na {p+1}ª partida? '))
    estatisticas[f'Gols partida {p+1}'] = gols_marcados_partida
    total_gols += gols_marcados_partida
estatisticas['Total de gols marcados'] = total_gols
print ('=*'*30)
print (f'Calculando as estatísticas do jogador {estatisticas["Jogador"]}...')
sleep (1)

for k, v in estatisticas.items():
    print (f'O campo {k} tem o valor {v}')
