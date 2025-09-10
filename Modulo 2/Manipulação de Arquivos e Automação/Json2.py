import json

pessoa = '{"nome": "carlos", "idade":30, "estudante": false}'
json_string = json.dumps(pessoa)
print(json_string) 