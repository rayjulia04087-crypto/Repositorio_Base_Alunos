mensagem = input("Digite um texto")
teste = input("Digite outro texto")

arquivo = open("dados.txt" , "w")
arquivo.write(mensagem + "|" + teste +"\n")

arquivo.close()

