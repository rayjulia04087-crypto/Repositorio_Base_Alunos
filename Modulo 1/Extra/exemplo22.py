def imprimir_sequencia(n):
  """
  Imprime a sequência 1 2 2 3 3 3 ... n n n n ... n, até a n-ésima linha.

  Args:
    n: Um valor inteiro que indica até qual linha a sequência deve ser impressa.
  """
  for i in range(1, n + 1):
    for j in range(1, i + 1):
      print(i, end=" ")
    print()

n = int(input("Insira um valor inteiro para n: "))


imprimir_sequencia(n)