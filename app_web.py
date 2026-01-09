import streamlit as st
from clickup.planilha import ler_planilha
from clickup.client import criar_tarefa, lead_ja_existe
from PIL import Image
from streamlit.components.v1 import html
import base64
import pandas as pd
from io import BytesIO
import time

LIST_ID = "901324135542"

# --------------------- Layout da página ---------------------
st.set_page_config(page_title="Cadastro de Leads ClickUp", layout="wide")

# Caminho da imagem do banner
banner_path = r"C:\Users\Rafael Goncalves\OneDrive\Área de Trabalho\Automação Empresas\Logo Inovaeweb.png"

# Carrega a imagem e converte para base64
with open(banner_path, "rb") as f:
    data = f.read()
banner_base64 = base64.b64encode(data).decode()

# --------------------- CSS para banner fixo ---------------------
st.markdown(
    f"""
    <style>
    /* Banner fixo na parte superior */
    .banner {{
        position: fixed;
        top: 100px;
        left: 0;
        width: 100%;
        height: 150px; /* altura do banner, ajuste se necessário */
        background-image: url("data:image/png;base64,{banner_base64}");
        background-size: cover;
        background-position: center;
        z-index: 1000;
    }}

    /* Espaço no topo para não cobrir o conteúdo */
    .main-content {{
        padding-top: 130px; /* altura do banner + 10px de margem */
    }}
    </style>

    <div class="banner"></div>
    <div class="main-content"></div>
    """,
    unsafe_allow_html=True
)

# ------------------- Snowfall -------------------
html(
    """
    <canvas id="snowfall" style="position:fixed;top:0;left:0;width:100%;height:100%;pointer-events:none;z-index:9999;"></canvas>
    <script>
    const canvas = document.getElementById('snowfall');
    const ctx = canvas.getContext('2d');
    let width = canvas.width = window.innerWidth;
    let height = canvas.height = window.innerHeight;

    const snowflakes = [];
    for(let i=0;i<200;i++){
        snowflakes.push({
            x: Math.random()*width,
            y: Math.random()*height,
            r: Math.random()*4+1,
            d: Math.random()*1
        });
    }

    function draw(){
        ctx.clearRect(0,0,width,height);
        ctx.fillStyle = "white";
        ctx.beginPath();
        for(let i=0;i<snowflakes.length;i++){
            const f = snowflakes[i];
            ctx.moveTo(f.x,f.y);
            ctx.arc(f.x,f.y,f.r,0,Math.PI*2,true);
        }
        ctx.fill();
        update();
    }

    let angle = 0;
    function update(){
        angle += 0.01;
        for(let i=0;i<snowflakes.length;i++){
            const f = snowflakes[i];
            f.y += Math.cos(angle + f.d) + 1 + f.r/2;
            f.x += Math.sin(angle) * 2;
            if(f.y > height){
                f.y = 0;
                f.x = Math.random()*width;
            }
        }
    }

    setInterval(draw, 33);

    window.addEventListener('resize', ()=>{
        width = canvas.width = window.innerWidth;
        height = canvas.height = window.innerHeight;
    });
    </script>
    """,
    height=0
)

st.title("Cadastro de Leads")
st.markdown(
    """
    Carregue sua planilha `.xlsx`. 
    O sistema processará os leads e exibirá o resumo final ao concluir.
    """
)

# --------------------- Upload de planilha ---------------------
uploaded_file = st.file_uploader("Selecione a planilha (.xlsx)", type="xlsx")

if uploaded_file:
    try:
        leads = ler_planilha(uploaded_file)
        st.info(f"{len(leads)} leads únicos encontrados na planilha.")

        cadastrados = []
        duplicados = []

        # Barra de progresso
        progress_text = st.empty()
        progress_bar = st.progress(0)

        total = len(leads)
        for i, lead in enumerate(leads):
            telefone = lead["telefone"]

            if lead_ja_existe(LIST_ID, telefone):
                duplicados.append(lead)
            else:
                nome_tarefa = f"Lead - {lead['nome']}"
                descricao = (
                    f"Telefone: {telefone}\n"
                    f"Origem: {lead['origem']}\n"
                    f"Interesse: {lead['interesse']}"
                )
                tarefa = criar_tarefa(
                    list_id=LIST_ID,
                    nome=nome_tarefa,
                    descricao=descricao
                )
                cadastrados.append({**lead, "task_id": tarefa["id"]})

            # Atualiza barra de progresso
            progress_text.text(f"Processando {i+1}/{total} leads...")
            progress_bar.progress((i+1)/total)
            time.sleep(0.05)  # pequena pausa visual

        progress_text.text("Processamento finalizado!")
        progress_bar.progress(1.0)

        # --------------------- Resumo final ---------------------
        st.markdown("## Resumo Final")
        col1, col2, col3 = st.columns(3)
        col1.metric("Total de Leads", len(leads))
        col2.metric("Leads Cadastrados", len(cadastrados))
        col3.metric("Duplicados/Existentes", len(duplicados))

        # --------------------- Download Excel ---------------------
        if cadastrados or duplicados:
            output = BytesIO()
            with pd.ExcelWriter(output, engine='openpyxl') as writer:
                pd.DataFrame(cadastrados).to_excel(writer, sheet_name="Cadastrados", index=False)
                pd.DataFrame(duplicados).to_excel(writer, sheet_name="Duplicados", index=False)
            output.seek(0)
            st.download_button(
                label="Baixar relatório Excel",
                data=output,
                file_name="relatorio_leads.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

    except Exception as e:
        st.error(f"Erro ao processar a planilha: {e}")
