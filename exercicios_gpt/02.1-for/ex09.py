# %%
# Exercício 9 — for aninhado
# Utilize dois laços for para exibir:
# uma tabela de multiplicação de 1 a 5.

for i in range(1, 6):
    for j in range(1, 6):
        print(f'{i} x {j} = {i * j:2}  ', end='')
    print()


