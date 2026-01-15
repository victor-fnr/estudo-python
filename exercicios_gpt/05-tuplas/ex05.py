# %%
# Exercício 5 — Verificação de existência
# Verifique se um valor específico existe dentro de uma tupla e exiba uma mensagem apropriada.

numeros = (1, 2, 3, 4, 5, 1, 2, 3, 6, 7, 7, 7)

valor = int(input('Digite um valor: '))

if valor in numeros:
      print(f'o Valor {valor}, existe na tupla {numeros}')
else:
      print(f'o Valor {valor}, não existe na tupla {numeros}')
