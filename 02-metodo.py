#calculos
num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

soma = int(num1) + int(num2)
subtracao = int(num1) - int(num2)
divisao = int(num1) / int(num2)
moduloresto = int(num1) % int(num2)
multiplicacao = int(num1) * int(num2)
potenciacao = int(num1) ** int(num2)

print(soma)
print(subtracao)
print(divisao)
print(moduloresto)
print(multiplicacao)
print(potenciacao)

#o comando type retorna o tipo da variável
print(type(num1))
#print(type(num2))
print(type(soma))
'''print(type(subtracao))
print(type(divisao))
print(type(moduloresto))
print(type(multiplicacao))
print(type(potenciacao))'''

#Calcular área
lado1 = input('Informe o primeiro lado: ')
lado2 = input('Informe o segundo lado: ')

area = float(lado1) * float(lado2)

print('A área do quadrado é: {} m²' . format(area))

nomeCompleto = input('Informe o seu nome completo: ')
# função len retorna a quantidade de caracteres de uma variável
print('1. Quantidade de caracteres:', len(nomeCompleto))

# upper = todas maísculas
# lower = todas minúsculas
# capitalize = só a primeira letra maíscula
print('2. Nome em maísculo:', nomeCompleto.upper())
print('3. Nome em minúsculo:', nomeCompleto.lower())
print('4. Primeira letra em maísculo:', nomeCompleto.capitalize())