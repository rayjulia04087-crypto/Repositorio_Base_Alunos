#Crie um programa que receba do usuário três nomes e idades, e salve esses dados no arquivo pessoas.csv, com as colunas nome e idade.

import csv # vai pedir para importar a biblioteca csv

nome1 = input("Digite um nome: ")    # vai pedir od nomes 
nome2 = input("Digite outro nome: ")
nome3 = input("Digite mais um nome: ")

idade1 = input("Digite a idade de:" )   # vai pedir as idades
idade2 = input("Digite a idade de:" )
idade3 = input("Digite a idade de:" )

csvfile = open("pessoas.csv","w")    # Abre o arquivo
examplecsv = csv.writer(csvfile) # delimiter = que quero separa igual a que ? Quero separar como ? por , ; ...

examplecsv.writerow(["nomes","idades"])
examplecsv.writerow([nome1,idade1])
examplecsv.writerow([nome2,idade2])
examplecsv.writerow([nome3,idade3])

csvfile.close() # Fecha o Arquivo