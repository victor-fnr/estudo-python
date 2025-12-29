# Exercício 5 — Validação de entrada
# Solicite ao usuário um número maior que zero.
# Enquanto o valor informado for inválido, continue pedindo um novo número.

# %%


while True:
    num = float(input('Digite um número maior que 0: '))
    if num > 0:
        break
    print('[NÚMERO INVÁLIDO]')

print(num)
    
