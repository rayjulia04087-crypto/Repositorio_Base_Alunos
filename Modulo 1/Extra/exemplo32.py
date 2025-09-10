nome = input("Digite o nome da usuario:")
valor = int(input("Digite o valor:"))
quantidade = int(input("Digite uma quantidade"))

with open("produtos.txt", "a") as arquivo:
    arquivo.write(nome +"|" + "\n")