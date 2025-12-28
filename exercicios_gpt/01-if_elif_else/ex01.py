# Exercício 1 — Condição simples
# Crie um programa que leia um número inteiro e verifique se ele é positivo, negativo ou zero, exibindo uma mensagem correspondente.

# %%

num = int(input('Digite um número inteiro: '))

if num > 0:
    print(f'O número {num} é positivo.')
elif num == 0:
    print(f'O número {num} é zero.')
else:
    print(f'O número {num} é negativo.')
