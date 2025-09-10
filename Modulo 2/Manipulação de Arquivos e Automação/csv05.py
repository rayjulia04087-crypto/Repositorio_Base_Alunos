#Dado um arquivo clientes.csv, crie um programa que permita adicionar um novo cliente (com nome, email e telefone) sem apagar os dados já existentes.

import csv

with open('clientes.csv', 'a', newline='') as csvfile:
    fieldnames = ['nome', 'email', 'telefone']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writerow({'nome': 'Ana', 'email': 'ana@example.com', 'telefone': '1234-5678'})