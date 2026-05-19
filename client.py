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


checar_status()
listar_livros()