import requests

BASE_URL = "http://127.0.0.1:5000"


def checar_status():
    resposta = requests.get(f"{BASE_URL}/health")
    print("Status do servidor:", resposta.json())


checar_status()