# %%
# Exercício 9 — Associação de dados
# Utilize duas listas relacionadas (por exemplo, nomes e idades) e gere uma saída combinando os dados corretamente.

nomes = ['Victor', 'Aang']
idades = [26, 10]
for i in range(len(nomes)):
    print(f'{nomes[i]} tem {idades[i]} anos.')

 # %%
print("Cadastro de Usuários (deixe o nome em branco para encerrar)")

nomes = []
idades = []

while True:
    nome = input('Nome: ')
    if not nome:
        break

    try:
        idade = int(input(f'Idade de {nome}: '))
        if not 0 >= idade >= 130:
            print('Idade inválida.')
            continue
        else:
            nomes.append(nome)
            idades.append(idade)
    except:
        print('Valor inserido inválido. Cadastro deste usuário cancelado')
        continue
    
for i in range(len(nomes)):
    print(f'Nome: {nomes[i]} | Idade: {idades[i]} anos')