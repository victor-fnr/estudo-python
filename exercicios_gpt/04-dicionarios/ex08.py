# %%

# Exercício 8 — Lista de dicionários

# Crie uma lista contendo vários dicionários (por exemplo, cadastro de pessoas).
# Utilize laços para exibir os dados de cada registro.

usuarios = [
    {'Nome':'Victor Ribeiro',
     'Idade':26,
     'Sexo':'Masculino'},

    {'Nome':'Vito Corleone',
     'Idade':54,
     'Sexo':'Masculino'},

    {'Nome':'Michael Corleone',
     'Idade':26,
     'Sexo':'Masculino'},

    {'Nome':'Apollonia Vitelli',
     'Idade':20,
     'Sexo':'Feminino'},

    {'Nome':'Kay Adams',
     'Idade':24,
     'Sexo':'Feminino'},
]

for pessoa in usuarios:
    print('\nRegistro')
    for chave, valor in pessoa.items():
        print(f"{chave}: {valor}")