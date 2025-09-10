#Use o modulo json para converter a string Json  abaixo em um dicionário Python e imprima o resultado.
import json

json_string = '{"nome": "Ana", "idade": 25, "estudante": true}'
pessoa = json.loads(json_string)
print("nome:", pessoa['nome'], "idade:", pessoa['idade'], "estudante:", pessoa['estudante'])