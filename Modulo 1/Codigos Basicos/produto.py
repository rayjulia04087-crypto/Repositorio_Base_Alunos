nome= input("digite o nome do produto ")
preco_original= float(input("digite o preco_original"))
valor_desconto= float(input("digite o preco_desconto"))

valor_desconto=preco_original*(valor_desconto/100)
preco_final=preco_original-valor_desconto
print("nome do produto:", nome, "preco_original:", preco_original,"valor_desconto:", valor_desconto,"R$", preco_final)