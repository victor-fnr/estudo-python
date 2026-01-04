# %%
# *args == conjunto de elementos (lista, tuplas)
# **kwargs == (dicionario)
def calc_imposto(preco:float, tx_base:float, **kwargs):
    imposto = preco * tx_base

    for i in kwargs:
        print(i, kwargs[i])
        imposto += preco * kwargs[i]

    return imposto
# %%

impsotos_gerais = {
    'municipio':0.01,
    'estadual':0.005,
    'nacional':0.001

}

calc_imposto(preco=100, tx_base=0.03, **impsotos_gerais)
