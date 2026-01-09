# Cadastro de Leads ClickUp - Web App

## Descrição

Este projeto é um **sistema web** que permite cadastrar leads automaticamente no **ClickUp** a partir de uma planilha Excel (`.xlsx`).  
O aplicativo foi desenvolvido em **Python** usando **Streamlit** e integra diretamente com a **API do ClickUp**.  

O app oferece uma interface simples, moderna e interativa, com banner fixo no topo e efeito de neve (snowfall) na tela.

---

## Funcionalidades

- Upload de planilha `.xlsx` pelo usuário  
- Verificação de leads duplicados no ClickUp e na própria planilha  
- Criação automática de tarefas no ClickUp com dados do lead:  
  - Nome  
  - Telefone  
  - Origem  
  - Interesse  
- Barra de progresso visual durante o processamento  
- Resumo final com métricas: total de leads, cadastrados e duplicados  
- Download do relatório em Excel com abas separadas: **Cadastrados** e **Duplicados**  
- Layout moderno com banner fixo no topo e efeito snowfall  

---

## Tecnologias Utilizadas

- Python 3.10+  
- Streamlit  
- Pandas  
- openpyxl  
- Requests  
- python-dotenv  
- Pillow  

---

## Estrutura do Projeto

projeto/
│
├─ app_web.py # Web app principal (Streamlit)
├─ clickup/
│ ├─ client.py # Funções de integração com ClickUp
│ ├─ planilha.py # Funções para leitura e tratamento da planilha
│
├─ .env # Variáveis de ambiente (CLICKUP_API_TOKEN)
├─ requirements.txt # Dependências Python
└─ README.md


---

## Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto com a seguinte variável:

CLICKUP_API_TOKEN=pk_XXXXXXXXXXXXXX

Substitua `pk_XXXXXXXXXXXXXX` pelo seu token do ClickUp.

---

## Instalação

1. Clone o repositório:

```bash```
git clone https://github.com/seu-usuario/projeto_clickup.git
cd projeto_clickup

Crie um ambiente virtual (opcional, mas recomendado):

python -m venv venv
# Linux/macOS
source venv/bin/activate
# Windows
venv\Scripts\activate

Instale as dependências:

pip install -r requirements.txt

Execute o app Streamlit:

streamlit run app_web.py

Abra o navegador em http://localhost:8501

Faça upload da planilha .xlsx com os leads.

O sistema irá processar os leads, mostrando barra de progresso e resumo final.

Faça download do relatório Excel gerado com os leads cadastrados e duplicados.
