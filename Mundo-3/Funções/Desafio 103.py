# Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
# o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
def ficha(nome = '<desconhecido>', gols = 0):
    """
    -> Imprime na tela uma frase com o nome do jogador (Caso informado) e a quantidade de gols feitos no campeonato.
    :param nome: Opcional. Caso não seja informado será definido como "Desconhecido"
    :param gols: Opcional. Caso não informado será definido como 0.
    :return: Sem função return
    """
    print (f'O jogador {nome} marcou {gols} gols no campeonato.')


n = input('Digite o nome do jogador:  ')
g = input('Quantos gols o jogador fez?  ')
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n,g)