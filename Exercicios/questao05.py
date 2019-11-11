print(f'Exercício 5 - Desconto Produto')
produto = float(input(f'Informe o PREÇO do produto: '))
percentual = float(input(f'Informe o PERCENTUAL de desconto: '))
desconto = produto * (percentual/100)
total = produto - desconto
print(f'\n Valor do DESCONTO: R$ {desconto} \n Total a PAGAR: R$ {total}')
