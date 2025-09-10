def identificar_vogal_consoante(letra):
  letra = letra.upper()  
  vogais = "AEIOU"
  if letra in vogais:
    return "Vogal"
  else:
    return "Consoante"


letra = input("Digite uma letra: ")
resultado = identificar_vogal_consoante(letra)
print(f"A letra '{letra}' é: {resultado}")