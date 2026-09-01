#operadores de comparação
a = 10
b = 5

print(a > b)    #maior que
print(a < b)    #menor que
print(a == b)   #igual
print(a != b)   #diferente
print(a >= b)   #maior ou igual
print(a <= b)   #menor ou igual

#operadores lógicos
numero = 10

print("\nOperadores lógicos")
#No AND o resultado é True somente se os dois lados forem True
print(numero > 5 and numero < 15)

#No OR o resultafo é True se um dos lados for true
print(numero < 5 or numero == 10)

#NOT pega o bool original e nega o valor dele
print(not (numero > 5))
