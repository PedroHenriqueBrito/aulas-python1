#comentário de uma linha
 
''' comentários: auxiliam
a deixar
"anotações" no código fonte'''
 
# concatenação
print('Boas vindas a aula de' + ' Python!')
 
# interpolação
#print('Olá {}' . format(input('Qual o seu nome? ')))
 
#tipo de dados em python - números
# Inteiro
idade = 30
print(idade)
 
# Decimal (float)
altura = 1.75
print(altura)

# Número complexo
numero_complexo = 2 + 3j
print(numero_complexo)

#texto(str)
nome = 'Ana Cláudia'
print(nome)

#boolean(bool)
ativo = True
print(ativo)

logado = False
print(logado)

#nenhum valor (NoneType)
valor = None
print(valor)

#Lista(list) mutável
frutas = ['maçã', 'banana', 'uva']
print(frutas)

#tupla(tuple) imutável
cores = ('vermelho', 'azul', 'verde')
print(cores)

#conjunto(set)
numeros = {1, 2, 3, 4}
print(numeros)

#Dicionário(dict) pares chave-valor
pessoa = {
    'nome': 'Ana',
    'idade': 30
}
print(pessoa)

'''Python não possui constantes
verdadeiras, mas usamos uma convenção
para indicar que um valor não deve ser alterado.'''
PI = 3.14159
GRAVIDADE = 9.8

print('O valor de pi é', PI, '\nO valor da aceleração da gravidade terrestre é', GRAVIDADE, 'm/s²')
