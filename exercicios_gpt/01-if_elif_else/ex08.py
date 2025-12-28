# Exercício 8 — Classificação de triângulos
# Peça três valores representando os lados de um triângulo.
# Verifique:
# se é possível formar um triângulo;
# se for possível, classifique-o como:
# equilátero,
# isósceles,
# escaleno.

# %%


lado_a = float(input('Digite o valor do lado a: '))
lado_b = float(input('Digite o valor do lado b: '))
lado_c = float(input('Digite o valor do lado c: '))

if lado_a <= 0 or lado_b <= 0 or lado_c <=0:
    print("Valores inválidos. Lados devem ser positivos.")

elif (lado_a + lado_b > lado_c) and (lado_b + lado_c > lado_a) and (lado_c + lado_a > lado_b):
    if lado_a == lado_b == lado_c:
        print('Triângulo equilátero')
    elif (lado_a == lado_b) or (lado_b == lado_c) or (lado_c == lado_a) :
        print('Triângulo isósceles')
    else:
        print('Triângulo escaleno')

else:
    print('Não é possível formar um triângulo.')