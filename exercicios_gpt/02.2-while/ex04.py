# %%
# Exercício 4 — Validação de entrada
# Solicite um número maior que zero.
# Enquanto o valor informado for inválido, continue pedindo um novo valor.

while True:
    entrada = input('Digite um número maior que zero ([ENTER] para finalizar): ')
    if entrada == '':
        break

    try:
        valor = float(entrada)
        if valor > 0:
            print(valor)
        else:
            print(f'{valor} não é maior que 0.')
            continue
    except ValueError:
        print('Valor inválido.')
        continue
