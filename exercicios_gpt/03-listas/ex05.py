# %%
# Exercício 5 — Inserção dinâmica
# Solicite números ao usuário e armazene-os em uma lista até que ele informe um valor de parada.
# Ao final, exiba a lista completa.

number_list = []

while True:
    numero = input('Digite um número ([ENTER] para finalizar): ')

    try:
        numero = int(numero)
    except:
        if numero == '':
            break
        else:
            continue
    else:
        number_list.append(numero)

if number_list:
    print(number_list)
else:
    print('Lista vazia.')