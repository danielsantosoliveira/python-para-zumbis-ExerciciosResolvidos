print('\n Exercicio 1 - Número Triangular')
n = int(input('Informe um NÚMERO inteiro POSITIVO: '))
n1 = 0
n2 = 1
n3 = 2
ac = 1
while ac != n:
    if ac == n:
        break
    n1 = n1 + 1
    n2 = n2 + 1
    n3 = n3 + 1
    ac = n1*n2*n3
print(f'{ac} é triangular, pois {n1}*{n2}*{n3} = {ac}')
