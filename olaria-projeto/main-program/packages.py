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


def load_data():
    """Loads CSV data to program."""
    file = Path("sales.csv")
    lines = file.read_text().splitlines()
    df = csv.reader(lines)
    header_row = next(df)
    return header_row, df


def get_sales():
    """Ask user for year of reference and monthly sales."""
    months = [
        "janeiro",
        "fevereiro",
        "março",
        "abril",
        "maio",
        "junho",
        "julho",
        "agosto",
        "setembro",
        "outubro",
        "novembro",
        "dezembro",
    ]
    num_months = [
        "01",
        "02",
        "03",
        "04",
        "05",
        "06",
        "07",
        "08",
        "09",
        "10",
        "11",
        "12",
    ]
    yearly_sales = {}
    sales_dates = []
    sales_values = []
    whole_data = {}
    while len(yearly_sales) < len(months):
        date = input("Por favor, insira o ano de referência: ")
        for month, num_month in zip(months, num_months):
            sale = int(input(f"Agora insira o valor bruto em vendas para {month}: "))
            full_date = date + "-" + num_month
            yearly_sales[full_date] = sale
            sales_dates.append(full_date)
            sales_values.append(sale)
        whole_data["DATA"] = sales_dates
        whole_data["VENDAS"] = sales_values
    print(f"\n----------------------\nVendas geradas para o ano {date}:")
    print("Vendas geradas:")
    for date, sale in (whole_data.keys(), whole_data.values()):
        print(f"{date}: {sale}")
    return whole_data


def save_sales(whole_data):
    """Save user generated sales to the CSV file."""
    sales = whole_data
    answer = input("Você quer salvar as vendas geradas? (s/n)")
    if answer == "n":
        print("Vendas descartadas.")
    elif answer == "s":
        file = Path("sales.csv")
        if file.exists():
            df = pd.DataFrame(sales)
            df.to_csv("sales.csv", mode="a", index=False, header=False)
        else:
            df = pd.DataFrame(sales)
            df.to_csv("sales.csv", index=False)


def choose_plot_data():
    """Select year to plot from CSV loaded file."""
    sales_dates = []
    sales_years = []
    sales_values = []
    header_row, df = load_data()
    for date, sales in df:
        sales_dates.append(date)
        sales_values.append(sales)
        years = date[:4]
        if years not in sales_years:
            sales_years.append(years)
    print("Vendas disponíveis para os seguintes anos:")
    for year in sales_years:
        print(year)
    answer = input("Digite o ano de visualização: ")
    plot_dates = []
    plot_values = []
    if answer in sales_years:
        for date, value in zip(sales_dates, sales_values):
            if answer == date[:4]:
                plot_dates.append(date)
                plot_values.append(int(value))
        plt.bar(range(len(plot_dates)), plot_values, align="center")
        plt.xticks(range(len(plot_dates)), list(plot_dates))
        plt.gcf().autofmt_xdate()
        plt.xlabel(header_row[0])
        plt.ylabel(header_row[1])
        plt.tight_layout()
        plt.show()
    else:
        print("Ano não localizado. Por favor selecione um ano válido.")
