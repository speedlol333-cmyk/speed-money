import streamlit as st

# Configuração Master
st.set_page_config(page_title="Speed Money Pro", page_icon="💰", layout="wide")

# Estilo de Livro Premium
st.markdown("""
    <style>
    .main { background-color: #FDFBF7; }
    h1 { color: #1B4D3E; font-family: 'Playfair Display', serif; font-size: 55px; text-align: center; margin-bottom: 30px; border-bottom: 3px solid #D4AF37; }
    h2 { color: #8B4513; border-left: 5px solid #D4AF37; padding-left: 15px; margin-top: 30px; }
    .stProgress > div > div > div > div { background-color: #D4AF37; }
    .task-done { color: #2E7D32; font-weight: bold; }
    .card { background-color: #ffffff; padding: 25px; border-radius: 15px; border: 1px solid #e0e0e0; box-shadow: 5px 5px 15px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_html=True)

st.title("💰 SPEED MONEY")
st.subheader("O seu guia interativo para a liberdade financeira")

# --- BARRA DE PROGRESSO GERAL ---
st.sidebar.markdown("### 📊 Seu Progresso")
progresso = st.sidebar.slider("Quantos capítulos você já concluiu?", 0, 5, 0)
st.sidebar.progress(progresso * 20)

# --- NAVEGAÇÃO ---
menu = st.sidebar.radio("📚 Capítulos", 
    ["Início", "1. Mentalidade & Gestão", "2. Freelancer de Elite", "3. Vendas & E-commerce", "4. Máquina de Afiliados", "5. Império de Conteúdo", "🧮 Simulador de Ganhos"])

if menu == "Início":
    st.image("https://images.unsplash.com/photo-1553729459-efe14ef6055d?auto=format&fit=crop&w=1000&q=80")
    st.markdown("""
    ## Comece Aqui
    Este aplicativo foi desenhado para ser o seu mentor silencioso. Ao contrário de cursos caros, aqui você tem o **caminho das pedras** direto e reto.
    
    **Como usar este app:**
    1. Escolha um método no menu lateral.
    2. Leia a teoria e observe as imagens.
    3. Execute as **Tarefas Práticas** ao final de cada página.
    4. Use o simulador para projetar seus lucros.
    """)

elif menu == "1. Mentalidade & Gestão":
    st.header("Capítulo 1: Domando o Dinheiro")
    st.image("https://images.unsplash.com/photo-1554224155-6726b3ff858f?auto=format&fit=crop&w=800&q=80")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("### O Método 50-30-20")
        st.write("Para prosperar, você precisa dividir seu dinheiro assim:")
        st.write("- **50% Necessidades:** Aluguel, comida, luz.")
        st.write("- **30% Desejos:** Lazer, assinaturas, hobbies.")
        st.write("- **20% Liberdade:** Investimentos e reserva.")
    
    with col2:
        st.write("### O Passo a Passo Técnico
