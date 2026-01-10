# %%
# Exercício 7 — Média de valores
# Solicite valores ao usuário até que ele informe um valor de parada.
# Utilize while para calcular e exibir a média dos valores válidos.

valores = []

while True:
    
    entrada = input('Entre com um valor (0 para encerrar): ')
    
    if entrada == '0':
        break

    try: 
        valor = float(entrada)
        valores.append(valor)
    
    except ValueError:
        print('Valor inválido.')
        continue

if len(valores) > 0:
    media = sum(valores) / len(valores)
    print(f'Valores: {valores}')
    print(f'Média dos valores: {media}')

else:
    print('Nenhum valor inserido.')