print('Exercício 2 - Troco')
print('Abertura de Caixa')
v100 = int(input('Informe a quantidade de notas de R$ 100,00: '))
cont100 = 0
v50 = int(input('Informe a quantidade de notas de R$ 50,00: '))
cont50 = 0
v20 = int(input('Informe a quantidade de notas de R$ 20,00: '))
cont20 = 0
v10 = int(input('Informe a quantidade de notas de R$ 10,00: '))
cont10 = 0
v5 = int(input('Informe a quantidade de notas de R$ 5,00: '))
cont5 = 0
v2 = int(input('Informe a quantidade de notas de R$ 2,00: '))
cont2 = 0
v1 = int(input('Informe a quantidade de notas de R$ 1,00: '))
cont1 = 0

print('\n\n Captar Valores')
n1 = int(input('Informe o valor total da compra: '))
n2 = int(input('Informe o valor pago, para calcular o troco: '))
while n2 < n1:
    print('O valor pago não pode ser menor que o total da compra.')
    n2 = int(input('Informe o valor pago, para calcular o troco: '))
troco = n2 - n1
contTroco = troco
while contTroco != 0 :
    if v100 != 0 and troco >= 100:
        cont100 = cont100 + 1
        v100 = v100 - 1
        contTroco = contTroco - 100
    elif v50 != 0 and troco >= 50:
        cont50 = cont50 + 1
        v50 = v50 - 1
        contTroco = contTroco - 50
    elif v20 != 0 and troco >= 20:
        cont20 = cont20 + 1
        v20 = v20 - 1
        contTroco = contTroco - 20
    elif v10 != 0 and troco >= 10:
        cont10 = cont10 + 1
        v10 = v10 - 1
        contTroco = contTroco - 10
    elif v5 != 0 and troco >= 5:
        cont5 = cont5 + 1
        v5 = v5 - 1
        contTroco = contTroco - 5
    elif v2 != 0 and troco >= 2:
        cont2 = cont2 + 1
        v2 = v2 - 1
        contTroco = contTroco - 2
    elif v1 != 0 and troco >= 1:
        cont1 = cont1 + 1
        v1 = v1 - 1
        contTroco = contTroco - 1
    else:
        print(f'\nFalta R$ {contTroco:.2f} de troco, pois não há troco suficiente')
        contTroco = contTroco - contTroco
print(f'\n>>> Troco: R$ {troco:.2f}.\n>>Quantidade de notas:\n>Quantidade de 100: {cont100}'
      f'\n>Quantidade de 50: {cont50}\n>Quantidade de 20: {cont20}'
      f'\n>Quantidade de 10: {cont10}\n>Quantidade de 5: {cont5}'
      f'\n>Quantidade de 2: {cont2}\n>Quantidade de 1: {cont1}')
