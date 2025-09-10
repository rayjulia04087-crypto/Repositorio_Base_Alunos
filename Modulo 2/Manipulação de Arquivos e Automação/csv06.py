#Crie um programa que leia o arquivo vendas.csv e exiba apenas as vendas com valor acima de R$ 1.000,00. O CSV tem as colunas: cliente, produto, valor.
import csv # aqui importa o csv


csvfile = open("vendas.csv","w")    # Abre o arquivo
examplecsv = csv.writer(csvfile)  #exemplo de como escrever no arquivo csv

examplecsv.writerow(["cliente", "produto", "valor"]) #como eu quero separar os valores
examplecsv.writerow(["João", "Notebook", 3500])
examplecsv.writerow(["Ana", "Mouse", 80])
examplecsv.writerow(["Carlos", "Monitor", 1200])


csvfile = open("vendas.csv","r") # Abre o arquivo para leitura
reader = csv.DictReader(csvfile) #Cria um Dicionário para ler o CSV
for row in reader: # Interage sobre cada linha do arquivo
    if float(row['valor']) > 1000.00: # Verifica se o valor é maior que 1000
            print([row['valor']])
    else:
            print("Nenhuma venda acima de R$ 1.000,00 encontrada.")
            print(f"Cliente: {row['cliente']}, Produto: {row['produto']}, Valor: R$ {row['valor']}")
                  # o f serve para formatar a string de saída