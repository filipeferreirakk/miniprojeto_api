import requests

BASE_URL = "http://127.0.0.1:5000"


def checar_status():
    resposta = requests.get(f"{BASE_URL}/health")
    print("Status do servidor:", resposta.json())


def listar_livros():
    resposta = requests.get(f"{BASE_URL}/books")
    livros = resposta.json()
    if not livros:
        print("Nenhum livro cadastrado")
        return
    print("\nLivros cadastrados:")
    for livro in livros:
        print(f"  [{livro['id']}] {livro['titulo']} - {livro['autor']} ({livro['ano']})")


def buscar_livro(book_id):
    resposta = requests.get(f"{BASE_URL}/books/{book_id}")
    if resposta.status_code == 404:
        print("Livro nao encontrado")
        return
    livro = resposta.json()
    print(f"\nEncontrado: {livro['titulo']} de {livro['autor']}, {livro['ano']}")


def cadastrar_livro(titulo, autor, ano):
    payload = {"titulo": titulo, "autor": autor, "ano": ano}
    resposta = requests.post(f"{BASE_URL}/books", json=payload)
    print("Cadastrado:", resposta.json())


checar_status()
cadastrar_livro("Memorias Postumas de Bras Cubas", "Machado de Assis", 1881)
listar_livros()