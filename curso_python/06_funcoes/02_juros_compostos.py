# %%

def juros_compostos(anos):
    return 1000 * 1.13 ** anos
#          dinheiro * taxa ** anos

juros_compostos(4)

# %%

def juros_compostos(aporte:int, taxa:float, anos:int)->float:
    '''juros_compostos serve para calcular o retorno financeiro a partir de um aporte
    Deve-se considerar o valor, ataxa de juros atual e o tempo (em anos) para calculo do valor a ser retornado.
    
    :param aporte: um número inteiro que represente o valor em R$.

    :param taxa: um número float entre 0 e 1 que represente o valor da taxa.

    :param anos: um numero inteiro >= 1 que representa o tempo que o investimento terá liquidez.
    '''
    return aporte * (1 + taxa) ** anos

juros_compostos(aporte = 1000, taxa = 0.13, anos = 4)

# %%

print()