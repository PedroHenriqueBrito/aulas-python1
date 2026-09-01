numero = int(input('Informe um número: '))

resultado = int(numero % 2)

print('Se o resultado for 0 é par e se for 1 é ímpar, o resultado é:', resultado)
#input('Digite ENTER para continuar')

if resultado == 0:
    resultado = 'O número é par'
else:
    resultado = 'O número é ímpar'
print(resultado)

#input('Digite ENTER para continuar')

import subprocess
import os

comando = 'cls' if os.name == 'nt' else 'clear'
subprocess.run(comando, shell=True)

nota = float(input('Informe a nota do estudante: '))

if nota >= 7:
    print('Aprovado')
elif nota >=5:
    print('Recuperação')
else:
    print('Reprovado')