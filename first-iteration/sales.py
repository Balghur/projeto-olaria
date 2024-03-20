import scratch

#prompt = "- 'g': gerar vendas\n- 'v': visualizar vendas\n- 's': salvar vendas."
#while True:
#    print("Bem vindo ao gerenciador de vendas. Selecione uma das opções abaixo:")
#    answer = input(prompt)
#    if answer == 'g':
#        sales = packages.get_sales()
#        continue
#    elif answer == 's':
#        packages.save_sales(sales)
#    else:
#        print("Obrigado por utilizar o programa.")
#        break

sales = scratch.get_sales()
scratch.save_sales(sales)
