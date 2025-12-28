# Faça um programa que receba um número inteiro e calcule sua raiz quadrada e exiba o resultado.

numero = int(input('Digite um número inteiro para calcular a sua raiz quadrada: '))
raiz = numero ** 0.5
raiz = round(raiz, 4)

print(f'A raiz de {numero} é: {raiz}')