#Crie um programa que leia um arquivo chamado produtos.csv contendo duas colunas: nome e preço. Imprima no terminal o nome e o preço de cada produto.
import csv

csvfile = open("produtos.csv","w")    
examplecsv = csv.writer(csvfile) 

examplecsv.writerow(["Short Jeans", 79.90])
examplecsv.writerow(["Camisas", 85.90])
examplecsv.writerow(["bodys", 49.99])