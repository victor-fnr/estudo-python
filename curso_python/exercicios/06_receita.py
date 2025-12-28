# Faça um programa que exiba a seguinte receita de bolo de chocolate. Exiba um item por vez, conforme a pessoa aperte “enter”.

print('Receita de Bolo')
receita = [
    "Ingredientes:",
    "2 xícaras de farinha de trigo",
    "1 xícara de açúcar",
    "1/2 xícara de cacau em pó",
    "1 colher de chá de fermento em pó",
    "1 colher de chá de bicarbonato de sódio",
    "1/2 colher de chá de sal",
    "2 ovos",
    "1 xícara de leite",
    "1/2 xícara de óleo vegetal",
    "2 colheres de chá de extrato de baunilha",
    "1 xícara de água fervente",
    "",
    "Modo de preparo:",
    "Pré-aqueça o forno a 180°C. Unte uma forma de bolo.",
    "Em uma tigela grande, peneire os ingredientes secos e misture bem.",
    "Em outra tigela, bata os ovos e misture os ingredientes líquidos.",
    "Misture os ingredientes líquidos aos secos.",
    "Adicione a água fervente e misture até ficar homogêneo.",
    "Despeje a massa na forma preparada.",
    "Asse por 30–35 minutos.",
    "Retire do forno e deixe esfriar.",
    "Sirva simples ou com cobertura."
]

for item in receita:
    input("Pressione ENTER para continuar...")
    print(item)