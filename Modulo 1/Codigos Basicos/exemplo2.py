valor_desconto=int(input("Digite o valor desconto"))
preco_original=int(input("Digite o preco original"))
preco_final=int(input("Digite o preco final"))

valor_desconto=preco_original*(valor_desconto/100)
preco_final=preco_original-valor_desconto
print(preco_final)