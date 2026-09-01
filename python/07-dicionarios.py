pessoa = {
    'nome': 'Ana',
    'idade': 30
}

#print(pessoa)
#print(pessoa['nome'])

#alteração de valores
pessoa['idade'] = 31
#print(pessoa)

#adicionando novos valores
pessoa['cidade'] = 'São Paulo'
#print(pessoa)

pessoa['estado'] = 'SP'
#print(pessoa)

#removendo
del pessoa['idade']
#print(pessoa)

pessoa['estado'] = None
print(pessoa)

pessoasNovas = {
    1 : {
        'nome' : 'Vânia',
        'idade' : 50
    },
    2 : {
        'nome' : 'Carlos',
        'idade' : 35
    }
}

print(pessoasNovas)

del pessoasNovas[2]
print(pessoasNovas)

#ver chaves e valores
'''print(pessoasNovas.keys())
print(pessoa.keys())

print(pessoasNovas.values())
print(pessoa.values())'''

paes = {
    'nome1': 'Brioche',
    'tamanho1': 20,
    'nome2': 'Francês',
    'tamanho2': 15   
}

print(paes.items())

print(paes.get('nome1'))

for chave, valor in paes.items():
    print(chave, ':', valor)

bebidas = {
    10: {
        'nome': 'Coca-Cola',
        'volume': 350
    },
    20: {
        'nome': 'Suco de laranja',
        'volume': 1000
    }
}

print(bebidas)
print(bebidas.keys())
print(bebidas.values())
print(bebidas.items())