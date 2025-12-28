# Exercício 3 — Par ou ímpar
# Leia um número inteiro e determine se ele é par ou ímpar usando estruturas condicionais.

# %%

num = int(input('Digite um número inteiro'))

if num % 2 == 0:
    print(f'O número {num} é par')
else:
    print(f'O número {num} é ímpar.')