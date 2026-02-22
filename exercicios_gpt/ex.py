# %%

usuarios = []

while True:
    nome = input('Nome: ')
    if nome == '':
        break
    
    while True:
        
        try:
            idade = int(input('Idade: '))
            if idade < 0:
                print('Idade inválida!')
                continue
            break
        except ValueError:
            print('Digite um número válido.')
        
    usuarios.append((nome, idade))

menores = 0
maiores = 0
soma_idades = 0

for nome, idade in usuarios:
    
    soma_idades += idade

    if idade < 18:
        menores += 1
    else:
        maiores += 1

if usuarios:
    media = soma_idades / len(usuarios)
else:
    media = 0

print('-----RESUMO FINAL-----')
print(f'''Total de pessoas cadastradas: {len(usuarios)}
Quantidade de menores de idade: {menores}
Quantidade de adultos: {maiores}
Média de idade: {media} anos.''')
