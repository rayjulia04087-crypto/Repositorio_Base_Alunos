from flask import Flask, jsonify, request

app = Flask(__name__)

playlist = [

    {"id": 1, "title": "Bohemian Rhapsody", "artist": "Queen"},
    {"id": 2, "title": "Shape of You", "artist": "Ed Sheeran"}
]
#Criamos o banco de dados 👌
@app.route("/musicas", methods=['GET']) # nossa rota Pode ser a mesma coisa mas com metodo diferente
def get_musicas(): # def função do python no caso get musicas
    return jsonify({"playlist": playlist, "Total": len(playlist)}) # quantas musicas tem dentro da playlist ?
 
if __name__ == ' __main__ ':
    app.run(debug-True)