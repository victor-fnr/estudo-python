# %%
# Exercício 6 — Menu repetitivo
# Crie um menu de opções que se repita com while até o usuário escolher sair.
# Cada opção deve executar uma ação diferente.

while True:
    print("\n--- MENU DE OPERAÇÕES ---")
    print("1. Dizer Olá")
    print("2. Calcular Dobro")
    print("0. Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == '0':
        print("Encerrando o programa... Até logo!")
        break
    
    try:
        if opcao == '1':
            print("Olá! Espero que seus estudos de Python estejam indo bem.")
        
        elif opcao == '2':
            num = float(input("Digite um número para dobrar: "))
            print(f"O dobro de {num} é {num * 2}")
        
        else:
            print("[AVISO] Opção inválida! Escolha 1, 2 ou 0.")
            
    except ValueError:
        print("[ERRO] Para esta opção, você deve digitar um número válido.")
