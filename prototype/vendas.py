# --------------------------------------------------------------------
# Program to run on a terminal and show user yearly sales.
# --------------------------------------------------------------------

import packages

active = True
boas_vindas = "Bem vindo ao visualizador de vendas."
boas_vindas += "Por favor selecione uma das opções abaixo:"
operacao = "- Sair: 'q'\n- Gerar vendas: 'g'\n-Visualizar vendas: 'v'\n"

vendas = {}
print(boas_vindas)
while active:
    answer = input(operacao)
    if answer == "q":
        active = False
    elif answer == "g":
        vendas = packages.generate_sales_numbers()
        packages.display_sales_numbers(vendas)
        continue
    elif answer == "v":
        if len(vendas) < 10:
            print(
                "\n---!!!---\nERRO: Por favor gere dados antes de tentar visualizar.\n---!!!---\n"
            )
            continue
        else:
            packages.visualize_sales(vendas)
            continue
    else:
        print(
            "\n---!!!---\nERRO: Selecione uma das opções disponíveis abaixo.\n---!!!---\n"
        )
        continue
