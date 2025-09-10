def converter_dolar_real(valor):
    return valor * 5.8

def converter_real_dolar(valor):
    return valor / 5.8

converter = int(input("[digite -> 1] -converter_dolar_real: \n[digite -> 2] - converter_real_dolar"))
valor = float(input("digite o valor para ser convertido:"))


if converter == 1:
    print(converter_dolar_real (valor))
elif converter == 2:
    print(converter_real_dolar(valor))
else:
    print()

try:
    converter = int(converter)
    valor = float(valor)
    print(f"digite o valor convertido {convertido}")
except:
    print("Digite o valor correto")
