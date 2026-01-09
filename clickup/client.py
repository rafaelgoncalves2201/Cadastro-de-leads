import requests
import os
from dotenv import load_dotenv

load_dotenv()

CLICKUP_TOKEN = os.getenv("CLICKUP_API_TOKEN")
if not CLICKUP_TOKEN:
    raise Exception("CLICKUP_API_TOKEN não carregado. Verifique o .env")

HEADERS = {
    "Authorization": CLICKUP_TOKEN,
    "Content-Type": "application/json"
}
BASE_URL = "https://api.clickup.com/api/v2"

def criar_tarefa(list_id, nome, descricao=None, status=None):
    url = f"{BASE_URL}/list/{list_id}/task"
    payload = {"name": nome, "description": descricao}
    if status:
        payload["status"] = status
    response = requests.post(url, headers=HEADERS, json=payload)
    response.raise_for_status()
    return response.json()

def lead_ja_existe(list_id, telefone):
    """
    Verifica se já existe tarefa com o telefone no nome ou custom field
    """
    # Pega as tarefas da lista
    url = f"{BASE_URL}/list/{list_id}/task"
    params = {"page": 0}  # pode paginar se necessário
    response = requests.get(url, headers=HEADERS, params=params)
    response.raise_for_status()
    tasks = response.json().get("tasks", [])
    for t in tasks:
        if telefone in t.get("name", "") or telefone in (t.get("description") or ""):
            return True
    return False
