print(f'Exercício 4 - Aumento de Salário')
salario = float(input(f'Informe o valor do SALÁRIO: '))
porcentagem = float(input(f'Informe a PORCETAGEM do aumento: '))
aumento = salario * (porcentagem/100)
novoSalario = salario + aumento
print(f' Valor do AUMENTO: R$ {aumento} n\ Valor do NOVO Salário: R$ {novoSalario}')
