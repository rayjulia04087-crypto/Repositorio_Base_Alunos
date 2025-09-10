from flask import Flask, jsonify, request

app = Flask(__name__)

artistas = [
    {"id": 1, "nome": "Queen"},
    {"id": 2, "nome": "Ed Sheeran"}
]

@app.route("/artistas", methods=['GET'])
def get_artistas():
    return jsonify({"artistas": artistas, "Total": len(artistas)})

@app.route('/artistas', methods=['POST'])
def add_artista():
    novo_artista = request.json()
    novo_artista["id"] = len(artistas) + 1
    artistas.append(novo_artista)
    return jsonify({"mensagem": "Artista adicionado!", "artista": novo_artista}), 201

@app.route('/artistas/<int:id>', methods=['GET'])
def get_artista_by_id(id):
    for artista in artistas:
        if artista["id"] == id:
            return jsonify({"mensagem": "Artista encontrado", "artista": artista})
    return jsonify({"mensagem": "Artista não encontrado"}), 404

@app.route('/musica/<int:id>', methods=['PUT'])
def update_musica(id):
    dados = request.json

    for musica in playlist :
        if musica["id"] == id:
            musica.update(dados)
            return jsonify({"mensagem": "musica atualizada", "musica": musica})
    return jsonify({"erro": "musica não encontrada"}), 404

@app.route('/musica/<int:id>', methods=['DELETE'])
def delete_musica(id):
    for musica in playlist:
        if musica["id"] == id:
            playlist.remove(musica)
            return jsonify({"mensagem": "Musica deletada"}), 200 
        
    return jsonify({"erro": "Musica não encontrada"}), 404
