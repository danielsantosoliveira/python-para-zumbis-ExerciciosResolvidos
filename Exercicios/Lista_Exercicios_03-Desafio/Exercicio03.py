print('Exercício 3 - Número Primo')
n = int(input('Informe um número INTEIRO POSITIVO para análise: '))
x = 2
while x <= n and n != 1 and n != 0:
    if n % x == 0 and x < n:
        x = n + 1
        print(f'{n} não é primo')
    elif n % x == 0 and x == n:
            x = x + 1
            print(f'{n} é primo')
    else:
        x = x + 1
