# Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média
cadastro_geral = []
cadastro_temporario = {}
somaidade = 0
lista_mulheres = []
acima_media = []

while True:
    cadastro_temporario["Nome"] = input('Digite o nome da pessoa:  ')
    sexo = input('Digite o sexo: [M / F]  ').strip().upper()[0]
    while sexo not in "MmFf":
        sexo = input('Sexo inválido. Digite o sexo: [M / F]  ').strip().upper()[0]
        if sexo in "MmFf":
            break
    cadastro_temporario['Sexo'] = sexo
    cadastro_temporario['Idade'] = int(input('Qual a idade dessa pessoa? '))
    somaidade += cadastro_temporario['Idade']
    continuar = input('Deseja continuar? [S / N]  ').strip().upper()[0]
    while continuar not in "SsNn":
        continuar = input('Opção inválida. Deseja continuar? [S / N]  ').strip().upper()[0]
        if continuar in 'SsNn':
            break
    if sexo == "F":
        lista_mulheres.append(cadastro_temporario.copy())
    cadastro_geral.append(cadastro_temporario.copy())
    del cadastro_temporario
    cadastro_temporario = {}
    if continuar == 'N':
        break
mediaidade = somaidade / len(cadastro_geral)
print (cadastro_geral)
# Solução A)
print (f'A) A quantidade de pessoas cadastras foi: {len(cadastro_geral)}')
# Solução B)
print (f'B) A média de idade dessas pessoas é de {mediaidade:.1f} anos')
# Solução C)
print (f'C) A lista só com mulheres é {lista_mulheres}')
# Solução D)

for i in cadastro_geral:
    if i["Idade"] >= mediaidade:
        for k, v in i.items():
            print (f'{k} = {v}; ',end='')

print ('\nPrograma Encerrado')