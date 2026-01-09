Cadastro de Leads ClickUp - Web App
Descrição

Este projeto é um sistema web para cadastrar leads diretamente no ClickUp a partir de uma planilha Excel (.xlsx). O app permite:

Upload de planilha pelo usuário

Verificação de leads duplicados no ClickUp

Criação automática de tarefas para leads novos

Resumo final com total de leads, cadastrados e duplicados

Download do relatório Excel com leads cadastrados e duplicados

Layout web moderno com banner fixo e efeito snowfall

O sistema é construído usando Python, Streamlit e a API do ClickUp.

Funcionalidades

Upload de planilha: permite enviar um arquivo .xlsx com os leads.

Verificação de duplicados: não cadastra leads que já existem no ClickUp ou na própria planilha.

Cadastro automático no ClickUp: cria tarefas com nome, telefone, origem e interesse.

Resumo visual: exibe métricas do processo (total, cadastrados, duplicados).

Download do relatório: gera Excel com duas abas — Cadastrados e Duplicados.

Interface atrativa: banner fixo e snowfall caindo pela tela.

Tecnologias

Python 3.10+

Streamlit

Pandas

openpyxl

Requests

ClickUp API

Estrutura do Projeto
projeto_clickup/
│
├─ app_web.py              # Web app principal (Streamlit)
├─ clickup/
│   ├─ client.py           # Funções de integração com ClickUp
│   ├─ planilha.py         # Funções para leitura e tratamento da planilha
│
├─ .env                    # Variáveis de ambiente (CLICKUP_API_TOKEN)
├─ requirements.txt        # Dependências Python
└─ README.md

Variáveis de Ambiente

No arquivo .env, adicione:

CLICKUP_API_TOKEN=pk_XXXXXXXXXXXXXX

Instalação

Clone o repositório:

git clone https://github.com/seu-usuario/projeto_clickup.git
cd projeto_clickup


Crie um ambiente virtual (opcional, mas recomendado):

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows


Instale as dependências:

pip install -r requirements.txt


Dependências principais: streamlit, pandas, openpyxl, requests, python-dotenv, Pillow

Uso

Execute o app Streamlit:

streamlit run app_web.py


Acesse no navegador: http://localhost:8501

Faça upload da planilha .xlsx.

O sistema irá processar os leads, mostrar progresso e resumo final.

Faça download do relatório Excel gerado.

Formato da Planilha

A planilha deve ter as seguintes colunas:

Clientes	Telefone	Origem	Interesse
João Silva	11999999999	WhatsApp	Site
Maria Souza	11988888888	Instagram	Serviço
Personalização

Banner: substitua a imagem no banner_path do app_web.py.

Altura do banner: ajuste o height no CSS.

Neve (snowfall): configure quantidade, velocidade e tamanho no JavaScript do app.

Lista ClickUp: altere LIST_ID no app_web.py para a lista desejada.
