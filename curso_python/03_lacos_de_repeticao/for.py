# %%
nome = 'Victor Ribeiro'

for letra in nome:
    print(letra)

# %%
tabuada = 2
max_numero = 10

for multiplicador in range(1, max_numero + 1):
    print(f'{tabuada} x {multiplicador} = {tabuada * multiplicador}')

# %%
# Quais números são divisiveis por 4
# Em um intervalo de [4-100]

for divisor in range(4, 101):
    if divisor % 4 == 0:
        print(divisor)

# %%
# Faça um programa que receba 4 alturas usando um laço de repetição e realize a soma dessas alturas.

