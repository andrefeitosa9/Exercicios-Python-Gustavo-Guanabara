# Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time do Fortaleza.

tabela = ('Botafogo', 'Bragantino', 'Grêmio', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Fluminense', 'Athletico-PR', 'Atlético-MG',
          'São Paulo', 'Cuiabá', 'Internacional', 'Cruzeiro', 'Corinthians', 'Santos', 'Bahia', 'Vasco', 'Goiás', 'Coritiba', 'América-MG')

# Solução item A
print (f'A) Os cinco primeiros times do Brasileirão são {tabela[0:5]} \n')
# Solução item B
print (f'B) Estão zona de rebaixamento do Brasileirão: {tabela[-4:]} \n')
# Solução item C
print ('C) Times organizados em ordem alfabética: ')
print (sorted(tabela))
print ('\n')
# Solução item D
print (f'D) O Fortaleza está na {tabela.index("Fortaleza") + 1}ª colocação do Brasileirão')
