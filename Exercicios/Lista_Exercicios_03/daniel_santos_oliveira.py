############ Exercicio 1 ############
print('\n Exercício 1 - Número entre ZERO e DEZ')
nota = int(input('Informe uma nota entre 0(ZERO) e 10(DEZ): '))
while nota < 0 or nota > 10:
    print('Nota informada não é válida.')
    nota = int(input('Informe uma nota de 0(ZERO) a 10(DEZ): '))
print(f'Nota: {nota}')

############ Exercicio 2 ############
print('\n Exerício 2 - Usuário e Senha')
usuario = input('Informe o Usuário: ')
senha = input('Informe a Senha: ')
while usuario == senha:
    print('\n Os dados de <Usuário> e <Senha> não podem ser iguais.')
    usuario = input('Informe o Usuário: ')
    senha = input('Informe a Senha: ')
print('Dados registrados com sucesso!')

############ Exercicio 3 ############
print('\n Exercício 3 - Crescimento população')
A = 80000
B = 200000
cont = 0
while A != B or A > B:
    AC1 = ((A * 3)/100) + A
    AC2 = ((B * 1.5)/100) + B
    A = A + AC1
    B = B + AC2
    cont = cont + 1
print(f'Quantidade em ANOS é de: {cont}')

############ Exercicio 4 ############
print('\n Exercício 4 - Fibonacci')
n = int(input('Informe um número inteiro: '))
x = 1
pri = 1
seg = 1
while x < n:
    print(pri)
    ter = pri + seg
    pri = seg
    seg = ter
    x = x + 1

############ Exercicio 5 ############
print('\n Exercício 5 - Algorítmo de Euclides')
n1 = int(input('Informe 1º número INTEIRO: '))
n2 = int(input('Informe 2º número INTEIRO: '))
while n1 % n2 != 0:
    AC1 = n1 % n2
    n1 = n2
    n2 = AC1
print(f'MDC: {n2}')
