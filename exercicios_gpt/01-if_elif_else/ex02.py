# Exercício 2 — Comparação de valores
# Peça ao usuário dois números e informe:
# qual é o maior, ou
# se ambos são iguais.

# %%

num_1 = float(input('Digite o primeiro número:'))
num_2 = float(input('Digite o segundo número:'))

if num_1 > num_2:
    print(f'O {num_1} é maior que {num_2}')
elif num_1 < num_2:
    print(f'O {num_2} é meior que {num_1}')
else:
    print('Os números são iguais.')