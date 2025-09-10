from flask import Flask, jsonify, request

app = Flask(__name__)

frutas = [
    {"id": 1, "nome": "Maca", "cor": "Vermelha"},
    {"id": 2, "nome": "Banana", "cor": "Amarela"},
    {"id": 3, "nome": "Uva", "cor": "Roxa"}
]
@app.route("/frutas", methods=['GET'])
def get_frutas():
    return jsonify({"frutas": frutas, "Total": len(frutas)})

@app.route('/frutas', methods=['POST'])
def add_fruta():
    nova_fruta = request.json()

    nova_fruta["id"] = len(frutas) + 1
    frutas.append(nova_fruta)
    return jsonify({"mensagem": "Fruta adicionada!" , "fruta": nova_fruta}), 201

@app.route('/frutas/<int:id>', methods=['PUT'])
def update_fruta(id):
    dados = request.json

    for fruta in frutas :
        if fruta["id"] == id:
            fruta.update(dados)
            return jsonify({"mensagem": "Fruta atualizada", "fruta": fruta})
    return jsonify({"erro": "Fruta não encontrada"}), 404

@app.route('/frutas/<int:id>', methods=['DELETE'])
def delete_frutas(id):
    for frutas in frutas:
        if frutas["id"] == id:
            frutas.remove(frutas)
            return jsonify({"mensagem": "Musica deletada"}), 200
        
        return jsonify({"erro": Musica não encontrada!}) , 404
                        
if __name__ == "__main__":
    app.run(debug=True)
