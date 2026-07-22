from flask import Flask, jsonify

app = Flask(__name__)

produtos = [
    {"id": 1, "nome": "Notebook", "preco": 3500.00, "disponivel": True},
    {"id": 2, "nome": "Mouse", "preco": 80.00, "disponivel": True},
    {"id": 3, "nome": "Teclado", "preco": 150.00, "disponivel": False},
    {"id": 4, "nome": "Monitor", "preco": 1200.00, "disponivel": True}
]

@app.route("/produtos")
def listar_produtos():
    return jsonify(produtos)

@app.route("/produtos/<int:id>")
def buscar_produto(id):
    for p in produtos:
        if p["id"] == id:
            return jsonify(p)
    return jsonify({"erro": "Produto nao encontrado"}), 404

if __name__ == "__main__":
    app.run(debug=True)