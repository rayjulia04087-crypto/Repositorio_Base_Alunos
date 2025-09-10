#Utilize a função csv.DictReader para ler um arquivo alunos.csv com as colunas nome, nota1 e nota2. Calcule a média de cada aluno e imprima no terminal.
import csv

with open("pessoas.csv", "w") as csvfile:  # Abre o arquivo pessoas.csv para escrever o que eu quero
    writer = csv.writer(csvfile) # Cria um objeto writer pra escrever
    writer.writerow(['nome', 'nota1', 'nota2'])  # escreve os nomes
    writer.writerow(['Lucas', '7.5', '8'])       
    writer.writerow(['Marina', '9', '8.5'])    
    writer.writerow(['Pedro', '6.5', '7'])       
with open("pessoas.csv", "r") as csvfile: # Abre o arquivo para ler
    reader = csv.DictReader(csvfile)  # Cria um objeto DictReader para ler as linhas que eu escrevi.
    for row in reader:  # Interaje sobre cada linha do arquivo
        nome = row['nome'] # Pega o nome
        nota1 = float(row['nota1']) # nota1
        nota2 = float(row['nota2']) # nota2
        media = (nota1 + nota2) / 2  # Calcula a média




