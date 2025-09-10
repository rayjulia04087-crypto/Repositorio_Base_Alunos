mensagem = input("Digite um texto")
teste = input("Digite outro texto")
conteudo = input("Digite um conteudo")

arquivo = open("dados.txt" , "a")
arquivo.write(mensagem + "|" + teste + "|" + conteudo + "\n")

arquivo.close()

