ListaNumeroReais = []

print("informe os 10 numeros reais")

for i in range(10):
    ListaNumeroReais.append(float(input("numero"+ str(i+1)+":")))
ListaNumeroReais.reverse()

print(ListaNumeroReais)