####################### Exercício 1 #########################

from random import randint
print('Exercício 1 - Maio e Menor Valor')
maior = 0
menor = 100
lista = [randint(1,100) for x in range(10)]
for x in range(10):
    if maior < lista[x]:
        maior = lista[x]
    if menor > lista [x]:
        menor = lista [x]
print(f'Lista: {lista}\nMaior: {maior}\nMenor: {menor}')

####################### Exercício 2 #########################

from random import randint

print('Exercício 2 -  Pares e Impares')

lista = []
listaPar = []
listaImp = []

for x in range(20):
    lista.append(randint(1,100))
    if lista[x] % 2 == 0:
        listaPar.append(lista[x])
    else:
        listaImp.append(lista[x])
print(f'Lista: {lista}\nPares: {listaPar}\nImpares: {listaImp}')

####################### Exercício 3 #########################

from random import randint

print('Exercício 3 - Intercalar Números')

listaA = []
listaB = []
listaC = []

for x in range(10):
    listaA.append(randint(1,100))
    listaB.append(randint(1,100))
    listaC.append(listaA[x])
    listaC.append(listaB[x])
    
print(f'Lista A: {listaA}\nLista B: {listaB}\nLista C: {listaC}')

####################### Exercício 4 #########################

print('Exercício 4 - Lista de Palavras')

texto = 'The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based o mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.'.lower()
texto = texto.replace(',','')
texto = texto.replace('.','')
texto = texto.replace(':','')
lista = texto.split()
listaResult = []

for x in range(len(lista)):
    listaComp = lista[x]
    if listaComp[0] in 'python' or listaComp[-1] in 'python':
        listaResult.append(lista[x])

print(f'\nLista Atualizada: {listaResult}')
print(len(listaResult))

####################### Exercício 5 #########################

print('Exercício 4 - Lista de Palavras')

texto = 'The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based o mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.'.lower()
texto = texto.replace(',','')
texto = texto.replace('.','')
texto = texto.replace(':','')
lista = texto.split()
cont = 0

for x in range(len(lista)):
    listaComp = lista[x]
    if (listaComp[0] in 'python' or listaComp[-1] in 'python') and len(listaComp) > 4:
        cont = cont + 1

print(f'Quantidade: {cont}')
