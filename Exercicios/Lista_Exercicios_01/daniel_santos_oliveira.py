############## Exercício 01 ##############
print(f'Exercício 1 - Soma de dois números')
n1 = int(input(f'Informe o PRIMEIRO número: '))
n2 = int(input(f'Informe o SEGUNDO número: '))
soma = n1 + n2
print(f'Total da soma dos dois números: {soma}')

############## Exercício 02 ##############
print(f'Exercício 2 - Conversão METROS para MILÍMETROS')
n = float(input(f'Informe qualquer valor em METROS para conversão: '))
conversao = n * 1000
print(f'Valor convertido em MILÍMETROS: {conversao}mm')

############## Exercício 03 ##############
print(f'Exercício 3 - Cálculo em Segundos')
dias = int(input(f'Informe a quantidade de DIAS: '))
horas = int(input(f'Informe a quantidade de HORAS: '))
minutos = int(input(f'Informe a quantidade de MINUTOS: '))
segundos = int(input(f'Informe a quantidade de SEGUNDOS: '))
calculo = ((dias * 86400) + (horas * 3600) + (minutos * 60)) + segundos
print(f'Total em segundos: {calculo}s')

############## Exercício 04 ##############
print(f'Exercício 4 - Aumento de Salário')
salario = float(input(f'Informe o valor do SALÁRIO: '))
porcentagem = float(input(f'Informe a PORCETAGEM do aumento: '))
aumento = salario * (porcentagem/100)
novoSalario = salario + aumento
print(f' Valor do AUMENTO: R$ {aumento} \n Valor do NOVO Salário: R$ {novoSalario}')

############## Exercício 05 ##############
print(f'Exercício 5 - Desconto Produto')
produto = float(input(f'Informe o PREÇO do produto: '))
percentual = float(input(f'Informe o PERCENTUAL de desconto: '))
desconto = produto * (percentual/100)
total = produto - desconto
print(f'\n Valor do DESCONTO: R$ {desconto} \n Total a PAGAR: R$ {total}')

############## Exercício 06 ##############
print(f'Exercício 6 - Calcular tempo Viagem')
distancia = float(input(f'Informe a DISTÂNCIA a percorrer em Km: '))
velocidade = float(input(f'Informe a VELOCIDADE média Km/h: '))
tempo = distancia/velocidade
print(f'Tempo da VIAGEM: {tempo}h')

############## Exercício 07 ##############
print(f'Exercício 07 - Conversão de TEMPERATURA (Celsius para Fahrenheit)')
c = int(input(f'Informe a TEMPERATURA em graus Celsius: '))
f = 9*c/5+32
print(f'Temperatura em FAHRENHEIT: {f}')

############## Exercício 08 ##############
print(f'Exercício 08 - Conversão de TEMPERATURA (Fahrenheit para Celsius)')
f = int(input(f'Informe a TEMPERATURA em graus FAHRENHEIT: '))
c = 5*f/9+32
print(f'Temperatura em Graus CELSIUS: {c}')


############## Exercício 09 ##############
print(f'Exercício 9 - Preço a pagar')
kmpercorrido =  float(input(f'Informe a quantidade de KM percorridos: '))
qtddias = float(input(f'Informe a quantidade de DIA(S) pelo(s) qual(is) o carro foi alugado: '))
total = (kmpercorrido * 0,15) + (qtddias * 60)
print(f'Preço a PAGAR pela ALOCAÇÃO do veículo: {total}')

############## Exercício 10 ##############
print('Exercício 10 - Tempo de Vida')
qtdCgoDia = int(input('Informe a QUANTIDADE de cigarro(s) fumado(s) por dia: '))
qtdAnsFmu = int(input('Informe a QUANTIDADE de anos que já fumou: '))
ttlPerMin = (qtdCgoDia * (qtdAnsFmu*365)) * 10
totalDias = ttlPerMin / 1440 
print(f'Total em MINUTOS perdido: {ttlPerMin} min')
print('Total em DIAS perdido: {:.2} dias'.format(totalDias))

############## Exercício 11 ##############
print('Exercício 11 - Quantidade de Dígitos')
x = 2**1000000
y = len(str(x))
print(f'Quantidade de dígitos: {y}')
