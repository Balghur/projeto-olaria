# --------------------------------------------------------------------
# Packages I created to calculate and show yearly sales of bricks made
# by a company.
# --------------------------------------------------------------------

import random
import matplotlib.pyplot as plt

def generate_sales_numbers():
    """Generate a list to process as sales for one year."""
    sales = [random.randint(30_000, 100_000) for item in range(12)]
    months = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
    yearly_sales = {}
    for month, sale in zip(months, sales):
        yearly_sales[month] = sale
    return yearly_sales

def visualize_sales(yearly_sales):
    """Generate a graph to visualize sales."""
    plt.bar(range(len(yearly_sales)), list(yearly_sales.values()), align='center')
    plt.xticks(range(len(yearly_sales)), list(yearly_sales.keys()))
    plt.show()

def display_sales_numbers(yearly_sales):
    """Display on terminal sales numbers for each month."""
    print(f"A seguinte lista de vendas foi gerada:")
    for month, sale in yearly_sales.items():
        print(f"{month}: {sale}")
