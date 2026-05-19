from flask import Flask, request

app = Flask(__name__)

livros = [
    {"id": 1, "titulo": "Dom Casmurro", "autor": "Machado de Assis", "ano": 1899},
    {"id": 2, "titulo": "O Cortico", "autor": "Aluisio Azevedo", "ano": 1890},
]


@app.route("/")
def root():
    return {"mensagem": "API da biblioteca no ar"}


@app.route("/health")
def health():
    return {"status": "ok"}


@app.route("/books")
def listar_livros():
    autor = request.args.get("autor")
    if autor:
        return [l for l in livros if autor.lower() in l["autor"].lower()]
    return livros


@app.route("/books/<int:book_id>")
def buscar_livro(book_id):
    for livro in livros:
        if livro["id"] == book_id:
            return livro
    return {"erro": "livro nao encontrado"}, 404


@app.route("/books", methods=["POST"])
def criar_livro():
    dados = request.get_json()
    novo_id = max([l["id"] for l in livros], default=0) + 1
    novo = {
        "id": novo_id,
        "titulo": dados["titulo"],
        "autor": dados["autor"],
        "ano": dados["ano"],
    }
    livros.append(novo)
    return novo, 201


@app.route("/books/<int:book_id>", methods=["PUT"])
def atualizar_livro(book_id):
    dados = request.get_json()
    for livro in livros:
        if livro["id"] == book_id:
            livro["titulo"] = dados["titulo"]
            livro["autor"] = dados["autor"]
            livro["ano"] = dados["ano"]
            return livro
    return {"erro": "livro nao encontrado"}, 404


@app.route("/books/<int:book_id>", methods=["DELETE"])
def remover_livro(book_id):
    for i, livro in enumerate(livros):
        if livro["id"] == book_id:
            livros.pop(i)
            return {"mensagem": "livro removido"}
    return {"erro": "livro nao encontrado"}, 404


if __name__ == "__main__":
    app.run(debug=True)