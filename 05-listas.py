frutas = ['maçã', 'banana', 'uva']
print(frutas)

#Ver elementos da lista
print(frutas[0])
print(frutas[1])
print(frutas[2])

#substituindo item
frutas[1] = 'laranja'
print(frutas)

#adicionando itens ao fim da lista 
frutas.append('pêra')
print(frutas)

#adicionar no começo da lista
frutas.insert(0, 'abacaxi')
print(frutas)

#procurando
indice = frutas.index('uva')
print(indice)

if 'uva' in frutas:
    print('Uva está na lista.')

#removendo itens
frutas.remove('uva')
print(frutas)

#tamanho da lista
numeros = [100, 28, 4, 36]
print(len(numeros))

#ordenando
numeros.sort()
print(numeros)

frutas.sort()
print(frutas)

numeros.reverse()
print(numeros)

frutas.reverse()
print(frutas)

#verificar se existe
print(2 in numeros)
print(100 in numeros)

#adicionando múltiplos elementos
numeros = numeros + [10, 20, 30]
numeros.sort()
print(numeros)

#iterando listas
for n in numeros:
    print(n)