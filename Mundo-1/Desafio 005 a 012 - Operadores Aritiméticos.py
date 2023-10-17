# Desafio 05 - Faça um programa que leia um número inteiro e mostre na tela o seu antecessor e o seu sucessor
print ('Desafio número 05 -  \n')
numero = float(input('Digite um número: '))
print (f'O número digitado foi {numero}\n')
print (f'O número inteiro sucessor de {numero} é {int(numero+1)} \n')
print (f'O número inteiro antecessor de {numero} é {int(numero-1)}\n')

# Desafio 06 - Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
print ('Desafio número 06 - \n')
n = float(input('Digite um número: '))
print (f'O número digitado foi {n}.\n O dobro de {n} é {n*2}. O triplo de {n} é {n*3} e a raiz quadrada de {n} é {n**(1/2)}')

# Desafio 07 - Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média
print ('Desafio número 07 \n')
nota_1 = float(input('Qual foi a primeira nota do aluno? '))
nota_2 = float(input('Qual foi a segunda nota do aluno'))
print (f'A média do aluno entre suas duas notas foi {(nota_1+nota_2)/2}\n')

# Desafio 08 - Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
print ('Desafio número 08 \n')
altura = float(input('Qual a sua altura em metros?'))
print (f'Sua altura em metros é de {altura}\n')
print (f'Sua altura em centímetros é de {altura*100} e em milímetros é de {altura*1000}\n')

# Desafio 09 - Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada
numero = int(input('Digite um número inteiro qualquer: '))
print (f'O número inteiro digitado foi {numero}')
print (f'A tabuada de {numero} é:\n {numero}*1 = {numero*1} \n {numero}*2 = {numero*2} \n {numero}*3 = {numero*3} \n {numero}*4 = {numero*4} \n {numero}*5 = {numero*5} \n ... \n')

# Desafio 010 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
# US$ 1.00 = R$ 3,27
real_carteira = float(input('Quantos reais você tem na sua carteira?'))
cotacao_dolar = 3.27
print (f'Com o valor de R$ {real_carteira} você pode comprar US$ {(real_carteira/cotacao_dolar):.2f} \n')

# Desafio 011 - Faça um programa que leia a largura e a altura de uma parede em metros, calcule a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

altura = float(input('Qual a altura da parede em metros?'))
largura = float(input('Qual a largura da parede em metros?'))
area = altura * largura
print (f'A área da parede é de {area} m² \n')
print (f'Sabendo que cada litro de tinta pinta 2m², para pintar essa parede você irá precisar de {(area/2):.2f} litros de tinta')

# Desafio 012 - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

preco_antigo = float(input('Digite o preço antigo do produto, em reais:'))
preco_novo = preco_antigo * 0.95

print (f'O novo preço do produto com desconto de 5% é de R$ {preco_novo:.2f} ')
