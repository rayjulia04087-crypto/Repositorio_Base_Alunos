# Converta esse dicionário em uma string Json usando json.dumps () e imprima:

import json

json_dumps = {"nome": "carlos", "idade":30, "estudante": False}
json_string = json.dumps(json_dumps)
print(json_string)
