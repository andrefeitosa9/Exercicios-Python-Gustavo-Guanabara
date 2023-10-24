# Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos
# e vai retornar um dicionário com as seguintes informações:
#
# – Quantidade de notas
# – A maior nota
# – A menor nota
# – A média da turma
# – A situação (opcional)


def notas(*n, sit=False):
    """
    -> Recebe o valor das notas de uma turma e adiciona quantidade de notas, média, maior e menor notas em um dicionário.
    Em caso de sit=True, aprsenta a situação da turma, baseada na média da mesma
    :param n: Notas dos alunos
    :param sit: Situação da turma. Opcional. Por padrão, False
    :return: Dicionário com as informações da turma
    """
    r = dict()
    r['Quantidade'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n) / len(n)
    if sit == True:
        if r['Média'] <= 4:
            r['Situação'] = 'Péssima'
        if r['Média'] < 7:
            r['Situação'] = 'Ruim'
        if 7 <= r['Média'] < 8:
            r['Situação'] = 'Regular'
        if 8 <= r['Média'] < 9:
            r['Situação'] = 'Boa'
        if 9<= r['Média'] <= 10:
            r['Situação'] = 'Excelente'
    return r


# Programa principal
resp = notas(9, 9.3,10, 5, sit=True)
print (resp)
