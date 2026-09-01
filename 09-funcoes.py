try:
    numero = int(input("Digite um número: "))
    print(numero)
except:
    print("Inválido")

#try except com else e finally
try: 
    numero = float(input("Digite um número: "))
except ValueError:
    print("Erro: entrada inválida")
else:
    print("Você digitou: ", numero)
finally:
    print('Programa finalizado')

#exemplo de função com try e except
def dividir(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Erro: divisão por zero"

print(dividir(10, 2))
print(dividir(10, 0))

a = float(input('Digite o primeiro número: '))
b = float(input('Digite o segundo número: '))
print(dividir(a, b))