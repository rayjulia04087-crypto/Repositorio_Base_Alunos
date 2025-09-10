nome = input("Digite o nome do aluno:")
nota1 =float(input("Digite uma nota:"))
nota2 =float(input("Digite uma nota:"))
media = (nota1 + nota2)/2

arquivo = open("Desempenho escolar.txt", "a") 
arquivo.write(nome +"|" + nota1 + nota2 + media "\n")
arquivo.close()