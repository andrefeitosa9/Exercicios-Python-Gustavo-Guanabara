# Exercício Python 090: Faça um programa que leia nome e média de um aluno,
# guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
boletim = {}


nome = input('Nome do aluno:  ')
media = float(input('Média do aluno:  '))
if media >= 7:
    situacao = 'Aprovado'
else:
    situacao = 'Reprovado'
boletim = {'Nome: ': nome, 'Média: ': media, 'Situação: ': situacao}

print (boletim)
