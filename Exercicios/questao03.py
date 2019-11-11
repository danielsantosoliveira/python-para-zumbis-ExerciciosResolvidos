print(f'Exercício 3 - Cálculo em Segundos')
dias = int(input(f'Informe a quantidade de DIAS: '))
horas = int(input(f'Informe a quantidade de HORAS: '))
minutos = int(input(f'Informe a quantidade de MINUTOS: '))
segundos = int(input(f'Informe a quantidade de SEGUNDOS: '))
calculo = ((dias * 86400) + (horas * 3600) + (minutos * 60)) + segundos
print(f'Total em segundos: {calculo}s')
