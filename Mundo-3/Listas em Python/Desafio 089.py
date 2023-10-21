# Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

temporario = []
lista_final = []
continuar = ' '

# Cadastro notas de alunos
while True:
    temporario.append(input('Nome do estudante:  '))
    temporario.append(float(input('Primeira nota do estudante:  ')))
    temporario.append(float(input('Segunda nota do estudante:  ')))
    lista_final.append(temporario[:])
    temporario.clear()
    continuar = input('Deseja continuar? S / N  ').strip().upper()[0]
    if continuar not in 'SsNn':
        while True:
            continuar = input('Opção inválida. Deseja continuar? S / N  ').strip().upper()[0]
            if continuar in "SsNn":
                break
    if continuar == 'N':
        break
print (f'\n')
print (f'{lista_final}')
print ('*'*50)
print ()
# Solução A - Mostrar boletim com nome, média, com gatilho para ver nota de aluno específico

print(f'----- BOLETIM GERAL DA TURMA -----')
for a in range (0, len(lista_final)):
    print (f'{a}',end='  ')
    print (f'{lista_final[a][0]}',end='  ')
    print (f'{(lista_final[a][1] + lista_final[a][2]) / 2}')
print ('*'*50)
print ()
while True:
    indice = int(input('Mostrar notas de qual aluno? 999 interrompe:  '))
    if indice == 999:
        break
    print (f' As notas de {lista_final[indice][0]} foram {lista_final[indice][1:3]}\n')
    print(f'----- BOLETIM GERAL DA TURMA -----')
    for a in range(0, len(lista_final)):
        print(f'{a}', end='  ')
        print(f'{lista_final[a][0]}', end='  ')
        print(f'{(lista_final[a][1] + lista_final[a][2]) / 2}\n')
print ('Programa encerrado')


