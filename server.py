from flask import Flask

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


if __name__ == "__main__":
    app.run(debug=True)