# Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

from time import sleep
estatisticas_time = []
estatisticas_jogador = {}
gols_feitos = []

# Cadastro de atletas
while True:
    estatisticas_jogador['Nome'] = input('Digite o nome do jogador:  ')
    estatisticas_jogador['Quantidade de Jogos'] = int(input('Quantos jogos jogou? '))
    for a in range (0,estatisticas_jogador["Quantidade de Jogos"]):
        gols = int(input(f'     Quantidade de gols no {a+1}º jogo:  '))
        gols_feitos.append(gols)
    estatisticas_jogador["Gols Marcados"] = gols_feitos[:]
    estatisticas_jogador['Total de gols'] = sum(gols_feitos)
    estatisticas_time.append(estatisticas_jogador.copy())
    del gols_feitos
    gols_feitos = []
    while True:
        continuar = input('Deseja continuar? [S / N] ').strip().upper()[0]
        while continuar not in 'SsNn':
            continuar = input('Opção inválida. Deseja continuar? [S / N]  ').strip().upper()[0]
        if continuar in 'SsNn':
            break
    if continuar == 'N':
        break
print ('=*'*30)
print (f'Calculando as estatísticas do time...')
sleep (1)

print (f'{"Cód.":>3}',end=' ')
print (f'{"Nome":<10}',end=' ')
print (f'{"Partidas":<10}',end=' ')
print (f'{"Gols":<10}',end=' ')
print (f'{"Total de gols":<10}')
print ()

for k, v in enumerate(estatisticas_time):
    print (f'{k:>3}',end=' ')
    for d in v.values():
        print (f'{str(d):^10}',end=' ')
    print ()
print ('-'*40)

while True:
    busca = int(input('Qual jogador deseja mostrar? Use o código 999 para parar:  '))
    if busca > len(estatisticas_time):
        print (f'Código {busca} inválido. Tente novamente.')
    if busca == 999:
        break
    else:
        print (f'Levantamento do jogador {estatisticas_time[busca]["Nome"]}:  ')
        for i, g in enumerate(estatisticas_time[busca]["Gols Marcados"]):
            print (f'No jogo {i+1} o {estatisticas_time[busca]["Nome"]} fez {g} gols')
