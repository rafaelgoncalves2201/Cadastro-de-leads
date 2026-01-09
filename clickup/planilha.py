import pandas as pd

def ler_planilha(caminho_planilha):
    """
    Lê a planilha .xlsx e retorna uma lista de leads únicos
    """
    df = pd.read_excel(caminho_planilha)

    leads = []
    telefones_vistos = set()

    for _, row in df.iterrows():
        telefone = str(row["Telefone"]).strip()

        # Duplicado na própria planilha
        if telefone in telefones_vistos:
            continue

        telefones_vistos.add(telefone)

        leads.append({
            "nome": row["Clientes"],
            "telefone": telefone,
            "origem": row["Origem"],
            "interesse": row["Interesse"]
        })

    return leads
