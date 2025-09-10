# Crie um programa que gere um arquivo relatorio.csv com cabeçalho produto, quantidade e total. Os dados devem ser calculados a partir de uma lista de dicionários no próprio código.

import csv

with open('relatorio.csv', 'w') as csvfile:
    fieldnames = ['Produto', 'Quantidade', 'Total']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'Produto': 'Laranja', 'Quantidade': 1, 'Total': 5.99})
    writer.writerow({'Produto': 'Bolo', 'Quantidade': 2, 'Total': 15.98})
    writer.writerow({'Produto': 'Refrigerante', 'Quantidade': 3, 'Total': 17.00})