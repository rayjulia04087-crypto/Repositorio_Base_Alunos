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
# Método GET ☝️
