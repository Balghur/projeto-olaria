import packages


def main_loop():
    """Loop to run the program as long as the user wants."""
    prompt = "- 'g': gerar vendas\n- 'v': visualizar vendas"
    prompt += "\n- 's': salvar vendas\n- 'q': sair\n"
    while True:
        answer = input(prompt)
        if answer == "g":
            sales = packages.get_sales()
            continue
        elif answer == "s":
            try:
                packages.save_sales(sales)
            except UnboundLocalError:
                print("\n!!! ERRO!!!\nPor favor gere vendas antes de tentar salvar.\n")
                continue
        elif answer == "v":
            packages.choose_plot_data()
        else:
            print("Obrigado por utilizar o programa.")
            break


print("Bem vindo ao gerenciador de vendas. Selecione uma das opções abaixo.")
main_loop()
