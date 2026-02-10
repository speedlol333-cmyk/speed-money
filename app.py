import streamlit as st

# Configuração Master
st.set_page_config(page_title="Speed Money Pro", page_icon="💰", layout="wide")

# --- CONTROLE DE ZOOM REAL ---
st.sidebar.markdown("### 🔍 Ajuste de Leitura")
# Criamos um multiplicador que afetará todas as fontes
zoom_factor = st.sidebar.slider("Aumentar/Diminuir Zoom", min_value=0.8, max_value=2.5, value=1.0, step=0.1)

# Estilo com Injeção de CSS Dinâmico
st.markdown(f"""
    <style>
    /* Base de cálculo para o zoom */
    html, body, [data-testid="stWidgetLabel"], .stMarkdown p, .stMarkdown li {{
        font-size: {18 * zoom_factor}px !important;
        line-height: 1.6 !important;
    }}
    
    /* Zoom nos Títulos */
    h1 {{ 
        font-size: {50 * zoom_factor}px !important; 
        color: #1B4D3E; 
        text-align: center; 
        border-bottom: 3px solid #D4AF37; 
    }}
    
    h2 {{ 
        font-size: {35 * zoom_factor}px !important; 
        color: #8B4513; 
        border-left: 5px solid #D4AF37; 
        padding-left: 15px; 
    }}
    
    h3 {{ 
        font-size: {25 * zoom_factor}px !important; 
    }}

    /* Ajuste de imagens para não estourarem no zoom */
    img {{
        max-width: 100%;
        height: auto;
    }}

    .stCheckbox label {{
        font-size: {18 * zoom_factor}px !important;
    }}
    </style>
    """, unsafe_allow_html=True)

st.title("💰 SPEED MONEY")

# --- NAVEGAÇÃO ---
menu = st.sidebar.radio("📚 Capítulos", 
    ["Início", "1. Mentalidade & Gestão", "2. Freelancer de Elite", "3. Vendas & E-commerce", "4. Máquina de Afiliados", "5. Império de Conteúdo"])

if menu == "Início":
    st.image("https://images.unsplash.com/photo-1553729459-efe14ef6055d?auto=format&fit=crop&w=1000&q=80")
    st.markdown("## Comece Aqui")
    st.write("Use o controle deslizante à esquerda para ajustar o tamanho do texto conforme sua preferência.")
    st.write("Este guia foi criado para ser acessível a todos. Se o texto estiver pequeno, arraste o controle de zoom para a direita.")

elif menu == "1. Mentalidade & Gestão":
    st.header("Capítulo 1: Domando o Dinheiro")
    st.image("https://images.unsplash.com/photo-1554224155-6726b3ff858f?auto=format&fit=crop&w=800&q=80")
    st.write("### O Passo a Passo Técnico")
    st.markdown("""
    1. **Mapeamento:** Anote tudo o
