# %%
# Exercício 8 — Lista sem duplicados
# Crie um programa que receba vários valores e gere uma nova lista sem elementos repetidos, preservando a ordem original.

lista_original = []
lista_sem_repetidos = []

while True:
    entrada = input('Digite um número ([ENTER] para finalizar): ')

    if entrada == '':
        break

    try:
        entrada = int(entrada)
    except:
        print('Valor inválido inserido. Tente novamente.')
        continue
    else: 
        lista_original.append(entrada)

for valor in lista_original:
    if valor not in lista_sem_repetidos:
        lista_sem_repetidos.append(valor)

print(f'Lista original: {lista_original}')
print(f'Lista sem números repetidos: {lista_sem_repetidos}')