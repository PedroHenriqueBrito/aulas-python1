#for
for i in range(1, 6):
    print(i)

frutas = ['maça', 'banana', 'uva']
for fruta in frutas:
    print(fruta)

for j in range(1, 11):
    if j == 5:
        continue
    print(j)

for m in range(1, 11):
    if m == 5:
        break
    print(m)

for n in range(1, 11):
    if n == 5:
        continue

    if n == 8:
        break

    print(n)

#while
texto = ''

while texto != 'sair':
    texto = input("Digite algo (ou 'sair' para parar): ")

contador = 1

while contador <= 5:
    print(contador)
    contador += 1

'''while True:
    print('loop infinito uhul')'''

while True:
    try:
        n = int(input('Digite um número: '))
        print(n)
        break
    except ValueError:
        if input("Tentar novamente? (s/n): ").lower() != 's':
            break