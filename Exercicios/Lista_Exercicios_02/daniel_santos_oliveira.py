# Lista de exercícios 2 -  Algoritmo e Lógica de Programação - Masanori
# Exercício 1

print('Exercício 1 - Triângulo')
print('Informar números inteiros.')
lado1 = int(input('Informe o PRIMEIRO lado do triângulo: '))
lado2 = int(input('Informe o SEGUNDO lado do triângulo: '))
lado3 = int(input('Informe o TERCEIRO lado do triângulo: '))

if lado1 == 0 or lado2 == 0 or lado3 == 0:
    print('Quaisquer dos lados de um triângulo não pode ser <= 0.')
elif (lado1 + lado2) < lado3 or (lado1 + lado3) < lado2 or (lado2 + lado3) < lado1:
    print('Não é um triângulo, a soma de dois lados não pode ser menor que um lado.')
else:
    if lado1 == lado2 and lado2 == lado3:
        print('Triângulo Isósceles.')
    elif lado1 != lado2 and lado2 != lado3 and lado3 != lado1:
        print('Triângulo Escaleno.')
    else:
        print('Triângulo Equilátero.')

# Exercício 2

print('Exercício 2 - Ano BISSEXTO')
ano = int(input('Digite o ANO para análise: '))
if (ano % 100 != 0) and (ano % 4 == 0) or ano % 400 == 0:
    if ano > 2019:
        print('Será ano BISSEXTO')
    else:
        print('Foi ano BISSEXTO')
else:
    if ano > 2019:
        print('Não será é ano BISSEXTO')
    else:
        print('Não fora ano BISSEXTO')

# Exercício 3

print('Exercício 3 - Multa PESCA')
peso = float(input('Informe o peso TOTAL em KG do peixe pescado: '))
if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
else:
    excesso = 0
    multa = 0
print(f'Excesso: {excesso}kg \nMulta: R$ {multa}')

# Exercício 4

print('Exercício 4 - MAIOR número')
n1 = int(input('Informe o 1° NÚMERO: '))
n2 = int(input('Informe o 2° NÚMERO: '))
n3 = int(input('Informe o 3° NÚMERO: '))
if n1 > n2 and n1 > n3:
    print(f'Maior: {n1}')
else:
    if n2 > n3:
        print(f'Maior: {n2}')
    else:
        print(f'Maior: {n3}')

# Exercício 5

print('Exercício 5 - MAIOR número')
n1 = int(input('Informe o 1° NÚMERO: '))
n2 = int(input('Informe o 2° NÚMERO: '))
n3 = int(input('Informe o 3° NÚMERO: '))
if n1 > n2 and n1 > n3:
    print(f'Maior: {n1}')
else:
    if n2 > n3:
        print(f'Maior: {n2}')
    else:
        print(f'Maior: {n3}')
        
if n1 < n2 and n1 < n3:
    print(f'Menor: {n1}')
else:
    if n2 < n3:
        print(f'Menor: {n2}')
    else:
        print(f'Menor: {n3}')

# Exercício 6

print('Exercício 6 - Salário')
slrHora = int(input('Informe o valor do salário por HORA: '))
qtdHora = int(input('Informe a quantidade de HORAS trabalhadas: '))

imptRenda = ((slrHora * qtdHora) * 11)/100
inss = ((slrHora * qtdHora) * 8)/100
sind = ((slrHora * qtdHora) * 5)/100
slrLiq = (slrHora * qtdHora) - (imptRenda + inss + sind)

print(f'+Salário Bruto: R${slrHora * qtdHora:.2f}')
print(f'-Imposto de Renda(11%): R$ {imptRenda:.2f}')
print(f'-INSS(8%): R$ {inss:.2f}')
print(f'-Sindicato(5%): R$ {sind:.2f}')
print(f'=Salário Liquido: R$ {slrLiq:.2f}')

# Exercício 7

print('Exercício 7 - Loja de TINTAS')
tmhArea = int(input('Informe o TAMANHO em m² da área a ser pintada: '))
if tmhArea % 54 == 0:
    print('1', tmhArea % 54 == 0) #Linha adicionada para identifica em qual condição foi executada.
    qtdLata = int(tmhArea / 54)
else:
    print('2', tmhArea % 54 == 0) #Linha adicionada para identifica em qual condição foi executada.
    qtdLata = int(tmhArea / 54 + 1)
vlrPgr = qtdLata * 80
print(f'{qtdLata} lata(s).')
print(f'Total a pagar: {vlrPgr:.2f}')
