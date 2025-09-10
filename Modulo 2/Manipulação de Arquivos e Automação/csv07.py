#Dado um arquivo compras.csv com a coluna categoria, conte e mostre quantas vezes cada categoria aparece.

import csv

categoria_contagem = {}

with open('compras.csv', 'r') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        categoria = row['categoria']
        if categoria in categoria_contagem:
            categoria_contagem[categoria] += 1
        else:
            categoria_contagem[categoria] = 1
   


