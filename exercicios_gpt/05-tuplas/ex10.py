# %%
# Exercício 10 — Análise de dados
# Crie um programa que utilize tuplas para armazenar dados fixos (ex.: produtos, códigos, preços) e:
# percorra os dados,
# aplique regras de validação,
# gere um resumo ou relatório.

produtos = (
    (101, "Notebook", 3500.00),
    (102, "Mouse", 150.00),
    (103, "Teclado", -200.00),   # preço inválido
    (104, "Monitor", 0.00),      # preço inválido
    (105, "Cadeira", 800.00)
)


produtos_validos = 0
valor_total = 0
produtos_invalidos = []

for code, nome, preço in produtos:
      if preço > 0:
            produtos_validos += 1
            valor_total += preço
      else:
            produtos_invalidos.append((code, nome, preço))

print('RELATÓRIO DE ANÁLISE DE PRODUTOS')
print('-' * 35)

print(f'Produtos válidos: {produtos_validos}')
print(f'Valor total dos produtos válidos: R$ {valor_total:.2f}')


print('\nProdutos inválidos:')
if produtos_invalidos:
      for code, nome, preço in produtos_invalidos:
            print(f'- Código: {code} | Produto: {nome} | Preço: {preço}')
else:
      print('Nenhum produto inválido encontrado.')