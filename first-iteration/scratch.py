from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
import csv

def find_file():
    """Load or create a CSV file to store sales."""
    file = Path("sales.csv")
    try:
        lines = file.read_text().splitlines()
    except FileNotFoundError:
        print("Arquivo não encontrado. Por favor, crie um arquivo primeiro.")
    else:
        df = csv.reader(lines)
        header_row = next(df)
        print(f"Vendas arquivadas: {header_row}")

def get_sales():
    """Ask user for year of reference and monthly sales."""
    months = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
    num_months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    yearly_sales = {}
    # EU TENHO QUE SEPARAR DATA DE VENDAS: UM DIC TIPO 'DATA: '... 'VENDA: ...'
    sales_dates = []
    sales_values = []
    whole_data = {}
    while len(yearly_sales) < len(months):
        date = input("Por favor, insira o ano de referência: ")
        for month, num_month in zip(months, num_months):
            sale = int(input(f"Agora insira o valor bruto em vendas para {month}: "))
            full_date = date + '-' + num_month
            yearly_sales[full_date] = sale
            sales_dates.append(full_date)
            sales_values.append(sale)
        whole_data['DATA'] = sales_dates
        whole_data['VENDAS'] = sales_values
    print(f"\n----------------------\nVendas geradas para o ano {date}:")
    print(f"Vendas geradas:\n{yearly_sales}")
    return whole_data

def save_sales(whole_data):
    """Save user generated sales to the CSV file."""
    sales = whole_data
    answer = input("Você quer salvar as vendas geradas? (s/n)")
    if answer == 'n':
        print("Vendas descartadas.")
    elif answer == 's':
        file = Path("sales.csv")
        if file.exists():
            df = pd.DataFrame(sales)
            df.to_csv('sales.csv', mode='a', index=False, header=False)
        else:
            df = pd.DataFrame(sales)
            df.to_csv('sales.csv', index=False)

def plot_sales(data):
    """Plot a bar graph for given yearly sales."""
