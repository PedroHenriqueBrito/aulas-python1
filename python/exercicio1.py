#1 - Help Desk

#declaração de variáveis
nomeCliente = input('Nome: ')
ticketNumero = input('Informe o número do seu ticket: ')
problemaDescricao = input('Informe o seu problema: ')

#desafios
ticketNumero = int(ticketNumero)
print(type(ticketNumero))

print('Olá {}, seja bem-vindo' . format(nomeCliente.upper()))

print('Caracteres do problema: ', len(problemaDescricao))

#2 - alimentos e bebidas

#declaração de variáveis
nomePrato = input('Digite o nome do prato/drink: ')
qtdIngrediente = input('Informe a quantidade padrão do ingrediente desta porção(em gramas/ml): ')
qtdClientes = input('Quantos clientes serão servidos? ')

qtdIngrediente = float(qtdIngrediente)
qtdClientes = int(qtdClientes)

totalIngrediente = qtdClientes * qtdIngrediente

prato = {
    'Nome': nomePrato,
    'Ingrediente para porção(g/ml)': totalIngrediente
}

print(prato)

#3 - logística

#declaração de variáveis
entregasDiarias = input('Quantas entregas você realizou hoje? ')
entregaGanho = input('Quanto fez por entrega? R$ ')
combustivel = input('Quanto gastou com combustível? R$ ')

ganhoBruto = int(entregasDiarias) * float(entregaGanho)
ganhoLiquido = ganhoBruto - float(combustivel)

print('Seu ganho líquido hoje foi de R${}' . format(ganhoLiquido))

#4 - gestão de atividades

#declaração de variáveis
servicoNome = input('Informe o nome do serviço: ')
servicoTotal = input('Informe o valor total cobrado: R$ ')
servicoHoras = input('Total de horas trabalhadas: ')

ganhoHora = float(servicoTotal) / int(servicoHoras)

tarefas = ['Depurar bugs', 'Criar página de checkout', 'Criar conexão com o DB']
print(tarefas)

projetoStatus = ('Em andamento')
print(projetoStatus)