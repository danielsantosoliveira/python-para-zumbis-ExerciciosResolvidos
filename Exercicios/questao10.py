print('Exercício 10 - Tempo de Vida')
qtdCgoDia = int(input('Informe a QUANTIDADE de cigarro(s) fumado(s) por dia: '))
qtdAnsFmu = int(input('Informe a QUANTIDADE de anos que já fumou: '))
ttlPerMin = (qtdCgoDia * (qtdAnsFmu*365)) * 10
totalDias = ttlPerMin / 1440 
print(f'Total em MINUTOS perdido: {ttlPerMin} min')
print('Total em DIAS perdido: {:.2} dias'.format(totalDias))
