nome = input ("digite um nome")
while len(nome) < 3:
    print ("nome invalido")


idade = int(input(" digite uma idade"))
while idade <= 0 and idade >= 150:
    print("idade invalida") 


salario = int(input("digite o salario"))
while salario <= 0:
    print("salario invalido")


sexo=input("digite F para feminino or M para masculino")

if sexo =="F" or sexo =="f":
    print("feminino")
elif sexo =="M" or sexo =="m":
    print("masculino")
else:
    print("sexo invalido")