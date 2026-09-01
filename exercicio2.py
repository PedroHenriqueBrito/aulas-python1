#1 - Manicure
nome = input("Digite o nome da cliente: ")
qtd_decoradas = int(input("Digite a quantidade de unhas decoradas: "))
 
# Valores
 
valor_simples = 30.00
valor_total = valor_simples + (qtd_decoradas * 2)
 
# Saída de dados
print("Nome da cliente:", nome.upper())
print(f"Valor total a pagar: R$ {valor_total:.2f}")
print("Quantidade de caracteres do nome:", len(nome))

#2 - Lava a Jato
LAVAGEMSIMPLES = 25.0
LAVAGEMCOMPLETA = 50.0

nomeCliente = input('Cliente: ')
tipoLavagem = input('Informe o tipo de lavagem(1 para simples e 2 para completa): ')

tipoLavagem = int(tipoLavagem)

if tipoLavagem == 1:
    print('Lavagem Simples - R${:.2f}' . format(LAVAGEMSIMPLES))
elif tipoLavagem == 2:
    print('Lavagem Completa - R${:.2f}' . format(LAVAGEMCOMPLETA))
else:
    print('Tipo Inválido')

#3 - Estacionamento
HORA = 5.0

nomeMotorista = input('Nome do motorista: ')
horasMotorista = input('Tempo de estacionamento: ')

valorTotal = HORA * float(horasMotorista)

if valorTotal > 30:
    valorTotal = valorTotal * 0.9
    print('O cliente recebeu 10% de desconto!')

print(f'O valor a ser cobrado é de R$ {valorTotal:.2f}')

#4 - Escola infantil
nome = input('Nome do(a) aluno(a):' )
idade = input('Idade do(a) aluno(a): ')
idade = int(idade)
tipoMatricula = ''

if idade >=3 & idade <= 4:
    tipoMatricula = 'Maternal'
elif idade >=5 & idade <=6:
    tipoMatricula = 'Jardim'
elif idade >=8 & idade <=7:
    tipoMatricula = 'Pré-Escola'
else:
    tipoMatricula = 'Fora da faixa atendida'

print("Nome do(a) aluno(a):", nome.upper(), "\n", nome.lower())
print(f"Idade: {idade} anos")
print(tipoMatricula)
print("Quantidade de caracteres do nome:", len(nome))

#5 - Pastelaria
PASTELQUEIJO = 8.0
PASTELCARNE = 9.0

qtdQueijo = int(input('Quantos pastéis de queijo foram comprados? '))
qtdCarne = int(input('Quantos pastéis de carne foram comprados? '))

qtdTotal = qtdQueijo + qtdCarne

valorTotal = (PASTELQUEIJO * qtdQueijo) + (PASTELCARNE + qtdCarne)

print(f'Total: R${valorTotal:.2f}')

print('Pastéis vendidos: ', qtdTotal)
if qtdTotal > 10:
    print('Mais de 10 pastéis vendidos!')

#6 - Casa de tintas
cores = ["Azul", "Branco", "Verde", "Amarelo"]

if "Verde" in cores:
  print("Cor disponível em estoque")
else:
  print("Cor indisponível")

print("Cores ordenadas:", sorted(cores))
print("Quantidade de cores:", len(cores))